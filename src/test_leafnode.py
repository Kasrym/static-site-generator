import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_basic(self):
        # Test basic paragraph tag
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        # Test link tag with attributes
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_tag(self):
        # Test raw text (no tag)
        node = LeafNode(None, "Just some raw text.")
        self.assertEqual(node.to_html(), "Just some raw text.")

    def test_to_html_value_error(self):
        # Test that it raises ValueError when value is None
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        # Test that the __repr__ matches the requirements
        node = LeafNode("h1", "Title", {"class": "main"})
        self.assertEqual(repr(node), "LeafNode(h1, Title, {'class': 'main'})")

if __name__ == "__main__":
    unittest.main()