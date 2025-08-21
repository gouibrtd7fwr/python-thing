'''
    This is the simple class of items where you need to create the class and also the list of items.
    You could create list of item in teir and try to implemented with the store
'''

import random

obj_types = ["head_armor", "body_armor", "leg_armor", "boot_armor", "att_weapon", "def_weapon", "potion"]

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

    def apply(self, player):
        if self.effect_type == 'attack':
            player.attack += self.effect_value
        elif self.effect_type == 'defense':
            player.defense += self.effect_value
        elif self.effect_type == 'heal':
            player.hp = min(player.max_hp, player.hp + self.effect_value)
        elif self.effect_type == 'temp_attack':
            player.temp_attack += self.effect_value
            player.attack += self.effect_value 
        elif self.effect_type == 'temp_defense':
            player.temp_defense += self.effect_value
            player.defense += self.effect_value
    

item_pool = [
    Item("Sword","att_weapon", 10, "attack", 2),
    Item("Shield","def_weapon", 8, "defense", 2),
    Item("Small Health Potion","potion", 5, "heal", 10),
    Item("Axe","att_weapon", 12, "attack", 3),
    Item("Leather Helmet","head_armor", 7, "defense", 1),
    Item("Big Health Potion", 10,"potion", "heal", 25),
    Item("Strength Potion","potion", 9, "temp_attack", 5),
    Item("Defense Potion","potion", 9, "temp_defense", 5)
]
