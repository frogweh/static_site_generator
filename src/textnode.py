from enum import Enum

class TextType(Enum):
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

class TextNode():
    def __init__(self, text,text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj):
        if not isinstance(obj, TextNode):
            return False
        else:
            return (
                self.text == obj.text and
                self.text_type == obj.text_type and
                self.url == obj.url
            )

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not delimiter:
        return old_nodes.copy()
    final = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            final.append(node)
            continue
        if delimiter not in node.text:
            final.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("Mismatched delimiter")
        for i, chunk in enumerate(split_text):
            type_to_use = TextType.text if i % 2 == 0 else text_type
            if chunk:
                final.append(TextNode(chunk, type_to_use))
    return final
