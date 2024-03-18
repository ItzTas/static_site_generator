class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        result = ""
        raise NotImplementedError("This feacture has not been implemented")

    def props_to_html(self):
        if not self.props or self.props == None:
            return ""
        html_atributes_str = ""
        for key, value in self.props.items():
            html_atributes_str += f" {key}=\"{value}\""
        return html_atributes_str
    
    def __repr__(self) -> str:
        return f"Class name: {self.__class__.__name__}\n \
              Tag: {self.tag} \n \
              Value: {self.value} \n \
              Children: {self.children} \n \
              Props: {self.props} \
              "

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, children=None,props=props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("All leafs nodes require a value")
        elif self.tag == None:
            return self.value
        elif self.tag != None:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        else:
            raise Exception("Something went wrong")
        
class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        result = ""
        if self.tag == None:
            raise ValueError("The tag cannot be None")
        elif not self.children or self.children == None:
            raise ValueError("The children cannot be None")
        for leaf in self.children:
            if hasattr(leaf, "to_html"):
                result += leaf.to_html()
        result = f"<{self.tag}{super().props_to_html()}>{result}</{self.tag}>"
        return result
