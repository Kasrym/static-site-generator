from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = [block.strip() for block in markdown.split("\n\n")]
    return [block for block in blocks if block != ""]

def block_to_block_type(block):
    # Headings: 1-6 # followed by a space
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                break
        else:
            return BlockType.QUOTE
        
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                break
        else:
            return BlockType.UNORDERED_LIST
        
    if block.startswith("1."):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                break
            i += 1
        else:
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = create_node_from_block(block)
        children.append(html_node)
    return ParentNode("div", children)

def create_node_from_block(block):
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.QUOTE:
        return create_quote_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return create_ul_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return create_ol_node(block)
    if block_type == BlockType.CODE:
        return create_code_node(block)
    if block_type == BlockType.HEADING:
        return create_heading_node(block)
    return create_paragraph_node(block)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    # Remove the '#' symbols and the leading space
    content = block[level + 1:]
    children = text_to_children(content)
    return ParentNode(f"h{level}", children)

def create_code_node(block):
    # Strip the triple backticks from start and end
    content = block.strip("```").strip()
    content += "\n"
    # Code blocks wrap <code> inside <pre> and don't parse inline markdown
    code_node = ParentNode("code", [LeafNode(None, content)])
    return ParentNode("pre", [code_node])

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        # .lstrip("> ") removes the marker and the potential leading space
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def create_ul_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        # Extract text after the "- " or "* "
        content = line[2:]
        children = text_to_children(content)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ul", li_nodes)

def create_ol_node(block):
    lines = block.split("\n")
    li_nodes = []
    for line in lines:
        # Find the first space to strip the "i. " part
        first_space_idx = line.find(" ")
        content = line[first_space_idx + 1:]
        children = text_to_children(content)
        li_nodes.append(ParentNode("li", children))
    return ParentNode("ol", li_nodes)