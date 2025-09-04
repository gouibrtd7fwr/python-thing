from utils import get_input
from data.items import *

class Character:
    def __init__(self, name, start_pos):
        # Initialize player attributes:
        self.name = name
        self.health = self.max_hp = {"base": 100, "temp": 0}
        self.damage = {"base": 5, "temp": 0}
        self.weapon = "Fists"
        self.armor = [
            {"type": "head", "name": "", "strength": 0},
            {"type": "body", "name": "", "strength": 0},
            {"type": "legs", "name": "", "strength": 0},
            {"type": "boot", "name": "", "strength": 0}
        ]
        self.position = start_pos
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

    def show_stats(self):
        self.calc_total_str()
        print("-- Character's Stats --")
        # print('* means temporary effects!')
        print(f"HP: {self.health["base"]}, Damage: {self.damage["base"]}, Defense: {self.total_str["base"]}")
        # Display player stats:
        # - HP, attack, defense, gold
        # - Indicate temporary effects with an asterisk
        pass

    # def remove_temp_effect(self):
    #     Remove any temporary attack/defense bonuses
    #     - Subtract temp_attack and temp_defense from current stats
    #     - Reset temp values to 0
    #     pass
