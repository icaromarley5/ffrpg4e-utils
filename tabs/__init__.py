from . import (
    enemy_attack,
    player_attack,
    player_reaction,
    initiative_generation,
    laws_selection,
    enemy_creation,
)


TABS_LIST = [
    player_attack.PlayerAttackTab,
    enemy_attack.EnemyAttackTab,
    player_reaction.PlayerReactionTab,
    initiative_generation.InitiativeGenerationTab,
    laws_selection.LawsSelectionTab,
    enemy_creation.EnemyCreationTab,
    enemy_creation.EnemyAttackCreationTab,
]
