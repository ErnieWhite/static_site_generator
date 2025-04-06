from textnode import TextNode, TextType

def main():
    textnode = TextNode("Anchor", TextType.LINK, "https://www.boot.dev")
    print(textnode)

if __name__ == "__main__":
    main()
