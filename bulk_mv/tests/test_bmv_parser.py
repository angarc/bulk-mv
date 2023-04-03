import unittest
from bulk_mv import build_from_directory, FileTree, parse_bmv
from pathlib import Path


class TestBmvParser(unittest.TestCase):
    def sample1_file_contents(self):
        with open(f"{Path(__file__).parent}/dummy_bmv_files/sample1.bmv") as file:
            return file.read().strip()

    def test_file_tree_visitor(self):
        sample1 = self.sample1_file_contents()
        output = parse_bmv(sample1)

        expected_output = {
            "add": ["web/assets/", "web/pages/images/", "web/pages/images/profile_photos/"],
            "delete": ["web/pages/images/delete_me.jpg"],
            "rename_files": [
                {"old_path": "web/static/main.css", "new_path": "web/static/script.css"},
                {"old_path": "web/static/main.js", "new_path": "web/static/script.js"},
            ],
            "rename_dirs": [],
            "move_files": [
                {"current_path": "web/pages/images/photo.jpg", "new_path": "web/pages/images/profile_photos"}
            ],
            "move_dirs": [{"current_path": "web/static/", "new_path": "web/assets"}],
        }

        self.assertEqual(output, expected_output)
