#!/usr/bin/env python3
"""Prepare and validate the exact static directory sent to GitHub Pages.

Use --prepare only on Jekyll's build output, never on the source repository.
No network requests, model calls, or repository writes are performed.
"""
from __future__ import annotations

import argparse
import json
import shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

SITE_HOST = "xia-geom.github.io"
PRIMARY = ("", "research", "teaching", "projects", "projects/math-video",
           "projects/conversation-archive", "cv", "travel")
FORBIDDEN = ("people", "books", "blog", "news", "repositories",
             "projects/french-learning", "fr/projects/french-learning")
GUIDES = ("AGENTS", "ANALYTICS", "CLAUDE", "QUICKSTART", "SEO", "TROUBLESHOOTING",
          "README", "CONTRIBUTING", "CUSTOMIZE", "FAQ", "INSTALL")
SAMPLES = ("assets/video/tutorial_al_folio.mp4", "assets/html/relativity.html",
           "assets/jupyter/blog.ipynb.html")


class Document(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.ids: set[str] = set()
        self.refs: list[str] = []
        self.text = text
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append((tag, data))
        if data.get("id"):
            self.ids.add(data["id"])
        if tag == "a" and data.get("name"):
            self.ids.add(data["name"])
        for key in ("href", "src", "poster"):
            if data.get(key):
                self.refs.append(data[key])
        if data.get("srcset"):
            for item in data["srcset"].split(","):
                if item.strip():
                    self.refs.append(item.strip().split()[0])


def local_target(root: Path, source: Path, ref: str):
    url = urlsplit(ref)
    if url.scheme and url.scheme not in ("http", "https"):
        return None
    if url.netloc and url.netloc != SITE_HOST:
        return None
    path = unquote(url.path)
    if url.netloc and not path:
        path = "/"
    if not path:
        target = source
    elif path.startswith("/"):
        target = root / path.lstrip("/")
    else:
        target = source.parent / path
    target = target.resolve()
    if not target.is_relative_to(root):
        raise ValueError(f"Reference leaves build directory: {ref}")
    if target.is_dir():
        target /= "index.html"
    elif not target.exists() and not target.suffix:
        target = target.with_suffix(".html")
    return target, unquote(url.fragment)


def prepare(root: Path) -> list[str]:
    removed = []
    paths = list(FORBIDDEN) + list(SAMPLES)
    paths += [f"{name}.{ext}" for name in GUIDES for ext in ("md", "html")]
    for path in paths:
        target = root / path
        if target.is_dir():
            shutil.rmtree(target)
            removed.append(path)
        elif target.exists():
            target.unlink()
            removed.append(path)
    # Branch-based Pages must serve this already-built output without a second Jekyll pass.
    (root / ".nojekyll").write_text("", encoding="utf-8")
    sitemap = root / "sitemap.xml"
    if sitemap.exists():
        tree = ET.parse(sitemap)
        for item in list(tree.getroot()):
            loc = item.find("{*}loc")
            if loc is None or not loc.text:
                continue
            resolved = local_target(root, root / "index.html", loc.text)
            if resolved and (not resolved[0].exists() or resolved[0].name.startswith("google")):
                tree.getroot().remove(item)
        tree.write(sitemap, encoding="utf-8", xml_declaration=True)
    return removed


def validate(root: Path) -> dict:
    errors = []
    pages = {p.resolve(): Document(p.read_text(encoding="utf-8-sig"))
             for p in root.rglob("*.html")}
    checked = 0
    for path, doc in pages.items():
        label = str(path.relative_to(root))
        if "french-learning" in doc.text or "français qui vit" in doc.text.lower():
            errors.append(f"{label}: removed book still referenced")
        for ref in doc.refs:
            try:
                resolved = local_target(root, path, ref)
            except ValueError as exc:
                errors.append(f"{label}: {exc}")
                continue
            if resolved is None:
                continue
            checked += 1
            target, fragment = resolved
            if not target.is_file():
                errors.append(f"{label}: missing local target {ref}")
            elif fragment and target in pages and fragment not in pages[target].ids:
                errors.append(f"{label}: missing fragment {ref}")
        for tag, attrs in doc.tags:
            if tag == "a" and attrs.get("role") == "button" and not attrs.get("href"):
                errors.append(f"{label}: non-keyboard disclosure anchor")
    for prefix in ("", "fr/"):
        for route in PRIMARY:
            path = (root / prefix / route / "index.html").resolve()
            doc = pages.get(path)
            label = str(path.relative_to(root))
            if doc is None:
                errors.append(f"Required page absent: {label}")
                continue
            if "main-content" not in doc.ids:
                errors.append(f"{label}: skip target missing")
            if not any(t == "nav" and "navbar-expand-lg" in a.get("class", "") for t, a in doc.tags):
                errors.append(f"{label}: narrow-screen navigation regression")
            langs = {a.get("hreflang") for t, a in doc.tags if t == "link" and a.get("rel") == "alternate"}
            if not {"en", "fr"}.issubset(langs):
                errors.append(f"{label}: language alternates missing")
            if route == "research":
                if not any(t == "summary" for t, a in doc.tags):
                    errors.append(f"{label}: native disclosure controls missing")
                if "complex projective line" not in doc.text:
                    errors.append(f"{label}: repaired abstract absent")
    fr_cv = pages.get((root / "fr/cv/index.html").resolve())
    if fr_cv:
        for text in ("sichuanais", "Coordonnées", "Formation"):
            if text not in fr_cv.text:
                errors.append(f"French CV missing: {text}")
        if "Contact Information" in fr_cv.text or "Professional Summary" in fr_cv.text:
            errors.append("French CV has untranslated template labels")
    for route in FORBIDDEN:
        if (root / route).exists():
            errors.append(f"Non-public route exists: {route}")
    for name in GUIDES:
        for ext in ("html", "md"):
            if (root / f"{name}.{ext}").exists():
                errors.append(f"Internal guide published: {name}.{ext}")
    if not (root / ".nojekyll").is_file():
        errors.append("Missing .nojekyll publication marker")
    return {"html_files": len(pages), "required_pages": 16,
            "local_references_checked": checked, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.site.resolve()
    if not root.is_dir() or not (root / "index.html").is_file():
        parser.error("Expected a built site directory containing index.html")
    removed = prepare(root) if args.prepare else []
    result = validate(root)
    result["removed_output_paths"] = removed
    output = json.dumps(result, ensure_ascii=False, indent=2)
    print(output)
    if args.report:
        args.report.write_text(output + "\n", encoding="utf-8")
    raise SystemExit(bool(result["errors"]))


if __name__ == "__main__":
    main()
