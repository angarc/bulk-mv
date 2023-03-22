from .file_tree_builder import build_from_directory
from .bmv_parser import grammar, FileTreeVisitor
from os import system
from .operations import perform_adds, perform_deletes, perform_renames, perform_moves


def run(start_path):
    ft = build_from_directory(start_path)
    paths = ft.all_paths()

    with open("file_tree.bmv", "w") as file:
        file.write('\n'.join(paths))

    system("vim file_tree.bmv")

    with open("file_tree.bmv", "r") as file:
        tree = grammar.parse(file.read().strip())
        ftv = FileTreeVisitor()
        output = ftv.visit(tree)

        # print(json.dumps(output, indent=4))

    perform_adds(output["add"])
    perform_deletes(output["delete"])
    perform_renames(output["rename"])
    perform_moves(output["move"])

    perform_deletes(['file_tree.bmv'])

    return 0
