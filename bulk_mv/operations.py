from .helpers import get_last_index_of_substring
from os import path, remove, rename
from shutil import rmtree, move
from pathlib import Path


def perform_adds(paths):
    for new_path in paths:
        last_slash_index = get_last_index_of_substring(new_path, "/")
        directory = new_path[: last_slash_index + 1]
        filename = new_path[last_slash_index + 1 :]

        p = Path(directory)
        p.mkdir(parents=True, exist_ok=True)
        open(p / filename, 'a').close()


def perform_deletes(paths):
    for path_to_delete in paths:
        if path.exists(path_to_delete):
            if path.isdir(path_to_delete):
                rmtree(path_to_delete)
            elif path.isfile(path_to_delete):
                remove(path_to_delete)


def perform_renames(renamings):
    for renaming in renamings:
        old_name = renaming["old_name"]
        new_name = renaming["new_name"]
        rename(old_name, new_name)


def perform_moves(movements):
    for movement in movements:
        current_path = movement["current_path"]
        new_path = movement["new_path"]
        move(current_path, new_path)
