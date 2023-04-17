import tkinter as tk
from tkinter import filedialog
from shutil import copy
import os
import json
from tkinter import messagebox
import xml.etree.ElementTree as ET


class MenuBar:
    def __init__(self, window, main_ui, graph_factory):
        self.menu_bar = tk.Menu(window)
        self.main_ui = main_ui
        self.graph_factory = graph_factory

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.add_file_menu()
        self.add_about_menu()

        window.config(menu=self.menu_bar)

    def add_file_menu(self):
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(
            label="Import From File", command=self.import_from_file
        )
        export_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Export As", menu=export_menu)
        export_menu.add_command(label="PNG", command=self.export_to_png)

    def add_about_menu(self):
        self.menu_bar.add_command(label="About", command=self.do_about)

    def read_xml_file(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        self.graph_factory.clear_graph()

        def create_nodes(node, parent_name=None):
            name = node.get("name")
            description = node.get("description")
            value = node.get("value")
            self.graph_factory.add_node(name, description, parent_name, value)

            for child_node in node:
                create_nodes(child_node, name)

        create_nodes(root)
        self.main_ui.display_nodes()

    def read_json_file(self, file_path):
        with open(file_path) as f:
            data = json.load(f)

        self.graph_factory.clear_graph()

        def create_nodes(data, parent_name=None):
            name = data["name"]
            description = data["description"]
            value = data["value"]
            self.graph_factory.add_node(name, description, parent_name, value)

            for child_data in data["children"]:
                create_nodes(child_data, name)

        create_nodes(data)
        self.main_ui.display_nodes()

    def import_from_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("XML files", "*.xml"), ("JSON files", "*.json")]
        )
        if not file_path:
            return

        if file_path.endswith(".json"):
            self.read_json_file(file_path)
        elif file_path.endswith(".xml"):
            self.read_xml_file(file_path)
        else:
            print("Unsupported file type")

    def do_about(self):
        messagebox.showinfo(
            "Information Security Management March 2023",
            "Attack tree generator application created by Mustafa Sibai",
        )

    def export_to_png(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG", "*.png")]
        )
        if file_path:
            output_file = os.path.join(os.getcwd(), "./output", "graph.png")
            copy(output_file, file_path)
