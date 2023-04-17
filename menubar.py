import tkinter as tk
from tkinter import filedialog
import os
from shutil import copy


class MenuBar:
    def __init__(self, window):
        self.menu_bar = tk.Menu(window)
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

    def import_from_file(self):
        print("Import From File")

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
