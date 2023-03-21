from os import listdir
from os.path import isdir
from .file_tree import FileTree

def build_from_directory(path):
    file_tree = FileTree(path)

    for entity_name in listdir(path):
        new_path = f"{path}/{entity_name}"
        
        child_file_tree = None
        if isdir(new_path):
            child_file_tree = build_from_directory(new_path)
        else:
            child_file_tree = FileTree(new_path)

        file_tree.add_child(child_file_tree)

    return file_tree

