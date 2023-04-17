import tkinter as tk
from tkinter import ttk
from graphviz import Digraph
from nodeFactory import NodeFactory


class GraphFactory:
    def __init__(self):
        self.node_factory = NodeFactory()
        self.graph = Digraph(comment="Node Tree")

    def clear_graph(self):
        self.node_factory.clear()

    def add_node(self, node_name, node_parent, node_type, node_value):
        if not node_name:
            print("Error: Node name cannot be empty.")
            return

        if not node_parent and self.node_factory.nodes:
            print(
                "You cannot create more than one parent nodes. This node should have a parent name. Please fill in the parent node name."
            )
            return

        return self.node_factory.create_node(
            node_name, node_parent, node_type, node_value
        )

    def create_graph(self):
        self.graph.clear()
        for node in self.node_factory.get_nodes():
            self.graph.node(node.name, label=node.name)

            if node.parent:
                self.graph.edge(node.parent, node.name)

        self.graph.format = "png"
        self.graph.render("graph", directory="./output/", view=False)
