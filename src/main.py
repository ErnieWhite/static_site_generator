from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.url, "alt": text_node.text})
        
    raise ValueError(f"{text_node.text_type} is not implemented")


def main():
    textnode = TextNode("Anchor", TextType.LINK, "https://www.boot.dev")
    print(textnode)

if __name__ == "__main__":
    main()
