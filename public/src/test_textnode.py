import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_diferent_text(self):
        node = TextNode("This is a text node", "bold")
        node3 = TextNode("THIS IS A TEXT NODE", "bold")
        self.assertNotEqual(node, node3)
        
    def test_eq_diferent_text_type(self):
        node5 = TextNode("This is a text node", "bold", "test")
        node6 = TextNode("This is a text node", "italic", "test")
        self.assertNotEqual(node5, node6)
        
    def test_eq_diferent_url(self):
        node4 = TextNode("This is a text node", "bold", "url")
        node5 = TextNode("This is a text node", "bold", "test")
        self.assertNotEqual(node4, node5)
        
    def test_repr(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))
        
        
        

if __name__ == "__main__":
    unittest.main()
