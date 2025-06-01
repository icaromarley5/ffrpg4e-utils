import tkinter as tk
import random


from data import LAWS
from .base import Tab


META_OPTIONS = list(LAWS.keys())


class LawsSelectionTab(Tab):
    def __init__(self, notebook):
        super().__init__(notebook)

    def initialize_inputs(self):
        pass

    def process(self):
        result_string = ""
        for tag_name in ["Proibido", "Recomendado"]:
            meta_option = random.choice(META_OPTIONS)
            option = random.choice(LAWS[meta_option])
            result_string += f"{tag_name}: {meta_option} -> {option}\n"
        self.result = result_string.strip()

    def draw_screen(self):
        self.draw_execute_button(row=0, column=0, sticky=tk.W, pady=10)
        self.draw_result()

    def draw_result(self):
        result_frame = tk.Frame(self.tab)
        result_frame.grid(row=1, column=0, columnspan=100, sticky=tk.NW)
        tk.Label(result_frame, text="Result").grid(sticky=tk.NW)
        self.result_field = tk.Text(result_frame, height=10)
        self.result_field.config(font=("Courier", 14))
        self.result_field["state"] = "disabled"
        self.result_field.grid(sticky=tk.NW, row=2, column=0)
