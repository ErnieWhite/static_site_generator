import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):

    def test_create_empty_node(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)

    def test_children_not_iterable(self):
        node = HTMLNode(None, None, None, None)
        try:
            if node.children:
                _ = [e for e in node.children]
        except TypeError():
            self.assertFalse(True)

    def test_single_props_to_html(self):
        SINGLE_PROP = {"href": "https://www.boot.dev"}
        node1 = HTMLNode(None, None, [None], SINGLE_PROP)
        self.assertEqual(node1.props_to_html(), ' href="https://www.boot.dev"')

    def test_multiple_props_to_html(self):
        MULTIPLE_PROPS = {"href": "https://www.boot.dev", "target": "_blank"}
        node = HTMLNode(None, None, None, MULTIPLE_PROPS)
        self.assertEqual(node.props_to_html(),' href="https://www.boot.dev" target="_blank"')

    def test_no_props_to_html(self):
        NO_PROPS = {}
        node = HTMLNode(None, None, None, NO_PROPS)
        self.assertEqual(node.props_to_html(), "")

    def test_none_props_to_html(self):
        NONE_PROPS = None
        node = HTMLNode(None, None, None, NONE_PROPS)
        self.assertEqual(node.props_to_html(), "")

    def test_repr_all_none(self):
        node = HTMLNode()
        string = str(node)
        self.assertEqual(string, 'HTMLNode(None, None, None, )')


if __name__ == "__main__":
    unittest.main()

