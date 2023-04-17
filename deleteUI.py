import tkinter as tk

class DeleteUI:
    def __init__(self, window):
        self.container = tk.Frame(window, pady=0, bg="red")
        self.container.pack(side="top", anchor="w")
    

        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="e", pady=5)

        self.node_delete_label = tk.Label(frame, text="Node to Delete:")
        self.node_delete_label.pack(side="left", anchor="w", padx=0)
        self.node_delete_entry = tk.Entry(frame)
        self.node_delete_entry.pack(side="left", anchor="w", padx=16)


        frame = tk.Frame(self.container)
        frame.pack(side="top", anchor="w", pady=5)

        self.delete_node_button = tk.Button(frame, text="Delete Node", command=self.delete_node, width=30)
        self.delete_node_button.pack(side="left", anchor="w", padx=0)

    def delete_node(self):
        node_to_delete = self.node_delete_entry.get()

        print("Node to delete:", node_to_delete)
