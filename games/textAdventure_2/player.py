'''
    This is the player class template, you can base on this and create the base class (character) and plan out the monster, item classes. 
'''

class Player:
    def __init__(self, start_pos):
        # Initialize player attributes:
        self.health = self.max_hp = [100, 0]
        self.damage = [5, 0]
        self.weapon = "Fists"
        self.inventory = {}
        self.cash = 0
        self.armor = [
            ['head', '', 0]
            ['body', '', 0]
            ['legs', '', 0]
            ['boot', '', 0]
        ]
        self.start_pos = (0,0)
        self.visited_rooms = [(0,0)]
        self.total_str = [0, 0]#used for further calculations.
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
        self.visited_rooms.append(new_pos)
        # Update player's position and add it to visited_rooms
        pass

    def show_inventory(self):
        # Show inventory menu:
        if len(self.inventory) == 0:
            print('You have nothing in your inventory.')
        else:
            for i in range(len(self.inventory)):
                print(self.inventory[i])
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

    #def remove_temp_effect(self):
        # Remove any temporary attack/defense bonuses
        # - Subtract temp_attack and temp_defense from current stats
        # - Reset temp values to 0
        pass

    def add_item(self, item):
        self.inventory.append(item)
        pass
