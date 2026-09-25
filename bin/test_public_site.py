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

    def test_removed_book_reference_is_rejected(self):
        (self.root / "index.html").write_text('<a href="/projects/french-learning/">Book</a>')
        self.assertTrue(any("book still referenced" in e for e in validate(self.root)["errors"]))

    def test_native_summary_has_no_fake_anchor(self):
        doc = Document('<details><summary>Abstract</summary><p>Text</p></details>')
        self.assertTrue(any(t == "summary" for t, a in doc.tags))
        self.assertFalse(any(t == "a" for t, a in doc.tags))


if __name__ == "__main__":
    unittest.main()
