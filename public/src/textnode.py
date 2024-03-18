class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"
    
    
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_type_text = "text"
    new_nodes = []
    allowed_text_types = ["text", "bold", "code", "italic"]
    if text_type not in allowed_text_types:
        raise Exception("Text type not allowed")
    
    for node in old_nodes:
        splitted_node_delimiter = node.text.split(delimiter)
        if not isinstance(node, TextNode):
            new_nodes.append(node)
        elif delimiter == None or delimiter == "":
            new_text_node = TextNode(text=node.text, text_type=text_type_text)
            new_nodes.append(new_text_node)
        elif len(splitted_node_delimiter) % 2 == 0:
            raise Exception("that's invalid Markdown syntax")

        else:
            
            for index, segment in enumerate(splitted_node_delimiter):
                if segment:
                    if index == 0 or index % 2 == 0:
                        text_node_text = TextNode(text=segment, text_type=text_type_text)
                        new_nodes.append(text_node_text)
                    
                    else:
                    
                        new_text_node_type = TextNode(text=segment, text_type=text_type)
                        new_nodes.append(new_text_node_type)
                
    return new_nodes    