class Node:
    def __init__(self, name, description, parent=None, value=None):
        self.name = name
        self.description = description
        self.parent = parent
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
