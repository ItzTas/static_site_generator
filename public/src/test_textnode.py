import unittest

from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link


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
        
class Test_split_nodes_delimiter(unittest.TestCase):
    def test_raise_exception(self):
        node = TextNode(text="this is a wrong **bold statement", text_type="bold")
                
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", "bold")
            
    def test_multiple_old_nodes(self):
        node = TextNode(text="this is a **bold statement**", text_type="bold")
        node1 = TextNode(text="this is another **bold statement** see?", text_type="bold")
        result = split_nodes_delimiter([node, node1], "**", "bold")
        expected = expected = [
            TextNode("this is a ", "text"),
            TextNode("bold statement", "bold"),
            TextNode("this is another ", "text"),
            TextNode("bold statement", "bold"),
            TextNode(" see?", "text"),
         ]

        
        self.assertEqual(result, expected)
        
class test_split_nodes_link_image(unittest.TestCase):
    def test_split_nodes_image_no_image_tag(self):
        nodes = [
            TextNode(text="This is just a text with no image", text_type="text"),
            TextNode(text="this is a text with a image ![image](https://test)", text_type="text")
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is just a text with no image", "text", None),
            TextNode("this is a text with a image ", "text", None),
            TextNode("image", "image", "https://test")
            ]
            
        self.assertEqual(result, expected)
        
    def test_split_nodes_image(self):
        nodes = [
            TextNode(text="This is a text with a pretty logo ![pretty logo](https://logo)", text_type="text"),
            TextNode(text="this is a text with a image ![image](https://test)", text_type="text")
            ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is a text with a pretty logo ", "text", None),
            TextNode("pretty logo", "image", "https://logo"),
            TextNode("this is a text with a image ", "text", None),
            TextNode("image", "image", "https://test")
            ]
        
        self.assertEqual(result, expected)
        
    def test_split_nodes_link(self):
        nodes = [
            TextNode(text="This is a text with a pretty link [pretty link](https://link)", text_type="text"),
            TextNode(text="this is a text with a link [link](https://test)", text_type="text")
            ]
        
        result = split_nodes_link(nodes)
        expected = [
            TextNode("This is a text with a pretty link ", "text", None),
            TextNode("pretty link", "link", "https://link"),
            TextNode("this is a text with a link ", "text", None),
            TextNode("link", "link", "https://test")
            ]
        
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()
