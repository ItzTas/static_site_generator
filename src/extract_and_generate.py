from markdown_blocks import (
    markdown_to_html_node
)

from pathlib import Path

import os

def extract_title(markdown):
    lines = markdown.split("\n")
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:]
            break
    
    if not title:
        raise Exception("All pages need a single h1 header.")
    return title

def generate_page(from_path, template_path, dest_path):
    directory_path = os.path.dirname(dest_path)
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        path_contents = f.read()
        html_node = markdown_to_html_node(path_contents)
        html_text = html_node.to_html()
        title = extract_title(path_contents)
    with open(template_path) as f:
        template_contents = f.read()
        new_template_contents = template_contents.replace("{{ Title }}", title)
        new_template_contents = new_template_contents.replace("{{ Content }}", html_text)
    with open(dest_path, "w") as f:
        f.write(new_template_contents)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
            