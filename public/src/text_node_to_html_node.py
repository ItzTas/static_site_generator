from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    allowed_text_types = {"text": {}, "bold": {"tag": "b"}, "italic": {"tag": "i"}, "code": {"tag": "code"}, "link": {"tag": "a"}, "image": {"tag": "img"}}
    
    if text_node.text_type not in allowed_text_types:
        raise Exception("This text type is not allowed")
    
    else:
        text_type_info = allowed_text_types[text_node.text_type].copy()
        text_type_info["value"] = text_node.text
        
        if text_node.text_type == "link":
            text_type_info["props"] = {"href": text_node.url}
        elif text_node.text_type == "image":
            text_type_info["value"] = ""
            text_type_info["props"] = {"src": text_node.url, "alt": text_node.text}
        
        html_leaf_node = LeafNode(**text_type_info)
    return html_leaf_node
