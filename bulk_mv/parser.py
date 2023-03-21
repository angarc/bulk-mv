from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import json

grammar = Grammar("""
    line = (unary_operation / binary_operation / entity)*
    entity = (filename / directory) ws
    unary_operation = (add / delete) ws
    binary_operation = (rename / move) ws

    directory  = ~"[a-zA-Z0-9/_]+"
    filename = ~"[a-zA-Z0-9/_]+\.[\w]+"

    rename_op = "->"
    rename = entity ws rename_op ws entity
    move_op = "=>"
    move = entity ws move_op ws directory
    add_op = "+"
    delete_op = "-"
    add = add_op ws entity
    delete = delete_op ws entity

    ws = ~"\s*"
""")

class FileTreeVisitor(NodeVisitor):
    def visit_line(self, node, visited_children):
        output = {"move": [], "rename": [], "add": [], "delete": []}
        for child in visited_children:
            if child[0] is not None:
                for key, val in child[0].items():
                    output[key].append(val)

        return output

    def visit_unary_operation(self, node, visited_children):
        bin_op, _ = node.children
        return {bin_op.children[0].expr_name: visited_children[0][0]}

    def visit_add(self, node, visited_children):
        _, *_, new_entity = node.children
        new_name = new_entity.text.strip()
        return new_name

    def visit_delete(self, node, visited_children):
        _, *_, old_entity = node.children
        old_name = old_entity.text.strip()
        return old_name

    def visit_binary_operation(self, node, visited_children):
        bin_op, _ = node.children
        return {bin_op.children[0].expr_name: visited_children[0][0]}

    def visit_move(self, node, visited_children):
        old_entity_name, _, rename_op, *_, new_entity_name = node.children

        old_name = old_entity_name.children[0].children[0].text.strip()
        new_name = new_entity_name.text.strip()
        return {"current_path": old_name, "new_path": new_name}

    def visit_rename(self, node, visited_children):
        old_entity_name, _, rename_op, *_, new_entity_name = node.children

        old_name = old_entity_name.children[0].children[0].text.strip()
        new_name = new_entity_name.children[0].children[0].text.strip()
        return {"old_name": old_name, "new_name": new_name}

    def visit_entity(self, node, visited_children):
        path, _ = node.children
        #return visited_children[0][0]
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
        """ The generic visit method. """
        return visited_children or node
