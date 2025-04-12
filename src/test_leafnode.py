import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_props_node(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_with_props_node(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_value_None(self):
        node = LeafNode("p")
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have a value.")
