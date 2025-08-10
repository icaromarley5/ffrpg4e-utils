import tkinter as tk


from .base import Tab
from data import STAT_LIST, ELEMENT_LIST, ATTACK_TYPE_LIST


MONSTER_IMPORTANCE_STAT_DICT = {
    "horde": {
        "init": 1,
        "attack_difficulty": 60,
        "level": -4,
        "hp_multiplier": 0.2,
        "mp_multiplier": 0.4,
        "dmg_multiplier_multiplier": 1,
    },
    "minion": {
        "init": 2,
        "attack_difficulty": 50,
        "level": -2,
        "hp_multiplier": 0.4,
        "mp_multiplier": 0.6,
        "dmg_multiplier_multiplier": 1,
    },
    "common": {
        "init": 3,
        "attack_difficulty": 40,
        "level": 0,
        "hp_multiplier": 0.8,
        "mp_multiplier": 1,
        "dmg_multiplier_multiplier": 1,
    },
    "elite": {
        "init": 4,
        "attack_difficulty": 30,
        "level": 0,
        "hp_multiplier": 3,
        "mp_multiplier": 2,
        "dmg_multiplier_multiplier": 1,
    },
    "boss": {
        "init": 5,
        "attack_difficulty": 20,
        "level": 0,
        "hp_multiplier": 6,
        "mp_multiplier": 3,
        "dmg_multiplier_multiplier": 1.2,
    },
}
MONSTER_TYPE_STAT_DICT = {
    "brute": {
        "stats": ["earth", "air", "water", "fire"],
        "arm_multiplier": 0.8,
        "marm_multiplier": 0.2,
        "final_hp_multiplier": 1,
        "final_mp_multiplier": 0.5,
    },
    "quick": {
        "stats": ["air", "earth", "water", "fire"],
        "arm_multiplier": 0.2,
        "marm_multiplier": 0.2,
        "final_hp_multiplier": 0.6,
        "final_mp_multiplier": 0.6,
    },
    "caster": {
        "stats": ["fire", "water", "air", "earth"],
        "arm_multiplier": 0.2,
        "marm_multiplier": 0.8,
        "final_hp_multiplier": 0.5,
        "final_mp_multiplier": 1,
    },
}

BASE_ATTRIBUTES = [stat.lower() for stat in STAT_LIST]
SECONDARY_ATTRIBUTES = ["hp", "mp", "arm", "marm", "dmg_multiplier"]
LEVEL_ATTRIBUTES = {
    10: {
        "hp": [32, 64],
        "mp": [10, 50],
        "arm": [2, 12],
        "marm": [2, 12],
        "dmg_multiplier": [2, 4],
    },
    19: {
        "hp": [80, 148],
        "mp": [16, 64],
        "arm": [4, 24],
        "marm": [4, 24],
        "dmg_multiplier": [3, 7],
    },
    27: {
        "hp": [216, 288],
        "mp": [24, 148],
        "arm": [13, 48],
        "marm": [13, 48],
        "dmg_multiplier": [5, 9],
    },
    36: {
        "hp": [388, 468],
        "mp": [62, 288],
        "arm": [24, 84],
        "marm": [24, 84],
        "dmg_multiplier": [8, 12],
    },
    45: {
        "hp": [604, 704],
        "mp": [80, 468],
        "arm": [37, 120],
        "marm": [37, 120],
        "dmg_multiplier": [10, 14],
    },
    54: {
        "hp": [892, 1000],
        "mp": [100, 704],
        "arm": [62, 184],
        "marm": [62, 184],
        "dmg_multiplier": [13, 17],
    },
    63: {
        "hp": [1208, 1332],
        "mp": [150, 1000],
        "arm": [75, 245],
        "marm": [75, 245],
        "dmg_multiplier": [14, 20],
    },
    74: {
        "hp": [1984, 2260],
        "mp": [250, 1332],
        "arm": [123, 368],
        "marm": [123, 368],
        "dmg_multiplier": [16, 24],
    },
    84: {
        "hp": [2320, 2484],
        "mp": [400, 2260],
        "arm": [144, 452],
        "marm": [144, 452],
        "dmg_multiplier": [18, 26],
    },
    100: {
        "hp": [2544, 2820],
        "mp": [500, 2484],
        "arm": [158, 555],
        "marm": [158, 555],
        "dmg_multiplier": [20, 35],
    },
}

DAMAGE_RESISTANCE_LIST = [
    "Weak",
    "Normal",
    "Resist",
    "Immune",
    "Absorb",
]


