import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_ne_text(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is an image node", TextType.bold,)
        self.assertNotEqual(node, node2)

    def test_ne_texttype(self):
        node = TextNode("This is a text node", TextType.italic)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertNotEqual(node, node2)

    def test_ne_url(self):
        node = TextNode("This is an image node", TextType.image, "https://www.google.com")
        node2 = TextNode("This is an image node", TextType.image, "https://www.notgoogle.com")
        self.assertNotEqual(node, node2)

    def test_ne_url_none(self):
        node = TextNode("This is a link node", TextType.link, "https://google.com")
        node2 = TextNode("This is a link node", TextType.link, None)
        self.assertNotEqual(node, node2)

    def test_split_nodes_delim_none(self):
        node = TextNode("This is just a plain old line of text", TextType.text)
        new_nodes = split_nodes_delimiter([node], "", TextType.text)
        self.assertEqual(new_nodes, [TextNode("This is just a plain old line of text", TextType.text)])

    def test_split_nodes_delim_bold(self):
        node = TextNode("This is a text with a **bolded** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertEqual(new_nodes, [TextNode("This is a text with a ", TextType.text), TextNode("bolded", TextType.bold), TextNode(" word", TextType.text)])

    def test_split_nodes_delim_italic(self):
        node = TextNode("This is a text with an _italicized_ word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "_", TextType.italic)
        self.assertEqual(new_nodes, [TextNode("This is a text with an ", TextType.text), TextNode("italicized", TextType.italic), TextNode(" word", TextType.text)])

    def test_split_nodes_delim_code(self):
        node = TextNode("This is a text with a `code block` section", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertEqual(new_nodes, [TextNode("This is a text with a ", TextType.text),TextNode("code block", TextType.code), TextNode(" section", TextType.text)])

if __name__ == "__main__":
    unittest.main()
