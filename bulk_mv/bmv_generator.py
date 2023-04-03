class BmvGenerator:
    def __init__(self):
        pass

    def generate(self, tree):
        return self.generate_helper(tree, 0)

    def generate_helper(self, tree, depth):
        tab = ''.join(['\t'] * depth)
        tab_plus_one = tab + "\t"
        name = tree._path() if depth == 0 else tree.name()

        contents = tab + "[" + name + "] {\n"

        for child in tree.children():
            if not child._is_dir():
                contents += tab_plus_one + child.name() + "\n"

        for child in tree.children():
            if child._is_dir():
                contents += self.generate_helper(child, depth + 1)

        return contents + tab + "}\n"
