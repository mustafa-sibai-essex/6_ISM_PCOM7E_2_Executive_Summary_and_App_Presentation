import tkinter as tk
from tkinter import ttk


class MainUI:
    def __init__(self, main_ui_container, graph_container, graph_factory):
        self.main_ui_container = main_ui_container
        self.graph_container = graph_container
        self.graph_factory = graph_factory

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_name_label = tk.Label(frame, text="Node Name:")
        self.node_name_label.pack(side="left", anchor="w", padx=10)
        self.node_name_entry = tk.Entry(frame)
        self.node_name_entry.pack(side="left", anchor="w", padx=16)

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_description_label = tk.Label(frame, text="Node Description:")
        self.node_description_label.pack(side="left", anchor="w", padx=10)
        self.node_description_entry = tk.Entry(frame)
        self.node_description_entry.pack(side="left", anchor="w", padx=16)

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_parent_label = tk.Label(frame, text="Node Parent:")
        self.node_parent_label.pack(side="left", anchor="w", padx=10)
        self.node_parent_entry = tk.Entry(frame)
        self.node_parent_entry.pack(side="left", anchor="w", padx=10)

        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

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

    def add_node(self):
        node_name = self.node_name_entry.get()
        node_description = self.node_description_entry.get()
        node_parent = self.node_parent_entry.get()
        node_value = self.node_value_entry.get()

        node = self.graph_factory.add_node(
            node_name, node_description, node_parent, node_value
        )

        if node:
            self.node_name_entry.delete(0, tk.END)
            self.node_description_entry.delete(0, tk.END)
            self.node_parent_entry.delete(0, tk.END)
            self.node_value_entry.delete(0, tk.END)
            self.display_nodes()

    def display_nodes(self, node_names=set()):
        self.graph_factory.create_graph(node_names)

        if hasattr(self, "graph_view"):
            self.graph_view.destroy()

        self.graph_view = tk.Label(self.graph_container)
        self.graph_view.pack(side="top", anchor="w", pady=5)
        self.graph_view.img = tk.PhotoImage(file="./output/graph.png")
        self.graph_view.config(image=self.graph_view.img)
