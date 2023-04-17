from tkinter import messagebox
from graphviz import Digraph
from nodeFactory import NodeFactory


class GraphFactory:
    def __init__(self):
        self.node_factory = NodeFactory()
        self.graph = Digraph(comment="Node Tree")

    def clear_graph(self):
        self.node_factory.clear()

    def add_node(self, node_name, node_description, node_parent, node_value):
        if not node_name:
            messagebox.showerror("Error", "Node name cannot be empty.")
            return

        if not node_description:
            messagebox.showerror("Error", "Node description cannot be empty.")
            return

        if not node_value and node_parent != '':
            messagebox.showerror("Error", "Node value cannot be empty.")
            return

        if not node_parent and self.node_factory.nodes:
            messagebox.showerror(
                "Error",
                "You cannot create more than one parent nodes. This node should have a parent name. Please fill in the parent node name.",
            )
            return

        return self.node_factory.create_node(
            node_name, node_description, node_parent, node_value
        )

    def create_graph(self, node_names=set()):
        self.graph.clear()
        if not node_names:
            node_names = set()

        else:
            node_names = set(node_names)

        for node in self.node_factory.get_nodes():
            label_text = f"{node.name}\n{node.description}\n{node.value}"
            node_color = "red" if node.name in node_names else "black"
            self.graph.node(node.name, label=label_text, color=node_color)

            if node.parent:
                edge_color = (
                    "red"
                    if node.name in node_names or node.parent in node_names
                    else "black"
                )
                self.graph.edge(node.parent, node.name, color=edge_color)

        self.graph.format = "png"
        self.graph.render("graph", directory="./output/", view=False)
