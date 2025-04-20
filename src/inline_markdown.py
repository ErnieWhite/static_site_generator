from textnode import TextNode, TextType
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
        new_nodes.extend(
            [
                TextNode(tokens[0], TextType.TEXT),
                TextNode(tokens[1], text_type),
                TextNode(tokens[2], TextType.TEXT)
            ]
        )
