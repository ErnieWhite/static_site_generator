from __future__ import annotations
from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:ParentNode | LeafNode, props=None):
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

