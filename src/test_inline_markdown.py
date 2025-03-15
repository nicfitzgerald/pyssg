import unittest
from inline_markdown import (
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
)
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
  def test_delim_bold(self):
    node = TextNode("This is text with **bolded** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is text with ", TextType.TEXT),
        TextNode("bolded", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_delim_bold_double(self):
    node = TextNode(
      "This is a text with **bolded** word and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is a text with ", TextType.TEXT),
        TextNode("bolded", TextType.BOLD),
        TextNode(" word and ", TextType.TEXT),
        TextNode("another", TextType.BOLD),
      ],
      new_nodes,
    )

  def test_delim_multiword(self):
    node = TextNode(
      "This is a text with **bolded word** and **another**", TextType.TEXT
    )
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is a text with ", TextType.TEXT),
        TextNode("bolded word", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("another", TextType.BOLD),
      ],
      new_nodes,
    )

  def test_delim_italic(self):
    node = TextNode("This is text with _italic_ word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "_", TextType.BOLD)
    self.assertEqual(
      [
        TextNode("This is text with ", TextType.TEXT),
        TextNode("italic", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def test_delim_bold_and_italic(self):
    node = TextNode("**bold** and _italic_", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    self.assertEqual(
      [
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
      ],
      new_nodes,
    )

  def test_delim_code(self):
    node = TextNode("This is text with `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    self.assertEqual(
      [
        TextNode("This is text with ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.TEXT),
      ],
      new_nodes,
    )

  def text_extract_markdown_images(self):
    matches = extract_markdown_images(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual(
      [("image", "https://i.imgur.com/zjjcJKZ.png")],
      matches
    )

  def text_extract_markdown_links(self):
    matches = extract_markdown_links(
      "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
    )
    self.assertListEqual(
      [
        ("link", "https://boot.dev"),
        ("another link", "https://blog.boot.dev"),
       ],
      matches
    )


if __name__ == "__main__":
  unittest.main()