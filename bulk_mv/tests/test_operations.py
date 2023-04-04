import unittest
from bulk_mv import (
    build_from_directory,
    parse_bmv,
    perform_adds,
    perform_deletes,
    perform_renames,
    perform_moves,
)
from os import path, remove, rename
from shutil import rmtree, move
import pathlib


class TestOperations(unittest.TestCase):
    def setUp(self):
        with open("bulk_mv/tests/dummy_bmv_files/sample3.bmv", "r") as file:
            self.output = parse_bmv(file.read().strip())

    def test_perform_adds(self):
        perform_adds(self.output["add"])

        self.assertTrue(path.exists("./bulk_mv/tests/dummy_directories/sample3/new_file.txt"))

        remove("./bulk_mv/tests/dummy_directories/sample3/new_file.txt")

    def test_perform_deletes(self):
        perform_deletes(self.output["delete"])

        self.assertTrue(not path.exists("./bulk_mv/tests/dummy_directories/sample3/markdown/2.md"))
        self.assertTrue(not path.exists("./bulk_mv/tests/dummy_directories/sample3/delete/"))

        open("./bulk_mv/tests/dummy_directories/sample3/markdown/2.md", 'a').close()
        pathlib.Path("./bulk_mv/tests/dummy_directories/sample3/delete/").mkdir(parents=True, exist_ok=True)
        open("./bulk_mv/tests/dummy_directories/sample3/delete/no_more.html", 'a').close()

    def test_perform_renames(self):
        perform_renames(self.output["rename_files"])
        perform_renames(self.output["rename_dirs"])

        self.assertTrue(path.exists("./bulk_mv/tests/dummy_directories/sample3/txt/"))

        rename("./bulk_mv/tests/dummy_directories/sample3/txt/", "./bulk_mv/tests/dummy_directories/sample3/text/")

    def test_perform_moves(self):
        perform_moves(self.output["move_files"])
        perform_moves(self.output["move_dirs"])

        self.assertTrue(path.exists("./bulk_mv/tests/dummy_directories/sample3/photos/markdown/"))

        move(
            "./bulk_mv/tests/dummy_directories/sample3/photos/markdown/",
            "./bulk_mv/tests/dummy_directories/sample3//markdown",
        )
