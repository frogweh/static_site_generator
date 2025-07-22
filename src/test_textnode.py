import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes


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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com)")
        self.assertListEqual([("to boot dev","https://www.boot.dev"),("to youtube","https://www.youtube.com")], matches)
    
    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.text,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode("second image", TextType.image, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode("This is text with a [link](https://www.boot.dev) and another [link too](https://www.google.com)", TextType.text,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("link", TextType.link, "https://www.boot.dev"),
                TextNode(" and another ", TextType.text),
                TextNode("link too", TextType.link, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
                [
                    TextNode("This is ", TextType.text),
                    TextNode("text", TextType.bold),
                    TextNode(" with an ", TextType.text),
                    TextNode("italic", TextType.italic),
                    TextNode(" word and a ", TextType.text),
                    TextNode("code block", TextType.code),
                    TextNode(" and an ", TextType.text),
                    TextNode("obi wan image", TextType.image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.text),
                    TextNode("link", TextType.link, "https://boot.dev"),
                ],
                nodes,
        )

if __name__ == "__main__":
    unittest.main()