class EnemyCreationTab(Tab):
    def __init__(self, notebook):
        super().__init__(notebook)

    def initialize_inputs(self):
        self.inputs["name"] = tk.StringVar(value="")
        self.inputs["level"] = tk.IntVar(value=0)
        self.inputs["class"] = tk.StringVar(
            value=next(iter(MONSTER_TYPE_STAT_DICT.keys()))
        )
        self.inputs["importance"] = tk.StringVar(
            value=next(iter(MONSTER_IMPORTANCE_STAT_DICT.keys()))
        )
        self.inputs["elements"] = {}
        for element in ELEMENT_LIST:
            self.inputs["elements"][element] = tk.StringVar(value="Normal")

    def compute_level(self, base_level, importance):
        monster_level = base_level + MONSTER_IMPORTANCE_STAT_DICT[importance]["level"]
        if monster_level < 1:
            monster_level = 1
        if monster_level > 100:
            monster_level = 100
        return monster_level

    def compute_base_stats(self, monster_level, monster_type):
        base_stat_points = monster_level // 4
        left_over = monster_level % 4
        imbalance_modifier = base_stat_points // 10
        if imbalance_modifier == 0:
            imbalance_modifier = 1
        monster_stats = {}
        for index in range(4):
            stat = MONSTER_TYPE_STAT_DICT[monster_type]["stats"][index]
            if index < 2:
                modifier = imbalance_modifier
            else:
                modifier = -imbalance_modifier
            monster_stats[stat] = base_stat_points + modifier
            if left_over > 0:
                monster_stats[stat] += 1
                left_over -= 1

            monster_stats[stat] *= 10

        return monster_stats

    def compute_level_attribute_info(self, attribute, monster_level):
        max_level = min_level = 0
        for level_bracket in LEVEL_ATTRIBUTES:
            if monster_level < level_bracket:
                max_level = level_bracket
                break
            min_level = level_bracket

        return min_level, max_level, LEVEL_ATTRIBUTES[max_level][attribute]

    def compute_attribute_value(self, attribute, monster_level):
        (
            min_level,
            max_level,
            (min_value, max_value),
        ) = self.compute_level_attribute_info(attribute, monster_level)
        difference = max_value - min_value
        base_max_level = max_level - 1 - min_level
        base_min_level = monster_level - min_level
        percentual = base_min_level / base_max_level

        return min_value + int(difference * percentual)

    def compute_attributes(self, level, _class, importance):
        attribute_dict = {}
        for attribute in SECONDARY_ATTRIBUTES:
            value = self.compute_attribute_value(attribute, level)
            if attribute in ["hp", "mp", "dmg_multiplier"]:
                value *= MONSTER_IMPORTANCE_STAT_DICT[importance][
                    f"{attribute}_multiplier"
                ]
                if attribute in ["hp", "mp"]:
                    value *= MONSTER_TYPE_STAT_DICT[_class][
                        f"final_{attribute}_multiplier"
                    ]
            if attribute in ["arm", "marm"]:
                value *= MONSTER_TYPE_STAT_DICT[_class][f"{attribute}_multiplier"]
            attribute_dict[attribute] = int(value)

        attribute_dict["init"] = MONSTER_IMPORTANCE_STAT_DICT[importance]["init"]
        attribute_dict["attack_difficulty"] = MONSTER_IMPORTANCE_STAT_DICT[importance][
            "attack_difficulty"
        ]

        return attribute_dict

    def compute_damage(self, stats_dict):
        multiplier = stats_dict["dmg_multiplier"]
        damage_dict = {}
        for attribute in BASE_ATTRIBUTES:
            damage_dict["dmg_" + attribute] = int(
                multiplier * stats_dict[attribute] / 10
            )

        return damage_dict

    def process(self):
        name = self.inputs["name"].get()
        level = self.inputs["level"].get()
        _class = self.inputs["class"].get()
        importance = self.inputs["importance"].get()

        result = {
            "level": level,
            "class": _class,
            "importance": importance,
        }

        result["elements"] = []
        for element, selected in self.inputs["elements"].items():
            resistance = selected.get().lower()
            if resistance != "normal":
                result["elements"].append({element.lower(): resistance})

        true_level = self.compute_level(level, importance)
        result.update(self.compute_base_stats(true_level, _class))
        result.update(self.compute_attributes(true_level, _class, importance))
        result.update(self.compute_damage(result))
        result.update({"attacks": {}})

        self.result = f"'{name}': {result}".strip()

    def draw_screen(self):
        self.draw_base_options()
        self.draw_class_options()
        self.draw_element_resistances()
        self.draw_execute_button(row=3, column=0, sticky=tk.NW, pady=10)
        self.draw_result()

    def draw_base_options(self):
        frame = tk.Frame(self.tab)
        frame.grid(row=0, column=0, sticky=tk.NW)

        tk.Label(frame, text="Name").grid(sticky=tk.NW)
        tk.Entry(frame, textvariable=self.inputs["name"]).grid(sticky=tk.NW)
        tk.Label(frame, text="Level").grid(sticky=tk.NW)
        tk.Entry(frame, textvariable=self.inputs["level"]).grid(sticky=tk.NW)

    def draw_class_options(self):
        class_frame = tk.Frame(self.tab)
        class_frame.grid(row=1, column=0, sticky=tk.NW)
        tk.Label(class_frame, text="Class").grid(sticky=tk.NW)
        for value in MONSTER_TYPE_STAT_DICT:
            tk.Radiobutton(
                class_frame,
                text=value,
                value=value,
                variable=self.inputs["class"],
            ).grid(sticky=tk.NW)

        importance_frame = tk.Frame(self.tab)
        importance_frame.grid(row=0, column=1, rowspan=3, sticky=tk.NW)
        tk.Label(importance_frame, text="Importance").grid(sticky=tk.NW)
        for value in MONSTER_IMPORTANCE_STAT_DICT:
            tk.Radiobutton(
                importance_frame,
                text=value,
                value=value,
                variable=self.inputs["importance"],
            ).grid(sticky=tk.NW)

    def draw_element_resistances(self):
        class_frame = tk.Frame(self.tab)
        class_frame.grid(row=2, column=0, columnspan=3, sticky=tk.NW)

        for index, value in enumerate(DAMAGE_RESISTANCE_LIST):
            tk.Label(class_frame, text=value).grid(
                row=index + 1, column=0, sticky=tk.NW
            )

        for column_index, element in enumerate(ELEMENT_LIST):
            tk.Label(class_frame, text=element).grid(
                row=0, column=column_index + 1, sticky=tk.NW
            )
            for row_index, value in enumerate(DAMAGE_RESISTANCE_LIST):
                tk.Radiobutton(
                    class_frame,
                    value=value,
                    variable=self.inputs["elements"][element],
                ).grid(row=row_index + 1, column=column_index + 1, sticky=tk.NW)

    def draw_result(self):
        frame = tk.Frame(self.tab)
        frame.grid(row=4, column=0, columnspan=100, sticky=tk.NW)

        tk.Label(frame, text="Result").grid(sticky=tk.NW)
        self.result_field = tk.Text(frame, height=10)
        self.result_field.config(font=("Courier", 14))
        self.result_field["state"] = "disabled"
        self.result_field.grid(sticky=tk.NW)


