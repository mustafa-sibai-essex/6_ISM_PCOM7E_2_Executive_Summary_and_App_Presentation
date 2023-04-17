import tkinter as tk
from tkinter import ttk

class MainUI:
    def __init__(self, window):
        self.container = tk.Frame(window, pady=0, bg="black")
        self.container.pack(side="left", anchor="sw", fill="y")


        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_name_label = tk.Label(frame, text="Node Name:")
        self.node_name_label.pack(side="left", anchor="w", padx=10)
        self.node_name_entry = tk.Entry(frame)
        self.node_name_entry.pack(side="left", anchor="w", padx=16)


        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_parent_label = tk.Label(frame, text="Node Name2:")
        self.node_parent_label.pack(side="left", anchor="w", padx=10)
        self.node_parent_entry = tk.Entry(frame)
        self.node_parent_entry.pack(side="left", anchor="w", padx=10)


        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_type_label = tk.Label(frame, text="Node Type:")
        self.node_type_label.pack(side="left", anchor="w", padx=10)
        self.node_type_var = tk.StringVar(frame)
        self.node_type_var.set("Or") # Set default option
        self.node_type_dropdown = ttk.Combobox(frame, textvariable=self.node_type_var, values=["Or", "And"], width=17)
        self.node_type_dropdown.pack(side="left", anchor="w", padx=22)
        self.node_type_dropdown.config(state='readonly')


        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="w", pady=5)

        self.node_value_label = tk.Label(frame, text="Node Value:")
        self.node_value_label.pack(side="left", anchor="w", padx=10)
        self.node_value_entry = tk.Entry(frame)
        self.node_value_entry.pack(side="left", anchor="w", padx=16)


        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="w", pady=5)

        self.add_node_button = tk.Button(frame, text="Add Node", command=self.add_node, width=30)
        self.add_node_button.pack(side="left", anchor="w", padx=10)

    def add_node(self):
        node_name = self.node_name_entry.get()
        node_parent = self.node_parent_entry.get()
        node_type = self.node_type_var.get()
        node_value = self.node_value_entry.get()
        
        print("Node Name:", node_name)
        print("Node Parent:", node_parent)
        print("Node Type:", node_type)
        print("Node Value:", node_value)
