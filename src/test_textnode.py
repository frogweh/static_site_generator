import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
