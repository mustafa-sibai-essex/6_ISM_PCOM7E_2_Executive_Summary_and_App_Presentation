import tkinter as tk
from deleteUI import DeleteUI
from menubar import MenuBar
from mainUI import MainUI

root = tk.Tk()
root.geometry("1280x720")

main_frame  = tk.Frame(root)
main_frame.pack(side="left", anchor="sw")

delete_frame = tk.Frame(root)
delete_frame.pack(side="left", anchor="sw")

menu_bar = MenuBar(root)
main_ui = MainUI(main_frame)
delete_ui = DeleteUI(delete_frame)

root.config(menu=menu_bar.menu_bar)

root.mainloop()
