import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Tests that two nodes with identical properties are equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        # Tests that nodes with different text are NOT equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        # Tests that nodes with different text types are NOT equal
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        # Tests that nodes with the same URL are equal
        node = TextNode("This is a text node", TextType.ITALIC, "localhost:8888")
        node2 = TextNode("This is a text node", TextType.ITALIC, "localhost:8888")
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        # Tests that nodes with different URL are NOT equal
        node = TextNode("This is a text node", TextType.BOLD, "localhost:8888")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()