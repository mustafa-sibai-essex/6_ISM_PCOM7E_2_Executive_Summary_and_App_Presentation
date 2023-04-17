import tkinter as tk
from deleteUI import DeleteUI
from menubar import MenuBar
from mainUI import MainUI

window = tk.Tk()
window.geometry("1280x720")


graph_frame = tk.Frame(window, pady=0)
graph_frame.pack(side="top", anchor="n")

main_frame = tk.Frame(window, pady=0)
main_frame.pack(side="left", anchor="sw")

delete_frame = tk.Frame(window, pady=0)
delete_frame.pack(side="left", anchor="sw")


menu_bar = MenuBar(window)
main_ui = MainUI(main_frame, graph_frame)
delete_ui = DeleteUI(delete_frame, main_ui)

window.mainloop()
