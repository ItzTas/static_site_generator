from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

import re
class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, bold section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes    


def text_to_textnode(text):
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image([TextNode(text=text, text_type="text")])), "**", "bold"), "*", "italic"), "`", "code")
    
    #another option :
    
    #initial_nodes = [TextNode(text=text, text_type="text")]
    #nodes_after_bold = split_nodes_delimiter(old_nodes=initial_nodes, delimiter="**", text_type="bold")
    #nodes_after_italic = split_nodes_delimiter(old_nodes=nodes_after_bold, delimiter="*", text_type="italic")
    #nodes_after_code = split_nodes_delimiter(old_nodes=nodes_after_italic, delimiter="`", text_type="code")
    #nodes_after_image = split_nodes_image(old_nodes=nodes_after_code)
    #nodes_after_link = split_nodes_link(old_nodes=nodes_after_image)
    #return nodes_after_link

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


def extract_markdown_images (text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links (text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block.strip() == "":
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks

def block_to_block_type(block):
    count_hastag = 0
    count_digit = 0
    lines = block.split("\n")
    for i in range(0, 7):
        if i >= len(block):
            continue
        if block[i] != "#":
            break
        elif block[i] == "#":
            count_hastag += 1
            
    for letter in block:
        if letter.isdigit():
            count_digit += 1
        else:
            break
    if block.startswith("#") and count_hastag <= len(block) and block[count_hastag] == " " :
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```") or block.startswith("``") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_unordered_list
        return block_type_unordered_list
    if block[0].isdigit() and block[count_digit] == ".":
        return block_type_ordered_list
    else:
        return block_type_paragraph 
    