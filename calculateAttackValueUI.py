import tkinter as tk
from tkinter import messagebox


class CalculateAttackValueUI:
    """This class adds all the UI necessary to calculate the attack value"""

    def __init__(self, calculate_attack_value_ui_container, main_ui, node_factory):
        """Constructor to initialize instance variables for the CalculateAttackValueUI class"""
        self.calculate_attack_value_ui_container = calculate_attack_value_ui_container
        self.node_factory = node_factory
        self.main_ui = main_ui

        # Create a new frame to hold the UI elements
        frame = tk.Frame(self.calculate_attack_value_ui_container)
        frame.pack(side="top", anchor="w", pady=0)

        self.note_label = tk.Label(
            frame,
            text="***Input must be the nodes name seperated with commas***\nexample a,b,c",
            justify="left",
        )
        self.note_label.pack(side="left", anchor="e", padx=0)

        # Create a new frame to hold the UI elements
        frame = tk.Frame(self.calculate_attack_value_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a label for the first node to calculate
        self.nodes_label = tk.Label(frame, text="Node to Calculate:")
        self.nodes_label.pack(side="left", anchor="w", padx=0)
        self.nodes_entry = tk.Entry(frame)
        self.nodes_entry.pack(side="left", anchor="w", padx=16)

        # Create an entry box for entering the node names to calculate
        frame = tk.Frame(self.calculate_attack_value_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a button to calculate the attack value of nodes
        self.calculate_value_of_nodes_button = tk.Button(
            frame,
            text="Calculate Nodes Attack Value",
            command=self.calculate_nodes_attack_value,
            width=40,
        )
        self.calculate_value_of_nodes_button.pack(side="left", anchor="w", padx=0)

    def calculate_nodes_attack_value(self):
        """Method to calculate the attack value of nodes. It goes through all the nodes and adds them together
        and set the root node to that value"""

        nodes_to_calculate = self.nodes_entry.get()
        node_names = []
        nodes = []

        # Split the input string and remove extra spaces from node names
        for node_name in nodes_to_calculate.split(","):
            node_names.append(node_name.strip())

        # Check if the first node name is empty
        if node_names[0] == "":
            messagebox.showerror("Error", "Node To Calculate cannot be empty")
            return

        # Get the root node and check if it exists
        node = self.node_factory.get_node_by_name(node_names[0])
        if node == None:
            return

        # Check if the first node is the root node
        if self.node_factory.get_node_by_name(node_names[0]).parent != None:
            messagebox.showerror(
                "Error", "The first element in Node To Calculate must be the root node."
            )
            return

        # Collect the nodes to calculate the attack value
        for node in self.node_factory.get_nodes():
            if node.name in node_names and node.parent:
                nodes.append(node)

        # Calculate the sum of the values of the nodes
        sum_of_values = sum(int(node.value) for node in nodes)

        # Set the value of the root node to the sum of the values of the nodes
        self.node_factory.get_node_by_name(node_names[0]).value = sum_of_values

        # Update the UI to display the updated nodes
        self.main_ui.display_nodes(node_names)
