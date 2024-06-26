# Pokemon Type Labels and Categories
TYPES = [
    'Normal', 'Fighting', 'Poison', 'Ground', 'Flying', 'Bug', 'Rock', 'Ghost',
    'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Psychic', 'Dragon'
]
PHYS_TYPES = [
    'Normal', 'Fighting', 'Poison', 'Ground', 'Flying', 'Bug', 'Rock', 'Ghost'
]
SPEC_TYPES = [
    'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Psychic', 'Dragon'
]
TYPE_COLORS = {  # sourced from Pocket Monsters' Stadium (1998)
    'Normal': '#a3a3a3',
    'Fire': '#c13e2c',
    'Fighting': '#c6703e',
    'Water': '#4d9bda',
    'Flying': '#4864b6',
    'Grass': '#55ab38',
    'Poison': '#7f54a4',
    'Electric': '#c1a549',
    'Ground': '#957b42',
    'Psychic': '#c2589a',
    'Rock': '#5c7979',
    'Ice': '#71acc4',
    'Bug': '#679a33',
    'Dragon': '#4da396',
    'Ghost': '#9e73b5'
}

# Statistic Labels and Names
STATS = ['HP', 'Attack', 'Defense', 'Special', 'Speed', 'Accuracy', 'Evasion']
BASE_STATS = ['HP', 'Attack', 'Defense', 'Special', 'Speed']

# Statistic Stages
statStages = {
    6: 4.00,
    5: 3.50,
    4: 3.00,
    3: 2.50,
    2: 2.00,
    1: 1.50,
    0: 1.00,
    -1: 0.66,
    -2: 0.50,
    -3: 0.40,
    -4: 0.33,
    -5: 0.28,
    -6: 0.25
}
evasionStages = {
    6: 0.25,
    5: 0.28,
    4: 0.33,
    3: 0.40,
    2: 0.50,
    1: 0.66,
    0: 1.00,
    -1: 1.50,
    -2: 2.00,
    -3: 2.50,
    -4: 3.00,
    -5: 3.50,
    -6: 4.00
}

# Status Conditions
NON_VOLATILE_STATUS_CONDITIONS = ["Burn", "Freeze", "Paralysis", "Poison", "Toxic", "Sleep", "Clear"]
VOLATILE_STATUS_CONDITIONS = ["Substitute", "Transform", "Bound", "Curse", "Disable", "Confusion",
                              "Focused", "Rampage", "Bide", "Recharge", "Fly", "Dig", "Flinch"]

MULTI_HIT_DISTRIBUTION = {
    1: 0.000,
    2: 0.375,
    3: 0.375,
    4: 0.125,
    5: 0.125
}

BOUND_DURATION_DISTRIBUTION = MULTI_HIT_DISTRIBUTION
BIDE_DURATION_DISTRIBUTION = {
    2: 0.500,
    3: 0.500
}
THRASH_PETAL_DANCE_DURATION_DISTRIBUTION = {
    3: 0.500,
    4: 0.500
}

PM_RGBP_CONSTANTS = {}
PM_S_CONSTANTS = {}
PM_S2_CONSTANTS = {}
PKMN_RBY_CONSTANTS = {}
PKMN_S_CONSTANTS = {}
