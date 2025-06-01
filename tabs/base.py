import tkinter as tk
from tkinter import ttk
import re


class Tab:
    def __init__(self, notebook):
        self.notebook = notebook

        self.tab = ttk.Frame(notebook)
        tab_name = self.__class__.__name__.replace("Tab", "")
        formatted_tab_name = re.sub("(?!^)([A-Z])", " \\1", tab_name)
        self.notebook.add(self.tab, text=formatted_tab_name)

        self.inputs = {}
        self.result = None
        self.result_field = None

        self.initialize_inputs()
        self.draw_screen()

    def draw_execute_button(self, *args, **kwargs):
        tk.Button(self.tab, text="Execute", command=lambda: self.execute()).grid(
            *args, **kwargs
        )

    def execute(self):
        self.process()
        self.fill_result()

    def fill_result(self):
        self.result_field["state"] = "normal"
        self.result_field.replace("1.0", tk.END, str(self.result))
        self.result_field["state"] = "disabled"

    def initialize_inputs(self):
        pass

    def process(self):
        pass

    def draw_screen(self):
        pass
