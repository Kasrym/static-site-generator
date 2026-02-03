from textnode import TextNode, TextType

def main():
    test_textNode = TextNode("This is some text", TextType.LINKS, "localhost:8888")
    print(test_textNode)


if __name__ == "__main__":
    main()