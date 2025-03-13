import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_to_html_props(self):
    node = HTMLNode(
      "div",
      "Hello, World!",
      None,
      {"class": "greeting", "href": "https://boot.dev"}
    )
    self.assertEqual(
      node.props_to_html(),
      ' class="greeting" href="https://boot.dev"',
    )

  def test_values(self):
    node = HTMLNode(
      "div",
      "I wish I could read",
    )
    self.assertEqual(
      node.tag,
      "div"
    )
    self.assertEqual(
      node.value,
      "I wish I could read"
    )
    self.assertEqual(
      node.children,
      None
    )
    self.assertEqual(
      node.props,
      None
    )

  def test_repr(self):
    node = HTMLNode(
      "p",
      "What a strange world",
      None,
      {"class": "primary"},
    )
    self.assertEqual(
      node.__repr__(),
      "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
    )

  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, World!")
    self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click Me!", {"href": "https://google.com"})
    self.assertEqual(
      node.to_html(),
      '<a href="https://google.com">Click Me!</a>'
    )

  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "Hello, World!")
    self.assertEqual(node.to_html(), "Hello, World!")

if __name__ == "__main__":
  unittest.main()