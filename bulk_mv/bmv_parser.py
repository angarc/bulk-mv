from lark import Lark, Transformer
from .helpers import get_last_index_of_substring


class TreeToOperations(Transformer):
    def start(self, items):
        return items[0]

    def dir(self, items):
        """Creates a dict representation of a directory.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a directory
        """
        dirname = items[1]['dir_op']['dirname']
        dirs = []
        files = []
        unary_ops = []
        file_op = []
        dir_op = []

        info_offset = 6
        if 'files' in items[info_offset]:
            files = items[info_offset]['files']
        if 'dirs' in items[info_offset]:
            dirs = items[info_offset]['dirs']
        if 'unary' in items[info_offset]:
            unary_ops = items[info_offset]['unary']
        if 'file_op' in items[info_offset]:
            for op in items[info_offset]['file_op']:
                if 'file' in op:
                    files.append(op['file'].value)
                elif 'rename_file_op' in op:
                    file_op.append(op)
                elif 'move_file_op' in op:
                    file_op.append(op)

        if 'move' in items[1]['dir_op']:
            dir_op.append({'move': items[1]['dir_op']['move']})
        if 'rename' in items[1]['dir_op']:
            dir_op.append({'rename': items[1]['dir_op']['rename']})

        return {
            'dir': {
                'dirname': dirname,
                'files': files,
                'unary': unary_ops,
                'dir_op': dir_op,
                'file_op': file_op,
                'dirs': dirs,
            }
        }

    def dir_op(self, items):
        """Creates a dict representation of a directory operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a directory operation
        """
        return {'dir_op': items[0]}

    def rename_dir_op(self, items):
        """Creates a dict representation of a directory rename operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a directory rename operation
        """
        old_name = items[0]['dirname']
        new_name = items[4]['dirname']
        return {'dirname': old_name, 'rename': {'old_name': old_name, 'new_name': new_name}}

    def move_dir_op(self, items):
        """Creates a dict representation of a directory move operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a directory move operation
        """
        current_name = items[0]['dirname']
        new_path = items[4]['dirname']
        return {'dirname': current_name, 'move': {'current_name': current_name, 'new_path': new_path}}

    def block(self, items):
        """Creates a dict representation of a block.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a block
        """
        files = []
        dirs = []
        unary_ops = []
        file_op = []
        dir_op = []

        for item in items:
            if 'file' in item:
                files.append(item['file'])
            elif 'dir' in item:
                dirs.append(item['dir'])
                for op in item['dir']['dir_op']:
                    if 'move' in op:
                        dir_op.append(op)
            elif 'unary' in item:
                unary_ops.append(item['unary'])
            elif 'file_op' in item:
                if 'file' in item['file_op']:
                    files.append(item['file_op']['file'])
                elif 'rename_file_op' in item['file_op']:
                    file_op.append(item['file_op'])
                elif 'move_file_op' in item['file_op']:
                    file_op.append(item['file_op'])

        return {'dirs': dirs, 'files': files, 'unary': unary_ops, 'file_op': file_op}

    def block_item(self, items):
        """Creates a dict representation of a block item.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a block item
        """
        return items[0]

    def entity(self, items):
        """Creates a dict representation of an entity.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of an entity
        """
        if 'file' in items[0]:
            return {'file': items[0]['file']}

        return items[0]

    def file_op(self, items):
        """Creates a dict representation of a file operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a file operation
        """
        return {'file_op': items[0]}

    def rename_file_op(self, items):
        """Creates a dict representation of a file rename operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a file rename operation
        """
        old_file_name = items[0]['file']
        new_file_name = items[4]['file']
        return {'rename_file_op': {'old_name': old_file_name, 'new_name': new_file_name}}

    def move_file_op(self, items):
        """Creates a dict representation of a file move operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a file move operation
        """
        current_name = items[0]['file']
        new_path = items[4]['dirname']
        return {'move_file_op': {'current_name': current_name, 'new_path': new_path}}

    def unary_op(self, items):
        """Creates a dict representation of a unary operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a unary operation
        """
        return {'unary': items[0]}

    def add_op(self, items):
        """Creates a dict representation of an add operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of an add operation
        """
        return {'add': items[1]}

    def delete_op(self, items):
        """Creates a dict representation of a delete operation.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a delete operation
        """
        return {'delete': items[1]}

    def dirname(self, items):
        """Creates a dict representation of a directory name.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a directory name
        """
        return {'dirname': items[0].value}

    def filename(self, items):
        """Creates a dict representation of a file name.

        Args:
            items (array): Array of node items from the Lark parser

        Returns:
            dict: dict representation of a file name
        """
        return {'file': items[0].value}

    def rename_op(self, _):
        return ">"

    def lbrace(self, _):
        return "{"

    def rbrace(self, _):
        return "}"

    def lbrack(self, _):
        return "["

    def rbrack(self, _):
        return "]"


