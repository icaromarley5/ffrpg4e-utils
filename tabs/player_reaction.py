import tkinter as tk

from data import MONSTERS, STAT_LIST
from .base import Tab


class PlayerReactionTab(Tab):
    def __init__(self, notebook):
        self.first_monster = next(iter(MONSTERS.keys()), None)
        super().__init__(notebook)

    def initialize_inputs(self):
        self.inputs["monster"] = tk.StringVar(value=self.first_monster)
        self.inputs["stat"] = tk.StringVar(value=STAT_LIST[0])
        self.inputs["roll"] = tk.IntVar(value=0)

    def process(self):
        monster_info = MONSTERS[self.inputs["monster"].get()]
        roll = self.inputs["roll"].get()
        stat_name = self.inputs["stat"].get().lower()

        stat = monster_info[stat_name]
        result = "Failed"
        if roll > stat:
            result = "Success"
        self.result = result

    def draw_screen(self):
        self.draw_monster_options()
        self.draw_stat_options()
        self.draw_player_inputs()
        self.draw_execute_button(row=1, column=0, sticky=tk.NW, pady=10)
        self.draw_result()

    def draw_monster_options(self):
        monster_options_frame = tk.Frame(self.tab)
        monster_options_frame.grid(row=0, column=0, sticky=tk.NW)

        tk.Label(monster_options_frame, text="Monster").grid(sticky=tk.NW)
        for value in MONSTERS:
            tk.Radiobutton(
                monster_options_frame,
                text=value,
                value=value,
                variable=self.inputs["monster"],
            ).grid(sticky=tk.NW)

    def draw_stat_options(self):
        stat_options_frame = tk.Frame(self.tab)
        stat_options_frame.grid(row=0, column=1, sticky=tk.NW)

        tk.Label(stat_options_frame, text="Stat").grid(sticky=tk.NW)
        for value in STAT_LIST:
            tk.Radiobutton(
                stat_options_frame,
                text=value,
                value=value,
                variable=self.inputs["stat"],
            ).grid(sticky=tk.NW)

    def draw_player_inputs(self):
        player_inputs_frame = tk.Frame(self.tab)
        player_inputs_frame.grid(row=0, column=3, sticky=tk.NW)

        tk.Label(player_inputs_frame, text="Roll").grid(sticky=tk.NW)
        tk.Entry(player_inputs_frame, textvariable=self.inputs["roll"]).grid(
            sticky=tk.NW
        )

    def draw_result(self):
        result_frame = tk.Frame(self.tab)
        result_frame.grid(row=3, column=0, columnspan=100, sticky=tk.NW)

        tk.Label(result_frame, text="Result").grid(sticky=tk.NW)
        self.result_field = tk.Text(result_frame, height=10)
        self.result_field.config(font=("Courier", 14))
        self.result_field["state"] = "disabled"
        self.result_field.grid(sticky=tk.NW)
