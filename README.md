# ffrpg4e-utils
Ferramenta para me ajudar a mestrar o sistema Final Fantasy RPG 4e no Roll20. Feito em python 3.10.4 e Windows 10

Configuração:
1. Os dados do time de jogadores devem ser coletados do roll20 e introduzidos no arquivo data.py
- Na mesa, tem um macro responsável por printar os dados dos jogadores em código python-like (dict):\
```/w gm Info da party em python dict: 🐍{"Bernard": {"earth": [[@{Bernard|earth_points}]], "air": [[@{Bernard|air_points}]], "fire": [[@{Bernard|fire_points}]], "water": [[@{Bernard|water_points}]], "arm": [[@{Bernard|arm}]], "marm": [[@{Bernard|marm}]], "init": 3}, "Dio": {"earth": [[@{Dio|earth_points}]], "air": [[@{Dio|air_points}]], "fire": [[@{Dio|fire_points}]], "water": [[@{Dio|water_points}]], "arm": [[@{Dio|arm}]], "marm": [[@{Dio|marm}]], "init": 3}, "Nyssa": {"earth": [[@{Nyssa|earth_points}]], "air": [[@{Nyssa|air_points}]],  "fire": [[@{Nyssa|fire_points}]], "water":  [[@{Nyssa|water_points}]], "arm": [[@{Nyssa|arm}]], "marm": [[@{Nyssa|marm}]], "init": 3}}```
2. Os dados dos monstros são gerados na ferramenta, também devem ser carregados em data.py


Execução:

```py -m main```
