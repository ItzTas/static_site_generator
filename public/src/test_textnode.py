import unittest

from textnode import TextNode, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnode, text_node_to_html_node, extract_markdown_images, extract_markdown_links


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

class TestTextToTextNode(unittest.TestCase):
    def test_one (self):
        node = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        result = text_to_textnode(node)
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
            ]
        self.assertEqual(result, expected)
        
class TestTextToHTML (unittest.TestCase):
    def test_Exception(self):
        node = TextNode(text="test", text_type="undefined")
        with self.assertRaises(Exception):
            node1 = text_node_to_html_node(node)

    def test_text_type_text(self):
        node = TextNode(text="test", text_type="text")
        node1 = text_node_to_html_node(node)
        expected = "Class name: LeafNode \n \
              Tag: None \n \
              Value: test \n \
              Children: None \n \
              Props: None \n \
              "
        self.assertEqual(repr(node1), expected)
    
    def test_text_type_bold(self):
        node = TextNode(text="test", text_type="bold")
        node1 = text_node_to_html_node(node)
        expected = "Class name: LeafNode \n \
              Tag: b \n \
              Value: test \n \
              Children: None \n \
              Props: None \n \
              "
        self.assertEqual(repr(node1), expected) 
        
    def test_text_type_link(self):
        node = TextNode(text="test", text_type="link", url="https//test")
        node1 = text_node_to_html_node(node)
        expected = "Class name: LeafNode \n \
              Tag: a \n \
              Value: test \n \
              Children: None \n \
              Props: {'href': 'https//test'} \n \
              "
        self.assertEqual(repr(node1), expected)
        
    def test_text_type_image(self):
        node = TextNode(text="test", text_type="image", url="https//test")
        node1 = text_node_to_html_node(node)
        expected = "Class name: LeafNode \n \
              Tag: img \n \
              Value:  \n \
              Children: None \n \
              Props: {'src': 'https//test', 'alt': 'test'} \n \
              "
        self.assertEqual(repr(node1), expected)
        
class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        node = "this is a ![image](https://test) and this is another ![another image](https://exemple)"
        result = extract_markdown_images(node)
        expected = [("image", "https://test"),("another image", "https://exemple")]
        self.assertEqual(result, expected)
        
    def test_extract_markdown_links(self):
        node = "this is a [link](https://test) and this is another [another link](https://exemple)"
        result = extract_markdown_links(node)
        expected = [("link", "https://test"),("another link", "https://exemple")]
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()
