'''
    This is the simple class of items where you need to create the class and also the list of items.
    You could create list of item in teir and try to implemented with the store
'''

import random

obj_types = ["head_armor", "body_armor", "legs_armor", "boot_armor", "att_weapon", "def_weapon", "potion"]

class Item:
    def __init__(self, name, obj_type, cost, effect_type, effect_value):
        if obj_type in obj_types:
            self.type = obj_type
        else:
            print("Cannot find object type. Cannot initialize.")
        self.name = name
        self.cost = cost
        self.effect_type = effect_type  # e.g., 'attack', 'defense', 'heal', 'temp_attack'
        self.effect_value = effect_value
        # self.effect_length = effect_length

    def apply(self, player):
        if self.effect_type == 'attack':
            player.damage['base'] += self.effect_value
            player.weapon = {"name": self.name, "strength": self.effect_value}
        elif self.effect_type == 'defense':
            if self.type == "head_armor":
                player.armor["head"] = {"name": self.name, "strength": self.effect_value}
            elif self.type == "body_armor":
                player.armor["body"] = {"name": self.name, "strength": self.effect_value}
            elif self.type == "legs_armor":
                player.armor["legs"] = {"name": self.name, "strength": self.effect_value}
            elif self.type == "boot_armor":
                player.armor["boot"] = {"name": self.name, "strength": self.effect_value}
            elif self.type == "def_weapon":
                player.offhand = {"name": self.name, "strength": self.effect_value}
        elif self.effect_type == 'heal':
            player.health['base'] = player.health['base'] + self.effect_value
            if player.health['base'] >= player.health['maximum']:
                player.health['base'] = player.health['maximum']
        elif self.effect_type == 'temp_attack':
            player.damage['temp'] += self.effect_value
        elif self.effect_type == 'temp_defense':
            player.total_str['temp'] += self.effect_value

class Key(Item):
    def __init__(self, name, level):
        super().__init__(name, None, None, None, None)
        self.level = level
        self.cost = self.level * 5

item_pool = [
    Item("Sword","att_weapon", 10, "attack", 2),
    Item("Shield","def_weapon", 8, "defense", 2),
    Item("Small Health Potion", "potion", 5, "heal", 10),
    Item("Axe","att_weapon", 12, "attack", 3),
    Item("Leather Helmet","head_armor", 7, "defense", 1),
    Item("Big Health Potion", "potion", 10, "heal", 25),
    Item("Strength Potion","potion", 9, "temp_attack", 5),
    Item("Defense Potion","potion", 9, "temp_defense", 5),
]

enemy_item_pool = [
    Item("Venom", "potion", 5, 'temp_attack', 3),
    Item("Ghostly Jar", "potion", 7, 'temp_defense', 4),
    Item('Iron Plate', 'body_armor', 15, 'defense', 6),
]
