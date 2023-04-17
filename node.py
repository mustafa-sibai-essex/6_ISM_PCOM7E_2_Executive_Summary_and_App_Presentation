# This is a class that implements a Node object.
class Node:
    """This class holds all the data related to the Node class such as name, description, parent and value"""

    def __init__(self, name, description, parent=None, value=None):
        """Initializing a Node object.
        The object has a name, description, parent, value, and a list of children nodes
        """
        self.name = name
        self.description = description
        self.parent = parent
        self.value = value
        self.children = []

    def add_child(self, child):
        """Function to add a child node to the current node.
        The function takes a child node as argument"""
        self.children.append(child)
