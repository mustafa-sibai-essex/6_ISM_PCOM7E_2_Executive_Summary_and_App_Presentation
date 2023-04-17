import tkinter as tk


class DeleteUI:
    def __init__(self, delete_ui_container):
        self.delete_ui_container = delete_ui_container

        frame = tk.Frame(self.delete_ui_container)
        frame.pack(side="top", anchor="e", pady=5)

        self.node_delete_label = tk.Label(frame, text="Node to Delete:")
        self.node_delete_label.pack(side="left", anchor="w", padx=0)
        self.node_delete_entry = tk.Entry(frame)
        self.node_delete_entry.pack(side="left", anchor="w", padx=16)

        frame = tk.Frame(self.delete_ui_container)
        frame.pack(side="top", anchor="w", pady=5)

        self.delete_node_button = tk.Button(
            frame, text="Delete Node", command=self.delete_node, width=30
        )
        self.delete_node_button.pack(side="left", anchor="w", padx=0)

    def delete_node(self):
        node_to_delete = self.node_delete_entry.get()

        print("Node to delete:", node_to_delete)
