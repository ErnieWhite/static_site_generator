import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
    
    def test_to_html_with_no_tag(self):
        child_node = LeafNode("span","child")
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode(None, [child_node]).to_html()
        self.assertEqual(str(context.exception), "All parent nodes must have a tag")

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "All parent nodes must have children")

    def test_to_thml_with_props(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("a", "Click me!")
        