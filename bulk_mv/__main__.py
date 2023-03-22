from .file_tree_builder import build_from_directory
from .parser import grammar, FileTreeVisitor
import sys
import json
from os import system

if __name__ == "__main__":  # pragma: no cover
    ft = build_from_directory(sys.argv[1])
    paths = ft.all_paths()

    with open("file_tree.bmv", "w") as file:
        file.write('\n'.join(paths))
    
    system("vim file_tree.bmv");

    with open("file_tree.bmv", "r") as file:
        tree = grammar.parse(file.read().strip())
        ftv = FileTreeVisitor()
        output = ftv.visit(tree)


        print(json.dumps(output, indent=4))

