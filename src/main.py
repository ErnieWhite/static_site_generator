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

def split_nodes_delimiter(old_nodes: TextNode, delimiter, text_type):

    new_nodes = []
    for old_node in old_nodes:

        # If an "old node" is not a TextType.TEXT type, just add it to the 
        # new list as-is, we only attempt to split "text" type objects
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        # If a matching closing delimiter is not found, raise an InvalidSyntax
        # exception
        # **bold** this is bold -> 3
        # this is **bold** -> 3
        # is **bold** bold -> 3
        # hello **bold** hi **bold** goobbye -> 5
        # **bold this is not bold -> ["", "bold this is not bold"] -> 2
        # **bold this **is** not bold -> ["", "bold this", "is", "not bold]"] -> 4
        tokens = old_node.text.split(delimiter)
        if len(tokens) % 2 != 1:
            raise SyntaxError(f'Matching delimiter "{delimiter}" not found')

    return new_nodes


def main():
    textnode = TextNode("Anchor", TextType.LINK, "https://www.boot.dev")
    print(textnode)

if __name__ == "__main__":
    main()
