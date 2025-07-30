import random
from data.items import item_pool
from time import sleep
from utils import get_input

'''
This is the class where you create multiple type of rooms. Use this for structure it building other sprite classes
'''


class Room:
    def __init__(self, pos):
        self.pos = pos
        self.description = "A plain room."

    def enter(self, player, map_manager, just_describe=False):
        print('You are at', self.pos, 'Description:', self.description)
        # If not just_describe, trigger interact()
        # Else, briefly pause for flavor
        pass

    def interact(self, player, map_manager):
        # Placeholder: to be overridden in subclasses
        pass


class EmptyRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.description = "It's quiet and empty."


class MonsterRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.description = "A monster blocks your path!"
        self.defeated = False

    def interact(self, player, map_manager):
        # If defeated: print remains
        # Else:
        #   Ask player to fight (y/n)
        #   If yes: simulate simple combat (lose HP), mark as defeated
        #   Else: skip fight
        pass


class StoreRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.description = "You find a market with items for sale."
        self.inventory = random.sample(item_pool, k=3)

    def interact(self, player, map_manager):
        # Show items in store (name + cost)
        # Let player choose item to buy
        #   - If enough gold: deduct gold, add item to inventory, remove from store
        #   - If not enough gold: inform player
        # Option to exit
        pass


class PortalRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.description = "A glowing portal hums mysteriously."

    def interact(self, player, map_manager):
        # Show available floors to travel (up/down)
        # Let player choose floor
        # If valid: switch map_manager floor and teleport player
        # Else: do nothing
        pass


class BossRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.description = "The Final Boss awaits!"
        self.defeated = False

    def interact(self, player, map_manager):
        # If defeated: show message
        # Else:
        #   Ask player to fight
        #   If yes: simulate boss fight (lose HP), mark as defeated
        #   Else: skip fight
        pass

