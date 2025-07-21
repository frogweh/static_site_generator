#print("Hello world")

from textnode import TextNode, TextType

main():
    text_node = TextNode("This is some anchor text", TextType.link, "https://www.boot.dev")
    print(text_node)

main()
