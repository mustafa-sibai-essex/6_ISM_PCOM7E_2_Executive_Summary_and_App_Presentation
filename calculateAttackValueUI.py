import tkinter as tk
from tkinter import messagebox


class CalculateAttackValueUI:
    def __init__(self, calculate_attack_value_ui_container, main_ui, node_factory):
        self.calculate_attack_value_ui_container = calculate_attack_value_ui_container
        self.node_factory = node_factory
        self.main_ui = main_ui

        frame = tk.Frame(self.calculate_attack_value_ui_container)
        frame.pack(side="top", anchor="e", pady=5)

        self.nodes_label = tk.Label(frame, text="Node to Calculate:")
        self.nodes_label.pack(side="left", anchor="w", padx=0)
        self.nodes_label2 = tk.Label(frame, text="Node to Calculate2:")
        self.nodes_label2.pack(side="top", anchor="w", padx=0)
        self.nodes_entry = tk.Entry(frame)
        self.nodes_entry.pack(side="left", anchor="w", padx=16)

        frame = tk.Frame(self.calculate_attack_value_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.calculate_value_of_nodes_button = tk.Button(
            frame,
            text="Calculate Nodes Attack Value",
            command=self.calculate_nodes_attack_value,
            width=50,
        )
        self.calculate_value_of_nodes_button.pack(side="left", anchor="w", padx=0)

    def calculate_nodes_attack_value(self):
        nodes_to_calculate = self.nodes_entry.get()
        node_names = []
        nodes = []

        for node_name in nodes_to_calculate.split(","):
            node_names.append(node_name.strip())

        if node_names[0] == "":
            messagebox.showerror("Error", "Node To Calculate cannot be empty")
            return

        node = self.node_factory.get_node_by_name(node_names[0])

        if node == None:
            return

        if self.node_factory.get_node_by_name(node_names[0]).parent != None:
            messagebox.showerror(
                "Error", "The first element in Node To Calculate must be the root node."
            )
            return

        for node in self.node_factory.get_nodes():
            if node.name in node_names and node.parent:
                nodes.append(node)

        sum_of_values = sum(int(node.value) for node in nodes)

        self.node_factory.get_node_by_name(node_names[0]).value = sum_of_values
        self.main_ui.display_nodes(node_names)
