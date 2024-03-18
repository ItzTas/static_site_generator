import unittest

from text_node_to_html_node import text_node_to_html_node

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

if __name__ == "__main__":
    unittest.main()