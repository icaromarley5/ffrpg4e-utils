import tkinter as tk
from tkinter import ttk

from tabs import TABS_LIST


root = tk.Tk()
root.title("FFRPG 4.0 Utils")
notebook = ttk.Notebook(root)

for tab_class in TABS_LIST:
    tab_class(notebook)

notebook.pack()
root.mainloop()
