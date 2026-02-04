# Static Site Generator

A powerful, from-scratch static site generator built in Python. This tool transforms Markdown files into a full-featured HTML website, handling everything from directory recursion to complex inline Markdown parsing.

## 🚀 Features

* **Recursive Directory Mirroring**: Automatically crawls a `content/` directory and replicates the structure in `docs/`.
* **Markdown to HTML Conversion**: Supports headings, code blocks, quotes, ordered/unordered lists, and paragraphs.
* **Inline Styling**: Parses and renders **bold**, *italic*, `inline code`, and [links](https://google.com) using a custom regex-based tokenizer.
* **Templating Engine**: Injects generated HTML into a reusable `template.html` using custom placeholders.
* **Deployment Ready**: Configurable `basepath` support for hosting on GitHub Pages subdirectories.

## 🛠️ Technical Implementation & Learning

Building this project involved solving several complex engineering challenges:

### 1. Data Structures & Tree Traversals
I implemented a tree-based approach to HTML generation using `HTMLNode`, `ParentNode`, and `LeafNode` classes. This allowed for complex nesting (like lists within blocks) and ensured valid HTML output through recursive `to_html()` methods.

### 2. Regex and Tokenization
To handle inline markdown, I built a multi-stage extraction system that identifies patterns for images, links, and text styles, converting raw strings into a list of intermediate `TextNode` objects before final HTML rendering.

### 3. Functional Block Parsing
I developed logic to identify "blocks" of Markdown (paragraphs vs. lists vs. headers) using method chaining and list comprehensions. This included strict validation, such as ensuring ordered lists increment correctly ($1, 2, 3...$).

### 4. File I/O and Automation
The project automates the build process by:
* Safely cleaning the destination directory using `shutil`.
* Recursively copying static assets (images/CSS) via `os.path` manipulations.
* Generating a production-ready `/docs` folder compatible with GitHub Pages.

## 📋 How to Run

1.  Place your Markdown files in the `/content` folder.
2.  Place your CSS and images in the `/static` folder.
3.  Run the generation script:
    ```bash
    python3 src/main.py "/"
    ```
4.  To preview locally, start a server in the output directory:
    ```bash
    cd docs && python3 -m http.server 8888
    ```

---
*Developed as part of the [Boot.dev](https://www.boot.dev) Backend Engineering curriculum.*
