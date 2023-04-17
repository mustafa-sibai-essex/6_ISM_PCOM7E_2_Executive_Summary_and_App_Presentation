from tkinter import messagebox
from graphviz import Digraph
from nodeFactory import NodeFactory


class GraphFactory:
    """This class represents a factory for creating a graph"""

    def __init__(self):
        """Initialize the factory with a node factory and a new Digraph object"""
        self.node_factory = NodeFactory()
        self.graph = Digraph(comment="Node Tree")

    def clear_graph(self):
        """Clears the graph and the node factory"""
        self.node_factory.clear()

    def add_node(self, node_name, node_description, node_parent, node_value):
        """Adds a new node to the graph and the node factory with the given attributes"""

        # Check that the node attributes are valid and show an error message if they are not
        if not node_name:
            messagebox.showerror("Error", "Node name cannot be empty.")
            return

        if not node_description:
            messagebox.showerror("Error", "Node description cannot be empty.")
            return

        if node_parent != "" and node_parent != None:
            if not node_value:
                messagebox.showerror("Error", "Node value cannot be empty.")
                return

            try:
                # try to parse the string to an integer
                node_value = int(node_value)
            except ValueError:
                messagebox.showerror("Error", "Node value has to be an integer.")
                return

        if not node_parent and self.node_factory.nodes:
            messagebox.showerror(
                "Error",
                "You cannot create more than one parent nodes. This node should have a parent name. Please fill in the parent node name.",
            )
            return

        # Create the new node and return it
        return self.node_factory.create_node(
            node_name, node_description, node_parent, node_value
        )

    def create_graph(self, node_names=set()):
        """Creates the graph with the current nodes in the node factory and the given set of node names"""

        # Clear the current graph and set the node names to display
        self.graph.clear()
        if not node_names:
            node_names = set()
        else:
            node_names = set(node_names)

        # Add each node to the graph with its label and color
        for node in self.node_factory.get_nodes():
            label_text = f"{node.name}\n{node.description}\n{node.value}"
            node_color = "red" if node.name in node_names else "black"
            self.graph.node(node.name, label=label_text, color=node_color)

            # Add an edge from the parent node to the current node (if it has a parent)
            # Color the node and edges red if the node_names array was set by the user
            if node.parent:
                edge_color = (
                    "red"
                    if node.name in node_names or node.parent in node_names
                    else "black"
                )
                self.graph.edge(node.parent, node.name, color=edge_color)

        # Set the graph format to PNG and render the graph to a file
        self.graph.format = "png"
        self.graph.render("graph", directory="./output/", view=False)
