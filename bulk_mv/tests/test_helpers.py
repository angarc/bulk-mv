import unittest
from bulk_mv import get_last_index_of_substring


class TestHelpers(unittest.TestCase):
    def test_get_last_index_of_substring_normal(self):
        file_path = "/path/to/some/file"

        last_index = get_last_index_of_substring(file_path, "/")

        self.assertEqual(last_index, 13)

    def test_get_last_index_of_substring_edge(self):
        string = "////////"

        last_index = get_last_index_of_substring(string, "/")

        self.assertEqual(last_index, 7)

    def test_get_last_index_of_substring_trivial(self):
        string = "/"

        last_index = get_last_index_of_substring(string, "/")

        self.assertEqual(last_index, 0)
