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

def extract_markdown_images(text):
    import re

    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    import re

    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    final = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            final.append(TextNode(node.text, node.text_type))
            continue
        images = extract_markdown_images(node.text)
        new_node = node.text
        if len(images) == 0:
            final.append(TextNode(node.text, TextType.text))
            continue
        for i in images:
            new_node = new_node.split(f"![{i[0]}]({i[1]})")
            if len(new_node[0]) > 0:
                final.append(TextNode(new_node[0], TextType.text))
            final.append(TextNode(i[0], TextType.image, i[1]))
            new_node = new_node[1]
        if len(new_node) > 0:
            final.append(TextNode(new_node, TextType.text))
    return final

def split_nodes_link(old_nodes):
    final = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            final.append(TextNode(node.text, node.text_type, node.url))
            continue
        links = extract_markdown_links(node.text)
        new_node = node.text
        if len(links) == 0:
            final.append(TextNode(node.text, TextType.text))
            continue
        for i in links:
            new_node = new_node.split(f"[{i[0]}]({i[1]})")
            if len(new_node[0]) > 0:
                final.append(TextNode(new_node[0], TextType.text))
            final.append(TextNode(i[0], TextType.link, i[1]))
            new_node = new_node[1]
        if len(new_node) > 0:
            final.append(TextNode(node.text, node.text_type, node.url))
    return final

def text_to_textnodes(text):
    node = TextNode(text, TextType.text)
    return split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            [node], "**", TextType.bold
                    ), "_", TextType.italic
                ), "`", TextType.code
            )
        )
    )
