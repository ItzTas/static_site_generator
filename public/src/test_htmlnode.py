import unittest

from htmlnode import HTMLNode, LeafNode

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
        
    def test_leaf_node_value_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode(value=None)
            node.to_html()
            
    def test_leaf_node_tag_none(self):
        node = LeafNode(value="test",tag=None)
        expected = "test"
        result = node.to_html()
        self.assertEqual(result, expected)
        
    def test_leaf_node_tag_not_none_no_props(self):
        node = LeafNode(value="test",tag="p")
        result = node.to_html()
        expected = "<p>test</p>"
        self.assertEqual(result, expected)
    
    def test_leaf_node_tag_not_none_with_props(self):
        node = LeafNode(value="test", tag="a", props={"href": "test"})
        result = node.to_html()
        expected = "<a href=\"test\">test</a>"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()