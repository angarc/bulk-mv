from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar(
    """
    line = ((unary_operation / binary_operation / entity) ws nl?)*
    entity = (directory / filename)
    unary_operation = (add / delete)
    binary_operation = (rename / move)

    directory  = ~"[a-zA-Z0-9/_\-\.]+"
    filename = ~"[A-Za-z0-9\./_\-]+"

    rename_op = "->"
    rename = entity rws rename_op rws entity

    move_op = "=>"
    move = entity rws move_op rws directory

    add_op = "+"
    add = add_op rws entity

    delete_op = "-"
    delete = delete_op rws entity

    rws = ~"\s+"
    ws = ~"\s*"
    nl = ~"\\n"
"""
)


class FileTreeVisitor(NodeVisitor):
    def visit_line(self, node, visited_children):
        output = {"move": [], "rename": [], "add": [], "delete": []}  # , "dir": [], "filename": []}
        for child in visited_children:
            if child[0][0] is not None:
                for key, val in child[0][0].items():
                    output[key].append(val)

        return output

    def visit_unary_operation(self, node, visited_children):
        return {node.children[0].expr_name: visited_children[0]}

    def visit_add(self, node, visited_children):
        _, *_, new_entity = node.children
        new_name = new_entity.text.strip()
        return new_name

    def visit_delete(self, node, visited_children):
        _, *_, old_entity = node.children
        old_name = old_entity.text.strip()
        return old_name

    def visit_binary_operation(self, node, visited_children):
        return {node.children[0].expr_name: visited_children[0]}

    def visit_move(self, node, visited_children):
        old_entity_name, _, move_op, *_, new_entity_name = node.children

        old_name = old_entity_name.children[0].text.strip()
        new_name = new_entity_name.text.strip()
        return {"current_path": old_name, "new_path": new_name}

    def visit_rename(self, node, visited_children):
        old_entity_name, _, rename_op, *_, new_entity_name = node.children
        old_name = old_entity_name.text.strip()
        new_name = new_entity_name.text.strip()
        return {"old_name": old_name, "new_name": new_name}

    def visit_entity(self, node, visited_children):
        # return visited_children[0][0]
        return None

    def visit_directory(self, node, visited_children):
        return {"dir": node.text}

    def visit_filename(self, node, visited_children):
        return {"filename": node.text}

    def visit_ws(self, node, visited_children):
        return ""

    def visit_move_op(self, node, visited_children):
        return ""

    def visit_rename_op(self, node, visited_children):
        return ""

    def visit_delete_op(self, node, visited_children):
        return ""

    def visit_add_op(self, node, visited_children):
        return ""

    def generic_visit(self, node, visited_children):
        """The generic visit method."""
        return visited_children or node
