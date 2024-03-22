import os, shutil

filepath_to_static = "/home/talinux/workspace/github.com/itzTas/static_site_generator/static"
filepath_to_public = "/home/talinux/workspace/github.com/itzTas/static_site_generator/public"

def ensure_directory_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)
        
def remove_old_files(file_path):
    for item in os.path.listdir(file_path):
        item_path = os.path.join(file_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

def copy_static(src_directory, dest_directory):
    if not os.path.exists(dest_directory):
        os.mkdir(dest_directory)
     
    for item in os.listdir(src_directory):
        full_item_path = os.path.join(src_directory, item)
        dest_path = os.path.join(dest_directory, item)
        if not os.path.exists(full_item_path):
            continue
        if os.path.isfile(full_item_path):
            ensure_directory_exists(os.path.dirname(dest_path))
            shutil.copy(full_item_path, dest_path)
        elif os.path.isdir(full_item_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_static(full_item_path, dest_path)
            
copy_static(filepath_to_static, filepath_to_public)

def combination(src_directory, dest_directory):
    remove_old_files(dest_directory)
    copy_static(src_directory, dest_directory)
            
combination(filepath_to_static, filepath_to_public)