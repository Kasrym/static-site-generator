import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("b", "Bold text")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold title"),
                LeafNode(None, " and subtext"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold title</b> and subtext</h2>"
        )

    def test_to_html_no_children(self):
        # Testing that a ValueError is raised when children are missing
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        # Testing that a ValueError is raised when tag is missing
        node = ParentNode(None, [LeafNode("b", "bold")])
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()