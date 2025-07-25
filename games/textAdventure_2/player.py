'''
    This is the player class template, you can base on this and create the base class (character) and plan out the monster, item classes. 
'''

class Player:
    def __init__(self, start_pos):
        # Initialize player attributes:
        self.health = self.max_hp = 100
        self.damage = 5
        self.weapon = "Fists"
        self.inventory = []
        self.cash = 0
        self.armor = {
            'head': '',
            'body': '',
            'legs': '',
            'boot': ''
        }
        self.start_pos = (0,0)
        self.visited_rooms = [(0,0)]
        # - position (start_pos)
        # - gold = 100
        # - hp = max_hp = 100
        # - attack = 5, defense = 3
        # - temp_attack, temp_defense = 0
        # - empty inventory list
        # - visited_rooms set that includes start_pos ( this will help to track which room has been discovered)

        
        pass

    def update_position(self, new_pos):
        # Update player's position and add it to visited_rooms
        pass

    def show_inventory(self):
        # Show inventory menu:
        # - If empty: show message
        # - Else: list all items with name and effect
        # - Let user choose one to use
        # - If item is usable, apply effect and remove from inventory
        # - Otherwise, inform the player it's passive
        pass

    def show_stats(self):
        # Display player stats:
        # - HP, attack, defense, gold
        # - Indicate temporary effects with an asterisk
        pass

    def remove_temp_effect(self):
        # Remove any temporary attack/defense bonuses
        # - Subtract temp_attack and temp_defense from current stats
        # - Reset temp values to 0
        pass

    def add_item(self, item):
        # Add item to player's inventory
        pass
