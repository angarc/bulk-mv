import unittest
from bulk_mv import build_from_directory, FileTree, grammar, FileTreeVisitor
from pathlib import Path
import json


class TestBmvParser(unittest.TestCase):
    def sample1_file_contents(self):
        with open(f"{Path(__file__).parent}/dummy_bmv_files/sample1.bmv") as file:
            return file.read().strip()

        return None

    def test_file_tree_visitor(self):
        sample1 = self.sample1_file_contents()
        tree = grammar.parse(sample1)

        ftv = FileTreeVisitor()
        output = ftv.visit(tree)

        expected_output = {
            "move": [
                {"current_path": "web/static/", "new_path": "web/assets/"},
                {"current_path": "web/images/", "new_path": "web/static/assets/images/"},
                {"current_path": "web/images/photo.jpg", "new_path": "web/pages/images/profile_photos"},
            ],
            "rename": [
                {"old_name": "web/static/main.css", "new_name": "script.css"},
                {"old_name": "web/static/main.js", "new_name": "script.js"},
            ],
            "add": ["web/pages/images/profile_photos", "web/assets/"],
            "delete": ["web/images/delete_me.jpg"],
        }

        self.assertEqual(output, expected_output)
