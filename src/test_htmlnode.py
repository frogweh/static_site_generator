import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href":"https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(tag=None, value="There is no tag")
        self.assertEqual(node.to_html(), 'There is no tag')

    def test_leaf_to_html_no_value(self):
        self.assertRaises(ValueError, LeafNode(tag="a", value=None).to_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)

    def test_to_html_with_no_children(self):        
        self.assertRaises(ValueError, ParentNode("div", None).to_html)

    def test_to_html_with_no_tags(self): 
        self.assertRaises(ValueError, ParentNode(None, children = [LeafNode("b", "Your mother sucks cocks in hell!")]).to_html)

    def test_to_html_with_empty_list(self):
        self.assertEqual(ParentNode("div", []).to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()
