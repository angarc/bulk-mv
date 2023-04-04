from os import listdir
from os.path import isdir
from .file_tree import FileTree

ignore = ['.git', '.github', '.pytest-cache', '__pycache__', '.pytest_cache', 'node_modules', 'tmp']


def build_from_directory(path):
    """Builds a FileTree representation of a directory at a given path

    Args:
        path (str): Path to directory from which a FileTree will be created

    Returns:
        FileTree: The resulting FileTree
    """
    file_tree = FileTree(path)
    ignore_set = set(ignore)

    for entity_name in sorted(listdir(path)):
        new_path = f"{path}/{entity_name}"

        child_file_tree = None
        if isdir(new_path) and entity_name not in ignore_set:
            child_file_tree = build_from_directory(new_path)
            child_file_tree.is_directory = True
        else:
            child_file_tree = FileTree(new_path)

        if entity_name not in ignore_set:
            file_tree.add_child(child_file_tree)

    return file_tree
