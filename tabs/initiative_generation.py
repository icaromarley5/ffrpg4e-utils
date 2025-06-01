import tkinter as tk
import random


from data import MONSTERS, PLAYERS
from .base import Tab


INITIATIVE_DIE = 10
PHASE_TOTAL = 10


class InitiativeGenerationTab(Tab):
    def __init__(self, notebook):
        super().__init__(notebook)

    def initialize_inputs(self):
        self.inputs["monsters"] = {}
        for monster_name in MONSTERS:
            self.inputs["monsters"][monster_name] = tk.IntVar(value=0)
        self.inputs["players"] = {}
        for player_name in PLAYERS:
            self.inputs["players"][player_name] = tk.BooleanVar(value=False)

    def find_actor_info_dict(self, actor_name):
        if "_" in actor_name:
            return MONSTERS[actor_name.split("_")[0]]
        else:
            for data_source in [MONSTERS, PLAYERS]:
                if actor_name in data_source:
                    return data_source[actor_name]

    def compute_order(self, actor_info_dict, actor, actor_list):
        ordered_actor_list = []
        actor_air_value = actor_info_dict["air"]
        last_position = len(actor_list) - 1
        inserted = False
        for index, existent_actor in enumerate(actor_list):
            if inserted:
                ordered_actor_list.append(existent_actor)
                continue
            if actor_air_value <= self.find_actor_info_dict(existent_actor)["air"]:
                ordered_actor_list.append(existent_actor)
                if index == last_position:
                    ordered_actor_list.append(actor)
                    inserted = True
            else:
                ordered_actor_list.append(actor)
                ordered_actor_list.append(existent_actor)
                inserted = True
        return ordered_actor_list

    def process(self):
        player_list = []
        for player_name, select_input in self.inputs["players"].items():
            if select_input.get():
                player_list.append(player_name)
        monster_list = []
        for monster_name, quantity_input in self.inputs["monsters"].items():
            quantity = quantity_input.get()
            if quantity == 1:
                monster_names = [f"{monster_name}"]
            else:
                monster_names = [
                    f"{monster_name}_{index+1}" for index in range(quantity)
                ]
            monster_list = monster_list + monster_names
        actor_list = player_list + monster_list
        random.shuffle(actor_list)

        phase_dict = {i: [] for i in range(1, 10 + 1)}
        for actor in actor_list:
            info_dict = self.find_actor_info_dict(actor)
            dice_list = []
            for _ in range(info_dict["init"]):
                dice_list.append(random.randrange(1, INITIATIVE_DIE + 1))
            for dice in dice_list:
                if not phase_dict[dice]:
                    phase_dict[dice].append(actor)
                else:
                    phase_dict[dice] = self.compute_order(
                        info_dict, actor, phase_dict[dice]
                    )
        phase_dict[5] = ["CENÁRIO"] + phase_dict[5]
        phase_dict[1] = ["CENÁRIO"] + phase_dict[1]
        result_string = ""
        for phase, phase_order in phase_dict.items():
            result_string += f"{phase}: {', '.join(phase_order)}\n"

        self.result = result_string.strip()

    def draw_screen(self):
        self.draw_player_options()
        self.draw_monster_options()
        self.draw_execute_button(row=1, column=0, sticky=tk.W, pady=10)
        self.draw_result()

    def draw_monster_options(self):
        monster_options_frame = tk.Frame(self.tab)
        monster_options_frame.grid(row=0, column=1, sticky=tk.NW)
        tk.Label(monster_options_frame, text="Monsters").grid(sticky=tk.NW)
        for index, monster_name in enumerate(MONSTERS):
            tk.Label(monster_options_frame, text=monster_name).grid(
                row=index + 1, column=0, sticky=tk.NW, pady=5
            )
            tk.Entry(
                monster_options_frame,
                textvariable=self.inputs["monsters"][monster_name],
            ).grid(row=index + 1, column=1, sticky=tk.NW, pady=5)

    def draw_player_options(self):
        player_options_frame = tk.Frame(self.tab)
        player_options_frame.grid(row=0, column=0, sticky=tk.NW)
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
