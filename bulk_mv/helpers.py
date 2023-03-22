def get_last_index_of_substring(string, substring):
    try:
        last_index = len(string) - 1 - string[::-1].index(substring)
        return last_index
    except ValueError:
        return -1
