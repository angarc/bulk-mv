import unittest
import random
from bulk_mv import build_from_directory, FileTree
from pathlib import Path
import os


class TestFileTree(unittest.TestCase):
    def build_sample_1(self):
        sample1 = build_from_directory(f"./bulk_mv/tests/dummy_directories/sample1/")
        return sample1

    def build_sample_2(self):
        sample2 = build_from_directory(f"./bulk_mv/tests/dummy_directories/sample2/")
        return sample2

    def build_sample_3(self):
        sample3 = build_from_directory(f"./bulk_mv/tests/dummy_directories/sample3/")
        return sample3

    def test_all_paths(self):
        sample3 = self.build_sample_3()
        expected_output = [
            './bulk_mv/tests/dummy_directories/sample3/',
            './bulk_mv/tests/dummy_directories/sample3/photos/',
            './bulk_mv/tests/dummy_directories/sample3/photos/test.jpg',
            './bulk_mv/tests/dummy_directories/sample3/markdown/',
            './bulk_mv/tests/dummy_directories/sample3/markdown/1.md',
            './bulk_mv/tests/dummy_directories/sample3/markdown/2.md',
            './bulk_mv/tests/dummy_directories/sample3/text/',
            './bulk_mv/tests/dummy_directories/sample3/text/1.txt',
            './bulk_mv/tests/dummy_directories/sample3/text/2.txt',
        ]

        output = sample3.all_paths()

        self.assertSetEqual(set(output), set(expected_output))

    def test_name(self):
        dir = FileTree("dir")
        dir.add_child(FileTree("file.txt"))

        sub_dir = FileTree("sub_dir")
        sub_dir.add_child(FileTree("test.txt"))
        dir.add_child(sub_dir)

        self.assertEqual(dir._name(), "dir")
        self.assertEqual(dir._children()[0]._name(), "file.txt")
        self.assertEqual(dir._children()[1]._name(), "sub_dir")
        self.assertEqual(dir._children()[1]._children()[0]._name(), "test.txt")

    def test_add_child(self):
        dir = FileTree("dir")
        sub_dir = FileTree("sub_dir")

        file_txt = FileTree("file.txt")
        test_txt = FileTree("test.txt")

        dir.add_child(file_txt)
        sub_dir.add_child(test_txt)
        dir.add_child(sub_dir)

        self.assertEqual(dir._path(), "dir")
        self.assertEqual(dir._children()[0]._path(), "dir/file.txt")
        self.assertEqual(dir._children()[1]._path(), "dir/sub_dir")
        self.assertEqual(dir._children()[1]._children()[0]._path(), "dir/sub_dir/test.txt")
        self.assertEqual(sub_dir._parent(), dir)
        self.assertEqual(file_txt._parent(), dir)
        self.assertEqual(test_txt._parent(), sub_dir)

    def test_inequality(self):
        sample1 = self.build_sample_1()
        sample2 = self.build_sample_2()

        self.assertNotEqual(sample1, sample2)

    def test_exact_equality(self):
        sample1 = self.build_sample_1()
        sample1_dup = self.build_sample_1()

        self.assertEqual(sample1, sample1_dup)

    def test_effective_equality(self):
        # What this means is suppose you have two directories A and B
        # (imagine A and B have the same name). If A has files: 1.txt, 2.txt and 3.txt
        # and B has files: 3.txt, 2.txt and 1.txt, A and B are equivalent. The order
        # in which the files are presented should not matter.

        sample1 = self.build_sample_1()
        sample1_dup = self.build_sample_1()

        stack = [sample1_dup]
        while stack:
            tree = stack.pop()
            random.shuffle(tree.children)

            for child in tree.children:
                if child._is_dir():
                    stack.append(child)

        self.assertEqual(sample1, sample1_dup)

    def test_extra_directory(self):
        sample1 = self.build_sample_1()
        ft = self.build_sample_1()

        dir = FileTree("some_dir")
        dir.add_child(FileTree("a.txt"))
        dir.add_child(FileTree("b.txt"))
        ft.add_child(dir)

        self.assertNotEqual(sample1, ft)

    def test_extra_file(self):
        sample1 = self.build_sample_1()
        ft = self.build_sample_1()
        ft.add_child(FileTree("some_file"))

        self.assertNotEqual(sample1, ft)
