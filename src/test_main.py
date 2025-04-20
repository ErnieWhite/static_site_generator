import unittest
from main import text_node_to_html_node, split_nodes_delimiter
from textnode import TextNode, TextType

class TestMain(unittest.TestCase):

    def text_text_node_to_html_example(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)


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

    def text_text_node_to_html_example_2(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
           [ 
               TextNode("This is text with a ", TextType.TEXT),
               TextNode("code block", TextType.CODE),
               TextNode(" word", TextType.TEXT),
           ],
           new_nodes
        )

    def test_split_nodes_delimiter(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        delimiter = "**"
        split_node = split_nodes_delimiter([node], delimiter, TextType.BOLD)
        self.assertEqual([node], split_node)

    def test_split_nodes_delimiter_no_matching_delimiter(self):
        node = TextNode("This has malformed **bold text", TextType.TEXT)
        delimiter = "**"
        with self.assertRaises(SyntaxError) as context:
            split_node = split_nodes_delimiter([node], delimiter, TextType.BOLD)
            self.assertEqual(str(context.exception), f'Matching delimiter {delimiter} not found')

    def test_split_nodes_delimiter_start_bold(self):
        node = TextNode("**bold** at the start", TextType.TEXT)
        delimiter = "**"
        split_nodes = split_nodes_delimiter([node], delimiter, TextType.BOLD)
        self.assertEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" at the start", TextType.TEXT)
            ],
            split_nodes
        )
