from utils import get_input
import inquirer
from data.items import *

class Player:
    def __init__(self, name, start_pos):
        # Initialize player attributes:
        self.name = name
        self.health = self.max_hp = {"base": 100, "temp": 0}
        self.damage = {"base": 5, "temp": 0}
        self.weapon = "Fists"
        self.inventory = []
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
        for piece in range(self.armor):
            self.total_str["base"] += piece["stats"]
        pass

    def update_position(self, new_pos):
        self.position = new_pos
        self.visited_rooms.append(new_pos)


    def show_inventory(self):
        # Show inventory menu:
        if len(self.inventory) == 0:
            print('You have nothing in your inventory.')
        else:
            for i in range(len(self.inventory)):
                print(f"{self.inventory[i]['name']}")
            usage = get_input("Do you want to use an item? (y/n)")
            if usage == "y":
                choices = [(item['name'], item) for item in self.inventory]

                questions = [
                    inquirer.List(
                        "item_chosen",
                        message = "Which item do you want to choose?",
                        choices = choices
                    )
                ]

                answers = inquirer.prompt(questions)
                selected = answers["choice"]
                index = choices.index(selected)
        get_input("Press space to continue.")
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
        print(f"HP: {self.health["base"]}, Damage: {self.damage["base"]}, Defense: {self.total_str["base"]}, Coins: {self.cash}")
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
