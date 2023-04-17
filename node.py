import tkinter as tk
from tkinter import ttk
from graphviz import Digraph


class Node:
    def __init__(self, name, parent=None, node_type="Or", value=None):
        self.name = name
        self.parent = parent
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
