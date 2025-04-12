from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None): 
        # no children are allowed so pass None to the parent
        super().__init__(tag, value, None, props)

    def to_html(self):
        # if the leaf node has no value, it hsould raise a ValueError.  All leaf nodes must have a value.
        if self.value=="" or self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        # if there is no tag (e.g. it's None), the value should be returned as raw text.
        if self.tag is None:
            return self.value
        # otherwise, it should render an HTML tag. For example, these leaf nodes:
        #
        # LeafNode("p", "This is a paragraph of text.").to_html()
        # <p>This is a paragraph of text.</p>
        #
        # LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        # <a href="https://www.google.com">Click me!</a>
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


        
        