def get_operations(tree, ops, current_path):
    """Extracts operation instructions from BMV Parse tree

    Args:
        tree (dict): BMV Parse tree
        ops (dict): Dictionary to store operations
        current_path (str): Current path of the directory

    Returns:
        dict: Dictionary of operations
    """
    for op in tree['unary']:
        if 'add' in op:
            if 'file' in op['add']:
                final_path = current_path + '/' + op['add']['file']
                ops['add'].append(final_path.replace("//", "/"))
            elif 'dir' in op['add']:
                final_path = current_path + '/' + op['add']['dir']['dirname']
                ops['add'].append((final_path + '/').replace("//", "/"))

                for file in op['add']['dir']['files']:
                    ops['add'].append((final_path + '/' + file).replace("//", "/"))

                get_operations(op['add']['dir'], ops, final_path.replace("//", "/"))

        elif 'delete' in op:
            if 'file' in op['delete']:
                final_path = current_path + '/' + op['delete']['file']
                ops['delete'].append(final_path.replace("//", "/"))
            elif 'dir' in op['delete']:
                final_path = current_path + '/' + op['delete']['dir']['dirname']
                ops['delete'].append((final_path + '/').replace("//", "/"))

    for op in tree['file_op']:
        if "rename_file_op" in op:
            old_path = current_path + '/' + op['rename_file_op']['old_name']
            new_path = current_path + '/' + op['rename_file_op']['new_name']
            ops['rename_files'].append({'old_path': old_path, 'new_path': new_path})
        if "move_file_op" in op:
            old_path = current_path + '/' + op['move_file_op']['current_name']
            new_path = op['move_file_op']['new_path']
            ops['move_files'].append({'current_path': old_path, 'new_path': new_path})

    for op in tree['dir_op']:
        if 'rename' in op:
            if current_path != op['rename']['old_name']:
                old_path = current_path + '/'

                last_slash_index = get_last_index_of_substring(current_path, "/")
                new_path = current_path[:last_slash_index] + '/' + op['rename']['new_name']
                ops['rename_dirs'].append({'old_path': old_path, 'new_path': new_path})
            else:
                ops['rename_dirs'].append(op['rename'])
        if 'move' in op:
            old_path = current_path + '/'
            new_path = op['move']['new_path']

            ops['move_dirs'].append({'current_path': old_path, 'new_path': new_path})

    for dir in tree['dirs']:
        final_path = current_path + '/' + dir['dirname']
        get_operations(dir, ops, final_path.replace('//', '/'))


def parse_bmv(data):
    """Parses a BMV string and returns a dictionary of operations

    Args:
        data (str): BMV string

    Returns:
        dict: Dictionary of operations
    """
    parser = Lark.open("bmv.lark", rel_to=__file__, parser='lalr')
    tree = parser.parse(data)
    res = TreeToOperations().transform(tree)

    ops = {'add': [], 'delete': [], 'rename_files': [], 'rename_dirs': [], 'move_files': [], 'move_dirs': []}
    get_operations(res['dir'], ops, res['dir']['dirname'])
    ops['rename_dirs'] = ops['rename_dirs'][::-1]

    return ops
