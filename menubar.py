import tkinter as tk
from tkinter import filedialog
from shutil import copy
import os
import json
from tkinter import messagebox
import xml.etree.ElementTree as ET


class MenuBar:
    """Creates the menu bar at the top of the window"""

    def __init__(self, window, main_ui, graph_factory):
        """Initialize MenuBar"""

        self.menu_bar = tk.Menu(window)
        self.main_ui = main_ui
        self.graph_factory = graph_factory

        # Create two menus, file and about
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Add the created menus to the menu bar
        self.add_file_menu()
        self.add_about_menu()

        # Set the window's menu to the created menu bar
        window.config(menu=self.menu_bar)

    def add_file_menu(self):
        """Define function to add file menu to the menu bar"""

        # Create file menu
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add import from file option to the file menu
        self.file_menu.add_command(
            label="Import From File", command=self.import_from_file
        )

        # Add export as option to the file menu
        export_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Export As", menu=export_menu)
        export_menu.add_command(label="PNG", command=self.export_to_png)

    def add_about_menu(self):
        """Define function to add about menu to the menu bar"""
        self.menu_bar.add_command(label="About", command=self.do_about)

    def read_xml_file(self, file_path):
        """Define function to read XML file and create nodes"""

        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Clear the graph
        self.graph_factory.clear_graph()

        def create_nodes(node, parent_name=None):
            """Create nodes recursively"""

            name = node.get("name")
            description = node.get("description")
            value = node.get("value")
            self.graph_factory.add_node(name, description, parent_name, value)

            for child_node in node:
                create_nodes(child_node, name)

        create_nodes(root)

        # Display the nodes in the main UI
        self.main_ui.display_nodes()

    def read_json_file(self, file_path):
        """Define function to read JSON file and create nodes"""

        # Read the JSON file
        with open(file_path) as f:
            data = json.load(f)

        # Clear the graph
        self.graph_factory.clear_graph()

        # Create nodes recursively
        def create_nodes(data, parent_name=None):
            name = data["name"]
            description = data["description"]
            value = data["value"]
            self.graph_factory.add_node(name, description, parent_name, value)

            for child_data in data["children"]:
                create_nodes(child_data, name)

        create_nodes(data)

        # Display the nodes in the main UI
        self.main_ui.display_nodes()

    def import_from_file(self):
        """Define function to import nodes from file"""

        # Open file dialog to select a file to import from
        file_path = filedialog.askopenfilename(
            filetypes=[("XML files", "*.xml"), ("JSON files", "*.json")]
        )
        if not file_path:
            return

        # Check the file type and read the file
        if file_path.endswith(".json"):
            self.read_json_file(file_path)
        elif file_path.endswith(".xml"):
            self.read_xml_file(file_path)
        else:
            print("Unsupported file type")

    def do_about(self):
        """This method displays the "About" information for the application"""

        messagebox.showinfo(
            "Information Security Management March 2023",
            "Attack tree generator application created by Mustafa Sibai",
        )

    def export_to_png(self):
        """This method exports the graph to a PNG file"""

        # Display a file dialog to allow the user to select a file path and name for the PNG file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG", "*.png")]
        )

        # If a file path was selected
        if file_path:
            # Set the output file path to the "./output/graph.png" file
            output_file = os.path.join(os.getcwd(), "./output", "graph.png")

            # Copy the output file to the selected file path
            copy(output_file, file_path)
