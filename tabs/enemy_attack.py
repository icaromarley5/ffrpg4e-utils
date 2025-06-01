import tkinter as tk
import random


from data import MONSTERS, PLAYERS
from .base import Tab


EXTRA_DIFFICULTY_LIST = [-20, 0, 40]
CRIT_VALUES = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]


class EnemyAttackTab(Tab):
    def __init__(self, notebook):
        self.first_monster = next(iter(MONSTERS.keys()), None)
        super().__init__(notebook)

    def initialize_inputs(self):
        self.inputs["monster"] = tk.StringVar(value=self.first_monster)
        self.inputs["players"] = {}
        for player_name in PLAYERS:
            self.inputs["players"][player_name] = tk.BooleanVar(value=False)
        self.inputs["extra difficulty"] = tk.IntVar(value=0)
        self.inputs["attack"] = tk.StringVar(value=None)

    def process(self):
        monster_info = MONSTERS[self.inputs["monster"].get()]
        attack = monster_info["attacks"][self.inputs["attack"].get()]
        result_string = f"Element: {attack['element']} Type: {attack['type']} "
        extra_difficulty = self.inputs["extra difficulty"].get()
        player_list = []
        for player_name, select_input in self.inputs["players"].items():
            if select_input.get():
                player_list.append(player_name)
        offensive_stat = monster_info[attack["offensive stat"]]
        difficulty = monster_info["attack_difficulty"]

        roll = random.randint(1, 100)
        result_string += f"Roll: {roll} "
        total_roll = roll + offensive_stat - (difficulty + extra_difficulty)

        damage = monster_info["dmg_" + attack["offensive stat"]]
        if roll in CRIT_VALUES:
            damage *= 2
            result_string += "(critical) "
        extra_damage = roll // 10
        if extra_damage == 0:
            extra_damage = 1
        damage += extra_damage

        for tag in ["buff", "debuff"]:
            if tag in attack:
                if roll > attack[tag]["difficulty"]:
                    result_string += f"{tag}: {attack[tag]['name']} "

        result_string += "\n"
        results = {}
        for player_name in player_list:
            player_info = PLAYERS[player_name]
            defensive_stat = player_info[attack["defensive stat"]]
            if total_roll > defensive_stat:
                armor = player_info["arm"]
                if attack["type"] == "magical":
                    armor = player_info["marm"]
                result = damage - armor
                if result < 0:
                    result = 1
                results[player_name] = result
        for name, result in results.items():
            result_string += f"{name}: {-result}\n"
        self.result = result_string.strip()

    def draw_screen(self):
        self.draw_monster_options()
        self.draw_difficulty_options()
        self.draw_player_options()
        self.draw_execute_button(row=2, column=0, sticky=tk.W, pady=10)
        self.draw_result()

    def fill_attack_options(self, monster_name, attack_frame):
        for index, widget in enumerate(attack_frame.winfo_children()):
            if index == 0:
                continue
            widget.destroy()
        monster = MONSTERS[monster_name]

        self.inputs["attack"].set(next(iter(monster["attacks"].keys())))
        for attack_name, attack_info in monster["attacks"].items():
            tk.Radiobutton(
                attack_frame,
                text=attack_name + f" ({self.format_attack_info(attack_info)})",
                value=attack_name,
                variable=self.inputs["attack"],
            ).grid(sticky=tk.NW)

    def format_attack_info(self, info):
        formatted_info = (
            f"roll: {info['offensive stat']} vs {info['defensive stat']}, "
            f"{info['type']}/{info['element']}, range: {info['range']}, "
            f"extra difficulty: {info['extra difficulty']} slow: {info['slow']} "
            f"mana: {info['mp']}"
        )
        for tag in ["buff", "debuff"]:
            if tag in info:
                formatted_info += (
                    f", {tag}: {info[tag]['name']} {info[tag]['difficulty']}"
                )
        return formatted_info

    def draw_monster_options(self):
        attack_options_frame = tk.Frame(self.tab)
        monster_options_frame = tk.Frame(self.tab)
        monster_options_frame.grid(row=0, column=0, columnspan=20, sticky=tk.NW)
        tk.Label(monster_options_frame, text="Monster").grid(sticky=tk.NW)
        for monster_name in MONSTERS:
            tk.Radiobutton(
                monster_options_frame,
                text=monster_name,
                value=monster_name,
                variable=self.inputs["monster"],
                command=lambda name=monster_name: self.fill_attack_options(
                    name, attack_options_frame
                ),
            ).grid(sticky=tk.NW)

        attack_options_frame.grid(row=0, column=1, sticky=tk.NW)
        tk.Label(attack_options_frame, text="Attack").grid(sticky=tk.NW)
        self.fill_attack_options(self.first_monster, attack_options_frame)

    def draw_difficulty_options(self):
        difficulty_options_frame = tk.Frame(self.tab)
        difficulty_options_frame.grid(row=1, column=0, sticky=tk.NW)
        tk.Label(difficulty_options_frame, text="Extra difficulty").grid(sticky=tk.NW)
        for value in EXTRA_DIFFICULTY_LIST:
            tk.Radiobutton(
                difficulty_options_frame,
                text=value,
                value=value,
                variable=self.inputs["extra difficulty"],
            ).grid(sticky=tk.NW)

    def draw_player_options(self):
        player_options_frame = tk.Frame(self.tab)
        player_options_frame.grid(row=1, column=1, sticky=tk.NW)
        tk.Label(player_options_frame, text="Players").grid(sticky=tk.NW)
        for player_name in PLAYERS:
            tk.Checkbutton(
                player_options_frame,
                text=player_name,
                variable=self.inputs["players"][player_name],
            ).grid(sticky=tk.NW)

    def draw_result(self):
        result_frame = tk.Frame(self.tab)
        result_frame.grid(row=3, column=0, columnspan=100, sticky=tk.NW)
        tk.Label(result_frame, text="Result").grid(sticky=tk.NW)
        self.result_field = tk.Text(result_frame, height=10)
        self.result_field.config(font=("Courier", 14))
        self.result_field["state"] = "disabled"
        self.result_field.grid(sticky=tk.NW, row=2, column=0)
