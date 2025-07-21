import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        node = ' href="https://www.google.com" target="_blank"'
        node2 = HTMLNode(props={"href":"https://www.google.com","target":"_blank"}).props_to_html()
        self.assertEqual(node, node2)

    def test_props_to_html_eq_none(self):
        node = None
        node2 = HTMLNode().props_to_html()
        self.assertEqual(node, node2)

    def test_props_to_html_eq_empty(self):
        node = None
        node2 = HTMLNode(props={}).props_to_html()
        self.assertEqual(node, node2)

    def test_props_to_html_ne_href(self):
        node = ' href="https://thisiswrong.com" target="_blank"'
        node2 = HTMLNode(props={"href":"https://www.google.com","target":"_blank"}).props_to_html()
        self.assertNotEqual(node, node2)

    def test_props_to_html_ne_target(self):
        node = ' href="https://thisiswrong.com" target="not_blank"'
        node2 = HTMLNode(props={"href":"https://www.google.com","target":"_blank"}).props_to_html()
        self.assertNotEqual(node, node2)

    def test_to_html_err(self):
        self.assertRaises(NotImplementedError, HTMLNode().to_html)

if __name__ == "__main__":
    unittest.main()
