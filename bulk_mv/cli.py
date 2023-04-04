from .file_tree_builder import build_from_directory
from .bmv_parser import parse_bmv
from .bmv_generator import BmvGenerator
from os import system
from .operations import perform_adds, perform_deletes, perform_renames, perform_moves


def run(start_path):
    """Runs the full pipeline for bmv.

    Args:
        start_path (str): The directory where you want to run bmv in.

    Returns:
        int: error code

    """
    ft = build_from_directory(start_path)
    bmv_content = BmvGenerator().generate(ft)

    with open("file_tree.bmv", "w") as file:
        file.write(bmv_content)

    system("vim file_tree.bmv")

    with open("file_tree.bmv", "r") as file:
        output = parse_bmv(file.read().strip())

    perform_adds(output["add"])
    perform_deletes(output["delete"])
    perform_renames(output["rename_files"])
    perform_renames(output["rename_dirs"])
    perform_moves(output["move_files"])
    perform_moves(output["move_dirs"])

    perform_deletes(['file_tree.bmv'])

    return 0
