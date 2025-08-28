'''
    This is the player class template, you can base on this and create the base class (character) and plan out the monster, item classes. 
'''
from utils import get_input
import inquirer
from data.items import *

class Player:
    def __init__(self, start_pos):
        # Initialize player attributes:
        # self.name = name
        self.health = self.max_hp = {"base": 100, "temp": 0}
        self.damage = {"base": 5, "temp": 0}
        self.weapon = "Fists"
        self.inventory = {}
        self.cash = 0
        self.armor = [
            {"type": "head", "name": "", "strength": 0},
            {"type": "body", "name": "", "strength": 0},
            {"type": "legs", "name": "", "strength": 0},
            {"type": "boot", "name": "", "strength": 0}
        ]
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
        for i in range(len(self.armor)):
            self.total_str[0] += self.armor[i][2]
        pass

    def update_position(self, new_pos):
        self.position = new_pos
        self.visited_rooms.append(new_pos)


    def show_inventory(self):
        # Show inventory menu:
        if len(self.inventory) == 0:
            print('You have nothing in your inventory.')
        else:
            inv = self.inventory
            print(inv)
            keys = list(inv.keys())
            for i in range(len(keys)):
                print(f"{keys[i]}")
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
        print(f"HP: {self.health[0]}, Damage: {self.damage[0]}, Defense: {self.total_str[0]}, Coins: {self.cash}")
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
        self.inventory.append(item)
        pass
