"""Regression tests for the static publication validator. No network needed."""
import tempfile
import unittest
from pathlib import Path
from check_public_site import Document, local_target, prepare, validate


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        (self.root / "index.html").write_text('<main id="main-content"></main>')

    def test_self_host_without_path_resolves_to_home(self):
        source = self.root / "404.html"
        self.assertEqual(local_target(self.root, source, "https://xia-geom.github.io")[0], self.root / "index.html")

    def test_external_url_is_not_a_network_test(self):
        self.assertIsNone(local_target(self.root, self.root / "index.html", "https://example.org/a"))

    def test_fragment_resolves_to_current_page(self):
        self.assertEqual(local_target(self.root, self.root / "index.html", "#main-content"), (self.root / "index.html", "main-content"))

    def test_relative_escape_is_rejected(self):
        with self.assertRaises(ValueError):
            local_target(self.root, self.root / "index.html", "../../outside.txt")

    def test_prepare_keeps_academic_content(self):
        (self.root / "research").mkdir()
        paper = self.root / "research/index.html"
        paper.write_text("academic content")
        (self.root / "AGENTS.md").write_text("internal instructions")
        prepare(self.root)
        self.assertEqual(paper.read_text(), "academic content")
        self.assertFalse((self.root / "AGENTS.md").exists())
        self.assertTrue((self.root / ".nojekyll").exists())

    def test_prepare_is_idempotent(self):
        prepare(self.root)
        self.assertEqual(prepare(self.root), [])

    def test_prepare_removes_unused_theme_assets_and_sitemap_entries(self):
        demo = self.root / "assets/plotly/demo.html"
        demo.parent.mkdir(parents=True)
        demo.write_text("theme example")
        sitemap = self.root / "sitemap.xml"
        sitemap.write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                           '<url><loc>https://xia-geom.github.io/assets/plotly/demo.html</loc></url>'
                           '<url><loc>https://xia-geom.github.io/</loc></url></urlset>')
        prepare(self.root)
        self.assertFalse(demo.exists())
        self.assertNotIn("demo.html", sitemap.read_text())
        self.assertIn("https://xia-geom.github.io/", sitemap.read_text())

    def test_unprepared_theme_resume_is_rejected(self):
        resume = self.root / "assets/json/resume.json"
        resume.parent.mkdir(parents=True)
        resume.write_text('{"name":"Albert Einstein"}')
        self.assertTrue(any("Theme example published: assets/json/resume.json" in e
                            for e in validate(self.root)["errors"]))

    def test_ai_math_is_required_in_both_languages(self):
        result = validate(self.root)
        self.assertEqual(result["required_pages"], 18)
        for route in ("projects/ai-for-math", "fr/projects/ai-for-math"):
            self.assertIn(f"Required page absent: {route}/index.html", result["errors"])

    def test_invalid_structured_data_is_rejected(self):
        (self.root / "index.html").write_text('<script type="application/ld+json">{"name":broken}</script>')
        self.assertIn("index.html: invalid structured data JSON", validate(self.root)["errors"])

    def test_wrong_canonical_is_rejected(self):
        (self.root / "index.html").write_text('<link rel="canonical" href="https://example.org/">')
        self.assertIn("index.html: canonical URL missing or incorrect", validate(self.root)["errors"])

    def test_publication_disclosures_do_not_depend_on_abstract_wording(self):
        research = self.root / "research/index.html"
        research.parent.mkdir()
        research.write_text('<details><summary>Abstract</summary><p>Updated research on ℂℙ¹.</p></details>')
        self.assertFalse(any("empty publication disclosure" in e for e in validate(self.root)["errors"]))
        research.write_text('<details><summary>Abstract</summary></details>')
        self.assertIn("research/index.html: empty publication disclosure", validate(self.root)["errors"])

    def test_removed_book_reference_is_rejected(self):
        (self.root / "index.html").write_text('<a href="/projects/french-learning/">Book</a>')
        self.assertTrue(any("book still referenced" in e for e in validate(self.root)["errors"]))

    def test_native_summary_has_no_fake_anchor(self):
        doc = Document('<details><summary>Abstract</summary><p>Text</p></details>')
        self.assertTrue(any(t == "summary" for t, a in doc.tags))
        self.assertFalse(any(t == "a" for t, a in doc.tags))

    def test_abstract_prose_and_unicode_notations_are_accepted(self):
        for notation in ("complex projective line", "ℂℙ¹", "&#x2102;&#x2119;&#xb9;"):
            with self.subTest(notation=notation):
                for route in ("research", "fr/research"):
                    folder = self.root / route
                    folder.mkdir(parents=True, exist_ok=True)
                    (folder / "index.html").write_text(
                        f'<details><summary>Abstract</summary><p>{notation}</p></details>', encoding="utf-8")
                errors = validate(self.root)["errors"]
                self.assertFalse(any("empty publication disclosure" in e for e in errors))

    def test_missing_abstract_still_rejected_in_both_languages(self):
        for route in ("research", "fr/research"):
            folder = self.root / route
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "index.html").write_text('<details><summary>Abstract</summary></details>')
        errors = validate(self.root)["errors"]
        self.assertEqual(sum("empty publication disclosure" in e for e in errors), 2)


if __name__ == "__main__":
    unittest.main()
