from os import listdir
from os.path import isdir
from .file_tree import FileTree

ignore = ['.git', '.github', '.pytest-cache', '__pycache__', '.pytest_cache', 'node_modules', 'tmp']


def build_from_directory(path):
    file_tree = FileTree(path)
    ignore_set = set(ignore)

    for entity_name in listdir(path):
        new_path = f"{path}/{entity_name}"

        child_file_tree = None
        if isdir(new_path) and entity_name not in ignore_set:
            child_file_tree = build_from_directory(new_path)
        else:
            child_file_tree = FileTree(new_path)

        if entity_name not in ignore_set:
            file_tree.add_child(child_file_tree)

    return file_tree
