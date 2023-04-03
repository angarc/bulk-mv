import unittest
from bulk_mv import build_from_directory, parse_bmv, BmvGenerator
from pathlib import Path


class TestBmvGenerator(unittest.TestCase):
    def test_generator(self):
        self.maxDiff = 10000
        file_tree = build_from_directory(f"{Path(__file__).parent}/dummy_directories/sample1/")
        bmv_content = BmvGenerator().generate(file_tree)

        expected_output = (
            "[" + str(Path(__file__).parent) + "/dummy_directories/sample1] {\n"
            "\tindex.html\n"
            "\t[admin] {\n"
            "\t\tindex.html\n"
            "\t\tnichoal.html\n"
            "\t}\n"
            "\t[users] {\n"
            "\t\tangel.html\n"
            "\t\tindex.html\n"
            "\t\tjosh.html\n"
            "\t\t[blocked] {\n"
            "\t\t\tblocked_user_1.html\n"
            "\t\t}\n"
            "\t}\n"
            "}\n"
        )

        self.assertEqual(expected_output, bmv_content)
