from collections import deque
from .helpers import get_last_index_of_substring


class FileTree:
    def __init__(self, path):
        self.path = path if path[-1] != "/" else path[:-1]
        self._children = []
        self.parent = None
        self.is_directory = False

    def all_paths(self):
        """Genterates every path for every node under a FileTree node

        Returns:
            array: array of string paths
        """
        stack = [self]
        paths = []

        while stack:
            tree = stack.pop()
            paths.append(tree._path() + "/")

            for child in tree.children():
                if child._is_dir():
                    stack.append(child)
                else:
                    paths.append(child._path())

        return paths

    def add_child(self, child):
        """Adds a child FileTree node to the callee FileTree node

        Args:
            child (FileTree): the node to be made a child
        """
        self._children.append(child)
        child.parent = self
        child._set_path(f"{self._path()}/{child.name()}")

        def _update_paths_for_children(tree):
            if tree.children():
                stack = [tree]
                while stack:
                    tree = stack.pop()

                    for tree in tree.children():
                        tree._set_path(f"{tree._parent()._path()}/{tree.name()}")
                        stack.append(tree)

        _update_paths_for_children(child)

    def _set_path(self, path):
        self.path = path

    def children(self):
        """Gets the children of the callee FileTree node

        Returns:
            array: array of FileTree nodes
        """
        return self._children

    def _parent(self):
        return self.parent

    def _path(self):
        return self.path

    def _is_dir(self):
        return self.is_directory

    def name(self):
        """Gets the name of the callee FileTree node

        Is derived from the path. The name is the last substring of the path
        after the last slash.

        For example, if the path is "foo/bar/baz", the name is "baz".

        Returns:
            str: the name of the callee FileTree node
        """
        try:
            last_slash_index = get_last_index_of_substring(self._path(), "/")
            return self._path()[last_slash_index + 1 :]
        except ValueError:
            return self._path()

    def __eq__(self, other):
        stack = deque([self])
        other_stack = deque([other])

        while stack and other_stack:
            tree = stack.pop()
            other_tree = other_stack.pop()

            if len(tree.children()) != len(other_tree.children()):
                return False

            for child in tree.children():
                other_child = None
                for other_child in other_tree.children():
                    if child.name() == other_child.name():
                        break

                if not other_child or child.name() != other_child.name():
                    return False

                if len(child.children()) != len(other_child.children()):
                    return False

                if child._is_dir():
                    stack.append(child)
                    other_stack.append(other_child)

        return len(stack) == 0 and len(stack) == len(other_stack)
