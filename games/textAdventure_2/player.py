'''
    This is the player class template, you can base on this and create the base class (character) and plan out the monster, item classes. 
'''
from utils import get_input
import inquirer
from data.items import *
import time

class Player:
    def __init__(self, start_pos):
        # Initialize player attributes:
        # self.name = name
        self.health = {"base": 100, "temp": 0, "maximum": 100}
        self.damage = {"base": 5, "temp": 0}
        self.weapon = {"name": "Fists", "strength": 0}
        self.offhand = {"name": "Nothing", "strength": 0}
        self.inventory = {}
        self.cash = 0
        self.armor = {
            "head": {"name": "", "strength": 0},
            "body": {"name": "", "strength": 0},
            "legs": {"name": "", "strength": 0},
            "boot": {"name": "", "strength": 0},
        }
        self.position = start_pos
        self.visited_rooms = [(0,0)]
        self.total_str = {"base": 0, "temp": 0}#used for further calculations.
        # - position (start_pos)
        # - gold = 100
        # - hp = max_hp = 100
        # - attack = 5, defense = 3
        # - temp_attack, temp_defense = 0
        # - empty inventory list
        # - visited_rooms set that includes start_pos ( this will help to track which room has been discovered)

        
        pass

    def calc_total_str(self):
        self.total_str['base'] = 0
        for part in self.armor.keys():
            self.total_str['base'] += self.armor[part]['strength']

    def update_position(self, new_pos):
        self.position = new_pos
        self.visited_rooms.append(new_pos)


    def show_inventory(self):
        # Show inventory menu:
        if len(self.inventory) == 0:
            print('You have nothing in your inventory.')
        else:
            print("\n-- INVENTORY --")
            inv = self.inventory
            keys = list(inv.keys())

            for i, key in enumerate(keys, 1):
                item = inv[key]
                print(f"{i}. {item.name} | Type: {item.type} | Effect: {item.effect_type} +{item.effect_value} | Cost: {item.cost}")

            usage = get_input("Do you want to use an item? (y/n)")
            if usage == "y":
                choices = [(item) for item in keys]

                questions = [
                    inquirer.List(
                        "item_chosen",
                        message = "Which item do you want to choose?",
                        choices = choices
                    )
                ]

                answers = inquirer.prompt(questions)
                selected = answers["item_chosen"]

                used = inv[selected]
                used.apply(self)

                index = choices.index(selected)
                inv.pop(keys[index])
        input("Press enter to continue.")
        # - If empty: show message
        # - Else: list all items with name and effect
        # below is later implementation
        # - Let user choose one to use
        # - If item is usable, apply effect and remove from inventory
        # - Otherwise, inform the player it's passive
        pass

    def show_stats(self):
        self.calc_total_str()
        print('-- STATS --')
        # print('* means temporary effects!')
        print(f"HP: {self.health['base']}/{self.health['maximum']}")
        print(f"Damage: {self.damage['base'] + self.weapon['strength'] + self.damage['temp']}")
        print(f"Defense: {self.total_str['base'] + self.offhand['strength'] + self.total_str['temp']}")
        print(f"Coins: {self.cash}")
        time.sleep(3)
        # Display player stats:
        # - HP, attack, defense, gold
        # - Indicate temporary effects with an asterisk
        pass

    # def remove_temp_effect(self):
    #     Remove any temporary attack/defense bonuses
    #     - Subtract temp_attack and temp_defense from current stats
    #     - Reset temp values to 0
    #     pass

    def add_item(self, item):
        self.inventory[item.name] = item
