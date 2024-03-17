import unittest

from htmlnode import HTMLNode

class TestHTMLNode (unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode("<h1>", "this is a test")
        self.assertEqual(repr(node1),
              "Class name: HTMLNode\n \
              Tag: <h1> \n \
              Value: this is a test \n \
              Children: None \n \
              Props: None \
              ")
    