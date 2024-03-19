from textnodefuncs import extract_markdown_images, extract_markdown_links
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


def split_nodes_image (old_nodes):
    text_type_text = "text"
    text_type_image = "image"
    new_nodes = []
    
    for node in old_nodes:
        extracted_image_node = extract_markdown_images(node.text)
        
        if extracted_image_node == [] or not extracted_image_node or extracted_image_node == None:
            new_nodes.append(node)
            continue
        
        while extracted_image_node:
            splitted_sentence = node.text.split(f"![{extracted_image_node[0][0]}]({extracted_image_node[0][1]})", 1)
            if splitted_sentence[0]:
                text_node_text = TextNode(text=splitted_sentence[0], text_type=text_type_text)
            new_nodes.append(text_node_text)
            
            text_node_image = TextNode(text=extracted_image_node[0][0], text_type=text_type_image, url=extracted_image_node[0][1])
            new_nodes.append(text_node_image)
            node.text = splitted_sentence[1]
            extracted_image_node = extract_markdown_images(node.text)
            
        if node.text:
            text_node_text = TextNode(text=node.text, text_type=text_type_text)
            new_nodes.append(text_node_text)

    return new_nodes

def split_nodes_link (old_nodes):
    text_type_text = "text"
    text_type_link = "link"
    new_nodes = []
    
    for node in old_nodes:
        extracted_link_node = extract_markdown_links(node.text)
        
        if not extracted_link_node or extracted_link_node == None:
            new_nodes.append(node)
            continue
        
        while extracted_link_node:
            splitted_sentence = node.text.split(f"[{extracted_link_node[0][0]}]({extracted_link_node[0][1]})", 1)
            if splitted_sentence[0]:
                text_node_text = TextNode(text=splitted_sentence[0], text_type=text_type_text)
            new_nodes.append(text_node_text)
            
            text_node_link = TextNode(text=extracted_link_node[0][0], text_type=text_type_link, url=extracted_link_node[0][1])
            new_nodes.append(text_node_link)
            node.text = splitted_sentence[1]
            extracted_link_node = extract_markdown_links(node.text)
            
        if node.text:
            text_node_text = TextNode(text=node.text, text_type=text_type_text)
            new_nodes.append(text_node_text)

    return new_nodes