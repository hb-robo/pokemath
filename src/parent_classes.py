"""
Refactor of the "classes.py" Monster class, to work with JSON data
that resembles a Pokedex entry. Only serves as a template for game-specific 
subclasses to work with, and will fail if instantiated.
"""

import json


class Pokemon():
    def __init__(
        self, name, level=50,
        item=None, ability=None,
        nature=None, iv_spread=None, ev_spread=None,
        custom_movepool=None, custom_stats=None,
        pokedex_path=None, constants=None
    ):
        # Set mandatory values
        self._name = name
        self._level = level

        # Set optional values
        # Ability only "optional" because they don't exist in Gens 1/2
        if ability is not None:
            self._ability = ability
        if item is not None:
            self._item = item

        # Grab static values from corresponding Pokedex
        self.getDexEntry(pokedex_path)

        # Override values for pokedex return
        if nature is not None:
            self._nature = nature
        if custom_movepool is not None:
            if (isinstance(custom_movepool, list)):
                if all(isinstance(elem, str) for elem in custom_movepool):
                    self._movepool = custom_movepool
                TypeError("Custom movepool list contains non-string elements")
            else:
                TypeError("Custom movepool must be a list.")
        if custom_stats is not None:
            if isinstance(custom_stats, dict):
                for stat, value in custom_stats.items():
                    setattr(self, stat, value)
            else:
                TypeError("Argument for 'custom_stats' must be a dictionary.")

        # Instantiate other battle-related constants
        self.instantiateConstants(constants)

    def getDexEntry(self, pokedex_path):
        if pokedex_path is None:
            raise FileNotFoundError("Pokedex file not defined.")
        with open(pokedex_path, 'r') as pokedex_json:
            pokedex = json.load(pokedex_json)
            if self.name not in list(pokedex.keys()):
                raise ValueError(
                    f"Pokemon '{self.name}' not found in Pokedex."
                )
            for key, value in pokedex[self.name].items():
                setattr(self, key, value)

    def instantiateConstants(self, constants):
        if constants is None:
            raise ValueError("Constants not defined.")
        for key, value in constants.items():
            setattr(self, key, value)

    """
    Each property has overridden setters to provide type validation and SOME
    value validation. To prevent class bloat, Pokemon instances will not carry
    with them dictionaries of legal values corresponding to their generation,
    for instance the array of legal types. Instead, the class will validate the
    type, and the corresponding Battle classes will check for legal values.
    """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == '':
            raise ValueError("Pokemon name must be a non-empty string.")
        self._name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int) or value < 1 or value > 100:
            raise ValueError(
                "Pokemon level must be an int between 1 and 100, inclusive."
            )
        self._level = value

    @property
    def type1(self):
        return self._type1

    @type1.setter
    def type1(self, value):
        if not isinstance(value, str) or value == '':
            raise ValueError("Pokemon Type1 must be a non-empty string")
        self._type1 = value

    @property
    def type2(self):
        return self._type2

    @type2.setter
    def type2(self, value):
        # Not all Pokemon have two types, so empty string and None are valid.
        if not isinstance(value, str) and value is not None:
            raise ValueError("Pokemon Type2 must be None or a string")
        self._type2 = value

    @property
    def tera_type(self):
        return self._tera_type

    @tera_type.setter
    def tera_type(self, value):
        # Only Gen 9 has Tera types, so empty string and None are valid.
        if not isinstance(value, str) and value is not None:
            raise ValueError("Pokemon Type2 must be None or a string")
        self._tera_type = value

    """
    Pokemon Statistics Overridden Setters
    """

    @property
    def hp(self):
        return self._HP

    @hp.setter
    def hp(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's HP must an int greater than 0.")
        self._hp = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's Attack must an int greater than 0.")
        self._attack = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's Defense must an int greater than 0.")
        self._defense = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's Speed must an int greater than 0.")
        self._speed = value

    # SPECIAL stat only used for Gen1.
    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's Special must an int greater than 0.")
        self._special = value

    # SP.ATT and SP.DEF stats only used for Gen2 onwards.
    @property
    def sp_attack(self):
        return self._sp_attack

    @sp_attack.setter
    def sp_attack(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's Sp. Attack must an int >0.")
        self._sp_attack = value

    @property
    def sp_defense(self):
        return self._sp_defense

    @sp_defense.setter
    def sp_defense(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Pokemon's Sp. Defense must be an int >0.")
        self._sp_defense = value

    """
    Overridden setters for other physical attributes
    """

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, float) or value <= 0.0:
            raise ValueError("Pokemon's height must a float greater than 0.")
        self._height = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if not isinstance(value, float) or value <= 0.0:
            raise ValueError("Pokemon's weight must a float greater than 0.")
        self._weight = value

    """
    TODO:
        Implement custom IV/EV spreads for stats distributions
        Implement nature as effect on stats distribution
        Overridden setters for movepool
    """