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
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        props_string = "" 
        for k,v in self.props.items():
            props_string += f' {k}="{v}"'
        return props_string

    def __repr__(self):
        props = self.props_to_html()
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {props})"
