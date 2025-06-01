STAT_LIST = [
    "Earth",
    "Air",
    "Fire",
    "Water",
]

PLAYERS = {
    "Bernard": {
        "earth": 100,
        "air": 100,
        "fire": 60,
        "water": 100,
        "arm": 27,
        "marm": 10,
        "init": 3,
    },
    "Dio": {
        "earth": 70,
        "air": 90,
        "fire": 100,
        "water": 100,
        "arm": 14,
        "marm": 26,
        "init": 3,
    },
    "Nyssa": {
        "earth": 80,
        "air": 100,
        "fire": 100,
        "water": 84,
        "arm": 25,
        "marm": 10,
        "init": 3,
    },
}


MONSTERS = {
    "ab": {
        "level": 30,
        "class": "brute",
        "importance": "boss",
        "elements": [],
        "earth": 100,
        "air": 100,
        "water": 70,
        "fire": 70,
        "hp": 1374,
        "mp": 388,
        "arm": 60,
        "marm": 15,
        "dmg_multiplier": 11,
        "init": 5,
        "attack_difficulty": 20,
        "dmg_earth": 110,
        "dmg_air": 110,
        "dmg_fire": 77,
        "dmg_water": 77,
        "attacks": {
            "golpe": {
                "name": "golpe",
                "offensive stat": "earth",
                "defensive stat": "earth",
                "type": "physical",
                "range": 1,
                "extra difficulty": 0,
                "element": "crush",
                "slow": 0,
                "mp": 0,
            }
        },
    }
}

ELEMENT_LIST = [
    "Crush",
    "Puncture",
    "Cut",
    "Fire",
    "Ice",
    "Lightning",
    "Air",
    "Earth",
    "Water",
    "Bio",
    "Light",
    "Shadow",
]


ATTACK_TYPE_LIST = ["Physical", "Magical"]

# Mental: Berserk, Charm, Confuse, Sleep
# Illusion: Blink, Vanish
# Seal: Blind, Disable, Immobilize, Mute
# Fatal: Condemn, Death, Gravity
# Elemental: Vulnerable: (Element), Resist: (Element), Immune: (Element), Absorb: (Element)
# Weaken: Curse, Meltdown, Weaken: [Armor, Magic, Mental, Physical, Speed]
# Strengthen: Regen, Strengthen: [Armor, Magic, Mental, Physical, Speed]
# Flight: Float, Flight
# Time: Slow, Stop, Haste, Premonition
# Toxic: Poison, Virus
# Barrier: Protect, Shell, Reflect, Reraise, Wall
# Transform: Stone, Toad, Zombie

LAWS = {
    "Action": [
        "Flanquear",
        "Bater De Frente",
        "Reações",
        "!Item",
        "!Flee",
        "Atacar fora do range",
        "Atacar mais que 4 quadrados",
        "Zone of control",
        "multiplos alvos",
        "alvo próprio",
        "curar hp",
        "repetir última ação",
    ],
    "Element": ELEMENT_LIST,
    "Weapon": [
        "Light Swords / Knives",
        "Weapons & Shields",
        "Heavy Weapons",
        "Polearms",
        "Claws / Gloves",
        "Katanas",
        "Bows",
        "Throwing Weapons",
        "Rifles / Crossbows",
        "Wands",
        "Staves",
        "Instruments",
        "Twin Blades",
    ],
    "Status": [
        "Mental",
        "Illusion",
        "Seal",
        "Fatal",
        "Elemental",
        "Weaken",
        "Strengthen",
        "Flight",
        "Time",
        "Toxic",
        "Barrier",
        "Transform",
    ],
}
