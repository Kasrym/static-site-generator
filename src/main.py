from gencontent import generate_pages_recursive
from textnode import TextNode, TextType
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    prepare_public_directory()
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public
    )

def prepare_public_directory():
    print("Cleaning public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)
    
def copy_files(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        to_path = os.path.join(dest_dir_path, filename)

        print (f" * {from_path} -> {to_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files(from_path, to_path)

if __name__ == "__main__":
    main()