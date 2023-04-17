import tkinter as tk
from tkinter import messagebox


class DeleteUI:
    """Adds the UI for deleting a node"""

    def __init__(self, delete_ui_container, main_ui, node_factory):
        """Initialize the DeleteUI object with delete_ui_container, node_factory, and main_ui parameters"""
        self.delete_ui_container = delete_ui_container
        self.node_factory = node_factory
        self.main_ui = main_ui

        # Create a new Frame widget for the Node to Delete label and entry field
        frame = tk.Frame(self.delete_ui_container)
        frame.pack(side="top", anchor="e", pady=5)

        # Add the Node to Delete label to the frame
        self.node_delete_label = tk.Label(frame, text="Node to Delete:")
        self.node_delete_label.pack(side="left", anchor="w", padx=0)

        # Add the Node to Delete entry field to the frame
        self.node_delete_entry = tk.Entry(frame)
        self.node_delete_entry.pack(side="left", anchor="w", padx=16)

        # Create a new Frame widget for the Delete Node button
        frame = tk.Frame(self.delete_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Add the Delete Node button to the frame
        self.delete_node_button = tk.Button(
            frame, text="Delete Node", command=self.delete_node, width=30
        )
        self.delete_node_button.pack(side="left", anchor="w", padx=0)

        frame = tk.Frame(self.delete_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Add the Delete Node button to the frame
        self.clear_graph_button = tk.Button(
            frame, text="Clear graph", command=self.main_ui.clear_graph_UI, width=30
        )
        self.clear_graph_button.pack(side="left", anchor="w", padx=0)

    def delete_node(self):
        """This function result in a node being deleted from the node factory class"""

        # Retrieve the value from the Node to Delete entry field
        node_to_delete = self.node_delete_entry.get()

        # If the Node to Delete entry is empty, display an error message and return
        if not node_to_delete:
            messagebox.showerror("Error", "Node name cannot be empty.")
            return

        # Delete the specified node using the node_factory instance variable
        self.node_factory.delete_node(node_to_delete)

        # Update the main user interface to display the updated list of nodes
        self.main_ui.display_nodes()