class EnemyAttackCreationTab(Tab):
    def __init__(self, notebook):
        super().__init__(notebook)

    def initialize_inputs(self):
        self.inputs["name"] = tk.StringVar(value="")
        first_stat = BASE_ATTRIBUTES[0]
        self.inputs["offensive stat"] = tk.StringVar(value=first_stat)
        self.inputs["defensive stat"] = tk.StringVar(value=first_stat)
        self.inputs["type"] = tk.StringVar(value=ATTACK_TYPE_LIST[0].lower())
        self.inputs["range"] = tk.IntVar(value=1)
        self.inputs["extra difficulty"] = tk.IntVar(value=0)
        self.inputs["element"] = tk.StringVar(value=ELEMENT_LIST[0].lower())
        self.inputs["slow"] = tk.IntVar(value=0)
        self.inputs["mp"] = tk.IntVar(value=0)
        self.inputs["buff"] = {
            "name": tk.StringVar(value=""),
            "difficulty": tk.IntVar(value=0),
        }
        self.inputs["debuff"] = {
            "name": tk.StringVar(value=""),
            "difficulty": tk.IntVar(value=0),
        }

    def process(self):
        result = {
            "name": self.inputs["name"].get(),
            "offensive stat": self.inputs["offensive stat"].get(),
            "defensive stat": self.inputs["defensive stat"].get(),
            "type": self.inputs["type"].get(),
            "range": self.inputs["range"].get(),
            "extra difficulty": self.inputs["extra difficulty"].get(),
            "element": self.inputs["element"].get(),
            "slow": self.inputs["slow"].get(),
            "mp": self.inputs["mp"].get(),
        }

        for rider in ["buff", "debuff"]:
            name = self.inputs[rider]["name"].get()
            difficulty = self.inputs[rider]["difficulty"].get()
            if name:
                result[rider] = {
                    "name": name,
                    "difficulty": difficulty,
                }

        attack_name = result["name"]
        self.result = f"'{attack_name}': {result}".strip()

    def draw_screen(self):
        self.draw_base_info()
        self.draw_element()
        self.draw_riders()
        self.draw_execute_button(row=3, column=0, sticky=tk.NW, pady=10)
        self.draw_result()

    def draw_base_info(self):
        base_frame = tk.Frame(self.tab)
        base_frame.grid(row=0, column=0, rowspan=2, sticky=tk.NW)

        tk.Label(base_frame, text="Name").grid(sticky=tk.NW)
        tk.Entry(base_frame, textvariable=self.inputs["name"]).grid(sticky=tk.NW)
        tk.Label(base_frame, text="Range").grid(sticky=tk.NW)
        tk.Entry(base_frame, textvariable=self.inputs["range"]).grid(sticky=tk.NW)

        tk.Label(base_frame, text="Extra difficulty").grid(sticky=tk.NW)
        tk.Entry(base_frame, textvariable=self.inputs["extra difficulty"]).grid(
            sticky=tk.NW
        )

        tk.Label(base_frame, text="Slow").grid(sticky=tk.NW)
        tk.Entry(base_frame, textvariable=self.inputs["slow"]).grid(sticky=tk.NW)

        tk.Label(base_frame, text="Mp").grid(sticky=tk.NW)
        tk.Entry(base_frame, textvariable=self.inputs["mp"]).grid(sticky=tk.NW)

        tk.Label(base_frame, text="Type").grid(sticky=tk.NW)
        for attack_type in ATTACK_TYPE_LIST:
            tk.Radiobutton(
                base_frame,
                text=attack_type,
                value=attack_type.lower(),
                variable=self.inputs["type"],
            ).grid(sticky=tk.NW)

        stat_frame = tk.Frame(self.tab)
        stat_frame.grid(row=0, column=1, sticky=tk.NW)
        tk.Label(stat_frame, text="Offensive stat").grid(sticky=tk.NW)
        for stat in BASE_ATTRIBUTES:
            tk.Radiobutton(
                stat_frame,
                text=stat,
                value=stat,
                variable=self.inputs["offensive stat"],
            ).grid(sticky=tk.NW)

        tk.Label(stat_frame, text="Defensive stat").grid(sticky=tk.NW)
        for stat in BASE_ATTRIBUTES:
            tk.Radiobutton(
                stat_frame,
                text=stat,
                value=stat,
                variable=self.inputs["defensive stat"],
            ).grid(sticky=tk.NW)

    def draw_element(self):
        frame = tk.Frame(self.tab)
        frame.grid(row=0, column=3, rowspan=3, sticky=tk.NW)

        tk.Label(frame, text="Element").grid(sticky=tk.NW)
        for element in ELEMENT_LIST:
            tk.Radiobutton(
                frame,
                text=element,
                value=element.lower(),
                variable=self.inputs["element"],
            ).grid(sticky=tk.NW)

    def draw_riders(self):
        frame = tk.Frame(self.tab)
        frame.grid(row=0, column=4, sticky=tk.NW)

        tk.Label(frame, text="Buff").grid(pady=10, sticky=tk.NW)
        tk.Label(frame, text="Name").grid(sticky=tk.NW)
        tk.Entry(frame, text="Name", textvariable=self.inputs["buff"]["name"]).grid(
            sticky=tk.NW
        )
        tk.Label(frame, text="Difficulty").grid(sticky=tk.NW)
        tk.Entry(
            frame, text="Difficulty", textvariable=self.inputs["buff"]["difficulty"]
        ).grid(sticky=tk.NW)

        tk.Label(frame, text="Debuff").grid(pady=10, sticky=tk.NW)
        tk.Label(frame, text="Name").grid(sticky=tk.NW)
        tk.Entry(frame, textvariable=self.inputs["debuff"]["name"]).grid(sticky=tk.NW)
        tk.Label(frame, text="Difficulty").grid(sticky=tk.NW)
        tk.Entry(frame, textvariable=self.inputs["debuff"]["difficulty"]).grid(
            sticky=tk.NW
        )

    def draw_result(self):
        frame = tk.Frame(self.tab)
        frame.grid(row=4, column=0, columnspan=100, sticky=tk.NW)

        tk.Label(frame, text="Result").grid(sticky=tk.NW)
        self.result_field = tk.Text(frame, height=10)
        self.result_field.config(font=("Courier", 14))
        self.result_field["state"] = "disabled"
        self.result_field.grid(sticky=tk.NW)
