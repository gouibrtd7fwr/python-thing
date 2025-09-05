import random
from data.items import item_pool
from time import sleep
from utils import get_input
from data.enemies import enemy_pool
import inquirer

'''
This is the class where you create multiple type of rooms. Use this for structure it building other sprite classes
'''


class Room:
    def __init__(self, pos):
        self.pos = pos
        self.description = "A plain room."

    def enter(self, player, map_manager, just_describe=False):
        print('You are at', self.pos, 'Description:', self.description)
        if just_describe == False:
            self.interact(player, map_manager)
        sleep(1)    
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
        # self.enemies_to_fight = 1
        self.enemy_pool = random.sample(enemy_pool, k=1)
        self.enemy_name = self.enemy_pool[0].name
        self.enemy = {str(self.enemy_name): self.enemy_pool[0]}

    def interact(self, player, map_manager):
        if self.defeated:
            print('The corpse of the monster lays dead in front of you')
        else:
            fight = get_input(f"Do you want to fight it? (E)")
            if fight.lower() == 'e':
                print('\nThe fight has started!')
                self.enemy_util = self.enemy[self.enemy_name]
                while player.health['base'] > 0 and self.enemy_util.health > 0:
                    self.enemy_util.health -= player.damage['base']
                    player.health['base'] -= self.enemy_util.damage
                    print(f"Your health: {player.health['base']}, Monster's health: {self.enemy_util.health}")
                    sleep(1)
            else:
                print('You chose to not fight the monster.')
        # If defeated: print remains
        # Else:
        #   Ask player to fight (y/n)
        #   If yes: simulate simple combat (lose HP), mark as defeated
        #   Else: skip fight
        pass


class StoreRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.items_to_sell = 3
        self.description = "You find a market with items for sale."
        self.item_pool = random.sample(item_pool, k=self.items_to_sell)
        self.inventory = dict()
        for item in self.item_pool:
            self.inventory[item.name] = item

    def buy(self, player, item):
        if player.cash >= item.cost:
            player.cash -= item.cost
            return True
        else:
            return False

    def interact(self, player, map_manager):
        print('Welcome to the Shop!')
        print('Available items are shown below!')
        for i in range(len(self.inventory)):
            print("\n-- Shop --")
            inv = self.inventory
            keys = list(inv.keys())

            for i, key in enumerate(keys, 1):
                item = inv[key]
                print(f"{i}. {item.name} | Type: {item.type} | Effect: {item.effect_type} +{item.effect_value} | Cost: {item.cost}")

            purchase = get_input("Do you want to buy an item? (y/n)")
            if purchase == "y":
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

                bought = inv[selected]
                # bought.apply(self)
                transaction_res = self.buy(player, bought)
                index = choices.index(selected)
                if transaction_res == True:
                    player.add_item(bought)
                    inv.pop(keys[index])
                    print('Your transaction was successful!')
                else:
                    print('You do not have enough money to buy this item!')
            elif purchase == 'n':
                pass
            else:
                print('Command not found.')
                sleep(2)
                pass
        input("Press enter to continue.")
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
        if self.defeated:
            print('The remains of the large boss lay here in this room.')
        else:
            fight = get_input("Do you want to fight it? (E)")
            if fight.lower() == 'e':
                print('The fight has started!')
                self.hp -= player.damage
                player.health -= self.damage
            else:
                print('You chose to not fight the boss.')
        # If defeated: show message
        # Else:
        #   Ask player to fight
        #   If yes: simulate boss fight (lose HP), mark as defeated
        #   Else: skip fight
        pass

class LootRoom(Room):
    def __init__(self, pos):
        super().__init__(pos)
        self.looted = False
        self.items_inside_chest = 1
        self.description = "You find a chest with something inside it..."
        self.loot = random.sample(item_pool, k=self.items_inside_chest)

    def interact(self, player, map_manager):
        if self.looted == False:
            for i in range(len(self.loot)):
                print(f"You found: {self.loot[i].name}!")
                player.add_item(self.loot[i])
                self.looted = True
            input()
        else:
            print('You have already looted this room.')
        # If defeated: show message
        # Else:
        #   Ask player to fight
        #   If yes: simulate boss fight (lose HP), mark as defeated
        #   Else: skip fight
        pass

