import unittest

from textnodefuncs import text_node_to_html_node, extract_markdown_images, extract_markdown_links

from textnode import TextNode


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
        
    def test_extract_markdown_images(self):
        node = "this is a [link](https://test) and this is another [another link](https://exemple)"
        result = extract_markdown_links(node)
        expected = [("link", "https://test"),("another link", "https://exemple")]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()