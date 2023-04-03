import unittest
from bulk_mv import build_from_directory, parse_bmv, BmvGenerator, dict_representation

class TestBmvGenerator(unittest.TestCase):
    def test_generator(self):
        file_tree = build_from_directory("./bulk_mv/tests/dummy_directories/sample1")
        bmv_content = BmvGenerator().generate(file_tree)

        output = dict_representation(bmv_content)
        expected_output = {
            "dir": {
                "dirname": "./bulk_mv/tests/dummy_directories/sample1",
                "files": [
                    "index.html"
                ],
                "unary": [],
                "dir_op": [],
                "file_op": [],
                "dirs": [
                    {
                        "dirname": "admin",
                        "files": [
                            "index.html",
                            "nichoal.html"
                        ],
                        "unary": [],
                        "dir_op": [],
                        "file_op": [],
                        "dirs": []
                    },
                    {
                        "dirname": "users",
                        "files": [
                            "josh.html",
                            "angel.html",
                            "index.html"
                        ],
                        "unary": [],
                        "dir_op": [],
                        "file_op": [],
                        "dirs": [
                            {
                                "dirname": "blocked",
                                "files": [
                                    "blocked_user_1.html"
                                ],
                                "unary": [],
                                "dir_op": [],
                                "file_op": [],
                                "dirs": []
                            }
                        ]
                    }
                ]
            }
        }

        self.assertEqual(output, expected_output)
