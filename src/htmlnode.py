class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value

        # force self.children to be iterable if not None
        try:
            self.children = [e for e in children]
        except TypeError:
            if children:
                self.children = [children]
            else:
                self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = "" 
        for k,v in self.props.items():
            props_string += f' {k}="{v}"'
        return props_string

    def __repr__(self):
        props = self.props_to_html()
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # no children are allowed so pass None to the parent
        super().__init__(tag, value, None, props)

    def to_html(self):
        # if the leaf node has no value, it hsould raise a ValueError.  All leaf nodes must have a value.
        if self.value == "" or self.value is None:
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


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def children_to_html(self):
        result_html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result_html += child.to_html()
        result_html += f"</{self.tag}>"
        return result_html

    def to_html(self):
        # if the object doesn't have a tag, raise a ValueError
        if self.tag is None or self.tag == "":
            raise ValueError("All parent nodes must have a tag")
        # if children is missing, raise a ValueError
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        # otherwise, return a string representing the HTML tag of the node and its children recursively.
        child_html = self.children_to_html()
        return child_html
