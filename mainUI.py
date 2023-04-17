import tkinter as tk


class MainUI:
    """This code defines a GUI for an attack tree generator application.
    It creates various labels, entries and buttons for user input,
    and displays an attack tree graph in response to the user's input."""

    def __init__(self, main_ui_container, graph_container, graph_factory):
        """Initialize MainUI class with main window container, graph container and graph factory parameters"""

        # Save main window container, graph container and graph factory as attributes of the MainUI instance
        self.main_ui_container = main_ui_container
        self.graph_container = graph_container
        self.graph_factory = graph_factory

        # Create a frame and pack it to the top of the main window container with a 5 pixel vertical padding
        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a label and an entry for node name, pack them to the left of the frame with a 10 pixel horizontal padding
        self.node_name_label = tk.Label(frame, text="Node Name:")
        self.node_name_label.pack(side="left", anchor="w", padx=10)
        self.node_name_entry = tk.Entry(frame)
        self.node_name_entry.pack(side="left", anchor="w", padx=16)

        # Create a frame and pack it to the top of the main window container with a 5 pixel vertical padding
        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a label and an entry for node description, pack them to the left of the frame with a 10 pixel horizontal padding
        self.node_description_label = tk.Label(frame, text="Node Description:")
        self.node_description_label.pack(side="left", anchor="w", padx=10)
        self.node_description_entry = tk.Entry(frame)
        self.node_description_entry.pack(side="left", anchor="w", padx=16)

        # Create a frame and pack it to the top of the main window container with a 5 pixel vertical padding
        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a label and an entry for node parent, pack them to the left of the frame with a 10 pixel horizontal padding
        self.node_parent_label = tk.Label(frame, text="Node Parent:")
        self.node_parent_label.pack(side="left", anchor="w", padx=10)
        self.node_parent_entry = tk.Entry(frame)
        self.node_parent_entry.pack(side="left", anchor="w", padx=10)

        # Create a frame and pack it to the top of the main window container with a 5 pixel vertical padding
        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a label and an entry for node value, pack them to the left of the frame with a 10 pixel horizontal padding
        self.node_value_label = tk.Label(frame, text="Node Value:")
        self.node_value_label.pack(side="left", anchor="w", padx=10)
        self.node_value_entry = tk.Entry(frame)
        self.node_value_entry.pack(side="left", anchor="w", padx=16)

        # Create a frame and pack it to the top of the main window container with a 5 pixel vertical padding
        frame = tk.Frame(self.main_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        # Create a button for adding a node, pack it to the left of the frame
        self.add_node_button = tk.Button(
            frame, text="Add Node", command=self.add_node, width=30
        )
        self.add_node_button.pack(side="left", anchor="w", padx=10)

    def add_node(self):
        """This method adds a new node to the graph"""

        # Get the values of the node attributes from the GUI entries
        node_name = self.node_name_entry.get()
        node_description = self.node_description_entry.get()
        node_parent = self.node_parent_entry.get()
        node_value = self.node_value_entry.get()

        # Create a new node using the GraphFactory and the values of the attributes
        node = self.graph_factory.add_node(
            node_name, node_description, node_parent, node_value
        )

        # If the node was created successfully, clear the GUI entries and update the graph display
        if node:
            self.node_name_entry.delete(0, tk.END)
            self.node_description_entry.delete(0, tk.END)
            self.node_parent_entry.delete(0, tk.END)
            self.node_value_entry.delete(0, tk.END)
            self.display_nodes()

    def display_nodes(self, node_names=set()):
        """This method displays the graph and take in node_names as an input.
        node_names are nodes the player wants to calculate the attack value for."""

        # Create the graph using the GraphFactory and the given node names
        self.graph_factory.create_graph(node_names)

        # Destroy the old graph view (if any) and create a new one with the updated graph image
        if hasattr(self, "graph_view"):
            self.graph_view.destroy()

        self.graph_view = tk.Label(self.graph_container)
        self.graph_view.pack(side="top", anchor="w", pady=5)
        self.graph_view.img = tk.PhotoImage(file="./output/graph.png")
        self.graph_view.config(image=self.graph_view.img)
