import unittest
from main import text_node_to_html_node
from textnode import TextNode, TextType

class TestMain(unittest.TestCase):

    def test_text_node_to_html_text(self):
        text = "This is a text node"
        node = TextNode(text, TextType.TEXT)

        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, text)
    
    def test_text_node_to_html_bold(self):
        text = "This a bold node"
        node = TextNode(text, TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, text)

    def test_text_node_to_html_italic(self):
        text = "This is an italic node"
        node = TextNode(text, TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, text)

    def test_text_node_to_html_link(self):
        text = "This is a link node"
        url = "https://www.boot.dev"
        node = TextNode(text=text, url=url, text_type=TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, text)
        self.assertEqual(html_node.props["href"], url)
