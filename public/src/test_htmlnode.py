import unittest

from htmlnode import HTMLNode

class TestHTMLNode (unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("<h1>", "this is a test")
        self.assertEqual(repr(node),
              "Class name: HTMLNode\n \
              Tag: <h1> \n \
              Value: this is a test \n \
              Children: None \n \
              Props: None \
              ")
    
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "width": "150px"})
        expected_result = ' href="https://www.google.com" target="_blank" width="150px"'
        self.assertEqual(node.props_to_html(), expected_result)
