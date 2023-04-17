import tkinter as tk
from calculateAttackValueUI import CalculateAttackValueUI
from deleteUI import DeleteUI
from graphFactory import GraphFactory
from menubar import MenuBar
from mainUI import MainUI

# Create a Tkinter window
window = tk.Tk()
window.title(
    "Information Security Management March 2023: Attack tree generator by Mustafa Sibai"
)
window.geometry("1280x720")

# Create frames to hold UI elements
graph_frame = tk.Frame(window, pady=0)
graph_frame.pack(side="top", anchor="n")

main_frame = tk.Frame(window, pady=0)
main_frame.pack(side="left", anchor="sw")

delete_frame = tk.Frame(window, pady=0)
delete_frame.pack(side="left", anchor="sw")

calculate_attack_value_frame = tk.Frame(window, pady=0)
calculate_attack_value_frame.pack(side="left", anchor="sw")

# Create instances of classes used in the UI
graph_factory = GraphFactory()

main_ui = MainUI(main_frame, graph_frame, graph_factory)
menu_bar = MenuBar(window, main_ui, graph_factory)
delete_ui = DeleteUI(delete_frame, main_ui, graph_factory.node_factory)
calculate_attack_value_ui = CalculateAttackValueUI(
    calculate_attack_value_frame, main_ui, graph_factory.node_factory
)

# Start the Tkinter event loop
window.mainloop()
