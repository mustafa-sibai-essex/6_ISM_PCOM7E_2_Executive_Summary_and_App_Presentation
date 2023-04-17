from node import Node


class NodeFactory:
    def __init__(self):
        self.nodes = {}

    def create_node(self, name, parent_name=None, node_type="Or", value=None):
        if parent_name and parent_name not in self.nodes:
            print(f"Error: Parent node '{parent_name}' not found.")
            return None

        if name in self.nodes:
            print(f"Error: Node '{name}' already exists.")
            return None

        node = Node(name, parent_name, node_type, value)
        self.nodes[name] = node

        if parent_name:
            parent_node = self.nodes[parent_name]
            parent_node.add_child(node)

        return node

    def delete_node(self, name):
        if name not in self.nodes:
            print(f"Error: Node '{name}' not found.")
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
        return list(self.nodes.values())
