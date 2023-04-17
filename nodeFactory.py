from tkinter import messagebox
from node import Node


class NodeFactory:
    """This is a class that implements a NodeFactory.
    It can be used to create, delete, and retrieve Node objects.
    Nodes can be created with a name, description, and optional parent name and value.
    If a parent name is given, the new node will be added as a child to the parent node.
    """

    def __init__(self):
        """Initializing the NodeFactory object"""
        self.nodes = {}

    def clear(self):
        """Function to clear all the nodes from the NodeFactory object"""
        self.nodes = {}

    def create_node(self, name, description, parent_name=None, value=None):
        """Function to create a new node and add it to the NodeFactory object.
        The function takes a name, description, and optional parent name and value as arguments
        """
        if parent_name and parent_name not in self.nodes:
            messagebox.showerror("Error", f"Parent node '{parent_name}' not found.")
            return None

        if name in self.nodes:
            messagebox.showerror("Error", f"Node '{name}' already exists.")
            return None

        node = Node(name, description, parent_name, value)
        self.nodes[name] = node

        if parent_name:
            parent_node = self.nodes[parent_name]
            parent_node.add_child(node)

        return node

    def delete_node(self, name):
        """Function to delete a node from the NodeFactory object.
        The function takes a node name as argument"""
        if name not in self.nodes:
            messagebox.showerror("Error", f"Node '{name}' not found.")
            return

        def remove_node(node):
            for child in node.children:
                remove_node(child)
                if child.name in self.nodes:
                    del self.nodes[child.name]
            if node.name in self.nodes:
                del self.nodes[node.name]

        remove_node(self.nodes[name])

    def get_nodes(self):
        """Function to get a list of all the nodes in the NodeFactory object"""
        return list(self.nodes.values())

    def get_node_by_name(self, name):
        """Function to get a node object by its name.
        The function takes a node name as argument"""
        if name in self.nodes:
            return self.nodes[name]
        else:
            messagebox.showerror("Error", f"Node '{name}' not found.")
            return None
