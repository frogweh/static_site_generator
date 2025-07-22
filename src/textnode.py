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



