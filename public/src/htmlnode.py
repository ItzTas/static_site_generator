class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
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
              