import tkinter as tk
from tkinter import filedialog
import os
from shutil import copy
import json
from graphFactory import GraphFactory
from node import Node
from nodeFactory import NodeFactory
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
        export_menu.add_command(label="XML", command=self.export_to_xml)
        export_menu.add_command(label="JSON", command=self.export_to_json)
        export_menu.add_command(label="PNG", command=self.export_to_png)
        export_menu.add_command(label="PDF", command=self.export_to_pdf)

    def add_about_menu(self):
        self.menu_bar.add_command(label="About", command=self.do_about)

    def read_xml_file(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        self.graph_factory.clear_graph()

        def create_nodes(node, parent_name=None):
            name = node.get("name")
            node_type = node.get("node_type")
            value = node.get("value")
            self.graph_factory.add_node(name, parent_name, node_type, value)

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
            node_type = data["node_type"]
            value = data["value"]
            self.graph_factory.add_node(name, parent_name, node_type, value)

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
        print("About")

    def export_to_xml(self):
        print("Exporting to XML")

    def export_to_json(self):
        print("Exporting to JSON")

    def export_to_png(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG", "*.png")]
        )
        if file_path:
            output_file = os.path.join(os.getcwd(), "./output", "graph.png")
            copy(output_file, file_path)

    def export_to_pdf(self):
        print("Exporting to PDF")
