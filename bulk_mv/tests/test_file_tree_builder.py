import unittest
from bulk_mv import build_from_directory, FileTree
from pathlib import Path


class TestFileTreeBuilder(unittest.TestCase):
    def build_sample_1(self):
        sample1 = build_from_directory(f"{Path(__file__).parent}/dummy_directories/sample1/")
        return sample1

    def build_sample_2(self):
        sample2 = build_from_directory(f"{Path(__file__).parent}/dummy_directories/sample2/")
        return sample2

    def test_build_from_directory_trivial(self):
        sample2 = self.build_sample_2()

        ft = FileTree("sample2")
        ft.add_child(FileTree("a.txt"))
        ft.add_child(FileTree("b.txt"))
        ft.add_child(FileTree("c.txt"))
        ft.add_child(FileTree("readme.md"))

        data_folder = FileTree("data")
        data_folder.add_child(FileTree("report.csv"))

        web_folder = FileTree("web")
        web_folder.add_child(FileTree("index.html"))
        web_folder.add_child(FileTree("main.css"))
        web_folder.add_child(FileTree("main.js"))

        ft.add_child(data_folder)
        ft.add_child(web_folder)

        self.assertEqual(sample2, ft)
