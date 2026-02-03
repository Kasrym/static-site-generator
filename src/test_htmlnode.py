import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_formatting(self):
        # Test that it creates the correct string format
        node = HTMLNode(tag="div", props={"class": "hero", "id": "main"})
        expected = ' class="hero" id="main"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_single(self):
        # Test that a single property works
        node = HTMLNode(tag="a", props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_none(self):
        # Test that if props is None, it returns an empty string
        node = HTMLNode(tag="p", value="Hello", props=None)
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()