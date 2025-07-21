class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

    def to_html(self):
        raise NotImplementedError("Will be overwritten by child classes.")

    def props_to_html(self):
        if self.props:
            tmp = ""
            for key, value in self.props.items():
                tmp += (f' {key}="{value}"')
            return tmp

    class LeafNode():
        def __init__(self, tag = None, value):
            self.tag = tag
            self.value = value

        def to_html(self):
            raise NotImplementedError("Not written yet")
