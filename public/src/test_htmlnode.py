import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_leaf_node_tag_not_none_with_multiple_props(self):
        node = LeafNode(value="test", tag="a", props={"href": "test", "width": "15px"})
        result = node.to_html()
        expected = "<a href=\"test\" width=\"15px\">test</a>"
        self.assertEqual(result, expected)
        
    def test_parent_node_no_tag (self):
        node = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_node_no_tag (self):
        node = ParentNode(tag="p", children=[])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_node_no_props (self):
        node = ParentNode(tag="div", 
            children = [
            LeafNode("bold text", "strong"),
            LeafNode("normal text", None),
            LeafNode("italic text", "em"),
        ])
        result = node.to_html()
        expected = "<div><strong>bold text</strong>normal text<em>italic text</em></div>"
        self.assertEqual(result, expected)
        
    def test_parent_node_with_props (self):
        node = ParentNode(tag="div", 
            children = [
            LeafNode("bold text", "strong", {"class": "test"}),
            LeafNode("normal text", None, {"id": "test"}),
            LeafNode("link", "a", {"href": "https://test"}),
        ])
        result = node.to_html()
        expected = "<div><strong class=\"test\">bold text</strong>normal text<a href=\"https://test\">link</a></div>"
        self.assertEqual(result, expected)
        
    def test_parent_node_inside_parent_node (self):
        node = ParentNode(tag="div", props={"class": "container"},
            children = [
            LeafNode("bold text", "strong", {"class": "test"}),
            ParentNode(tag="main", props={"id": "main"}, children=[
                LeafNode("bold text", "strong", {"class": "test"}),
                LeafNode("normal text", None, {"id": "test"}),
                LeafNode("image", "img", {"src": "https://test"}),
            ]),
            LeafNode("link", "a", {"href": "https://test"}),
        ])
        result = node.to_html()
        expected = '<div class="container"><strong class="test">bold text</strong><main id="main"><strong class="test">bold text</strong>normal text<img src="https://test">image</img></main><a href="https://test">link</a></div>'
        self.assertEqual(result, expected)
        
    def test_parent_node_inside_parent_node_inside_parent_node (self):
        node = ParentNode(tag="div", props={"class": "container"},
            children = [
            LeafNode("bold text", "strong", {"class": "test"}),
            ParentNode(tag="main", props={"id": "main"}, 
                children=[
                ParentNode(tag="main", props={"id": "main"}, 
                    children=[
                    LeafNode("image", "img", {"src": "https://test"}),
            ]),]),
            LeafNode("link", "a", {"href": "https://test"}),
        ])
        result = node.to_html()
        expected = '<div class="container"><strong class="test">bold text</strong><main id="main"><main id="main"><img src="https://test">image</img></main></main><a href="https://test">link</a></div>'
        self.assertEqual(result, expected)
        

if __name__ == "__main__":
    unittest.main()