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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value.")
            
        if not self.tag:
            return self.value

        if not self.props:
            return (f"<{self.tag}>{self.value}</{self.tag}>")
        else:
            return (f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>')

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")

        if self.children is None:
            raise ValueError("ParentNode must have children otherwise it's a LeafNode.")

        tmp = ""
        for i in self.children:
            tmp += i.to_html()

        if not self.props:
            return (f'<{self.tag}>{tmp}</{self.tag}>')
        else:
            return (f'<{self.tag}{super().props_to_html()}>{tmp}</{self.tag}>')
