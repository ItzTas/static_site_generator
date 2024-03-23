from copystatic import(
    remove_old_files,
    copy_static,
    filepath_to_public,
    filepath_to_static,
)

from extract_and_generate import (
    generate_pages_recursive
)


def combination(src_directory, dest_directory):
    print("---Removing old files---")
    remove_old_files(dest_directory)
    
    print("---Importing files---")
    copy_static(src_directory, dest_directory)
    print("---done---")
            
combination(filepath_to_static, filepath_to_public)
generate_pages_recursive("/home/talinux/workspace/github.com/itzTas/static_site_generator/content", "/home/talinux/workspace/github.com/itzTas/static_site_generator/template.html", "/home/talinux/workspace/github.com/itzTas/static_site_generator/public")

