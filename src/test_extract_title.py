import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        # Basic case
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_with_whitespace(self):
        # Header with extra spaces
        markdown = "#    Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_multiline(self):
        # H1 buried in other text
        markdown = """
This is a paragraph.

# The Real Title

Other content.
"""
        self.assertEqual(extract_title(markdown), "The Real Title")

    def test_extract_title_no_h1(self):
        # Missing H1 should raise an Exception
        markdown = "## Only an H2 here"
        with self.assertRaises(Exception) as cm:
            extract_title(markdown)
        self.assertEqual(str(cm.exception), "No h1 header found in markdown")

    def test_extract_title_wrong_start(self):
        # '#' must be followed by a space to be a valid header
        markdown = "#NoSpaceTitle"
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()