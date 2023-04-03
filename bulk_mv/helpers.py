def get_last_index_of_substring(string, substring):
    """Returns index of the final substring occurring in a given string
    For example, the index of the last '/' character in
    path/to/some/file is 12.

    Args:
        string (str): The full string
        substring (str): The substring your searching for in string

    Returns:
        int: the last index, or -1 if the substring is not found
    """

    try:
        last_index = len(string) - 1 - string[::-1].index(substring)
        return last_index
    except ValueError:
        return -1
