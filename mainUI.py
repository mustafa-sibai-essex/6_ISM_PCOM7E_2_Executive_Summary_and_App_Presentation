import tkinter as tk
from tkinter import ttk
from graphviz import Digraph
from nodeFactory import NodeFactory


class MainUI:
    def __init__(self, main_ui_container, graph_container, node_factory):
        self.main_ui_container = main_ui_container
        self.graph_container = graph_container
        self.node_factory = node_factory

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_name_label = tk.Label(frame, text="Node Name:")
        self.node_name_label.pack(side="left", anchor="w", padx=10)
        self.node_name_entry = tk.Entry(frame)
        self.node_name_entry.pack(side="left", anchor="w", padx=16)

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_parent_label = tk.Label(frame, text="Node Parent:")
        self.node_parent_label.pack(side="left", anchor="w", padx=10)
        self.node_parent_entry = tk.Entry(frame)
        self.node_parent_entry.pack(side="left", anchor="w", padx=10)

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_type_label = tk.Label(frame, text="Node Type:")
        self.node_type_label.pack(side="left", anchor="w", padx=10)
        self.node_type_var = tk.StringVar(frame)
        self.node_type_var.set("Or")  # Set default option
        self.node_type_dropdown = ttk.Combobox(
            frame, textvariable=self.node_type_var, values=["Or", "And"], width=17
        )
        self.node_type_dropdown.pack(side="left", anchor="w", padx=22)
        self.node_type_dropdown.config(state="readonly")

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_value_label = tk.Label(frame, text="Node Value:")
        self.node_value_label.pack(side="left", anchor="w", padx=10)
        self.node_value_entry = tk.Entry(frame)
        self.node_value_entry.pack(side="left", anchor="w", padx=16)

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.add_node_button = tk.Button(
            frame, text="Add Node", command=self.add_node, width=30
        )
        self.add_node_button.pack(side="left", anchor="w", padx=10)

        self.graph = Digraph(comment="Node Tree")

    def add_node(self):
        node_name = self.node_name_entry.get()
        node_parent = self.node_parent_entry.get()
        node_type = self.node_type_var.get()
        node_value = self.node_value_entry.get()

        if not node_name:
            print("Error: Node name cannot be empty.")
            return

        if not node_parent and self.node_factory.nodes:
            print(
                "You cannot create more than one parent nodes. This node should have a parent name. Please fill in the parent node name."
            )
            return

        node = self.node_factory.create_node(
            node_name, node_parent, node_type, node_value
        )

        if not node:
            return

        self.node_name_entry.delete(0, tk.END)
        self.node_parent_entry.delete(0, tk.END)
        self.node_value_entry.delete(0, tk.END)
        self.display_nodes()

    def display_nodes(self):
        self.graph.clear()
        for node in self.node_factory.get_nodes():
            self.graph.node(node.name, label=node.name)

            if node.parent:
                self.graph.edge(node.parent, node.name)

        self.graph.format = "png"
        self.graph.render("graph", view=False)

        if hasattr(self, "graph_view"):
            self.graph_view.destroy()

        self.graph_view = tk.Label(self.graph_container)
        self.graph_view.pack(side="top", anchor="w", pady=5)
        self.graph_view.img = tk.PhotoImage(file="graph.png")
        self.graph_view.config(image=self.graph_view.img)
