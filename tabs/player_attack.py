import tkinter as tk
from data import MONSTERS, STAT_LIST, ATTACK_TYPE_LIST


from .base import Tab


class PlayerAttackTab(Tab):
    def __init__(self, notebook):
        super().__init__(notebook)

    def initialize_inputs(self):
        self.inputs["monsters"] = {}
        for monster_name in MONSTERS:
            self.inputs["monsters"][monster_name] = tk.BooleanVar(value=False)
        self.inputs["stat"] = tk.StringVar(value=STAT_LIST[0])
        self.inputs["attack_type"] = tk.StringVar(value=ATTACK_TYPE_LIST[0])
        self.inputs["roll"] = tk.IntVar(value=0)
        self.inputs["damage"] = tk.IntVar(value=0)

    def process(self):
        monsters = []
        for name, selected in self.inputs["monsters"].items():
            if selected.get():
                monsters.append(name)
        attack_type = self.inputs["attack_type"].get().lower()
        roll = self.inputs["roll"].get()
        damage = self.inputs["damage"].get()
        stat_name = self.inputs["stat"].get().lower()
        monster_results = {}

        for name in monsters:
            monster_info = MONSTERS[name]
            stat = monster_info[stat_name]
            if roll > stat:
                armor = monster_info["arm"]
                if attack_type == "magical":
                    armor = monster_info["marm"]
                result = damage - armor
                if result < 0:
                    result = 1
                monster_results[name] = str(-result)

        result_string = ""
        for name, result in monster_results.items():
            result_string += f"{name}: {result}\n"
        result_string = result_string.strip()
        if not result_string:
            result_string = "Miss"
        self.result = result_string

    def draw_screen(self):
        self.draw_monster_options()
        self.draw_stat_options()
        self.draw_attack_options()
        self.draw_player_inputs()
        self.draw_execute_button(row=1, column=0, sticky=tk.NW, pady=10)
        self.draw_result()

    def draw_monster_options(self):
        monster_options_frame = tk.Frame(self.tab)
        monster_options_frame.grid(row=0, column=0, sticky=tk.NW)

        tk.Label(monster_options_frame, text="Monsters").grid(sticky=tk.NW)
        for monster_name in MONSTERS:
            tk.Checkbutton(
                monster_options_frame,
                text=monster_name,
                variable=self.inputs["monsters"][monster_name],
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

    def draw_attack_options(self):
        attack_options_frame = tk.Frame(self.tab)
        attack_options_frame.grid(row=0, column=2, sticky=tk.NW)

        tk.Label(attack_options_frame, text="Attack type").grid(sticky=tk.NW)
        for value in ATTACK_TYPE_LIST:
            tk.Radiobutton(
                attack_options_frame,
                text=value,
                value=value,
                variable=self.inputs["attack_type"],
            ).grid(sticky=tk.NW)

    def draw_player_inputs(self):
        player_inputs_frame = tk.Frame(self.tab)
        player_inputs_frame.grid(row=0, column=3, sticky=tk.NW)

        tk.Label(player_inputs_frame, text="Roll").grid(sticky=tk.NW)
        tk.Entry(player_inputs_frame, textvariable=self.inputs["roll"]).grid(
            sticky=tk.NW
        )

        tk.Label(player_inputs_frame, text="Damage").grid(sticky=tk.NW)
        tk.Entry(player_inputs_frame, textvariable=self.inputs["damage"]).grid(
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
