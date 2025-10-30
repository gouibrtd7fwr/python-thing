import random
from data.items import item_pool
from time import sleep
from utils import get_input
from data.enemies import enemy_pool, bosses
import inquirer

'''
This is the class where you create multiple type of rooms. Use this for structure it building other sprite classes
'''


class Room:
    def __init__(self, pos, current_floor):
        self.pos = pos
        self.description = "A plain room."
        self.current_floor = current_floor

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
    def __init__(self, pos, current_floor):
        super().__init__(pos, current_floor)
        self.description = "It's quiet and empty."


class MonsterRoom(Room):
    def __init__(self, pos, current_floor):
        super().__init__(pos, current_floor)
        self.description = "A monster blocks your path!"
        self.defeated = False
        # self.enemies_to_fight = 1
        self.enemy_pool = random.sample(enemy_pool, k=1)
        self.enemy_name = self.enemy_pool[0].name
        self.enemy = {str(self.enemy_name): self.enemy_pool[0]}

    def interact(self, player, map_manager):
        if self.defeated:
            self.description = 'The corpse of the monster lays dead in front of you'
        else:
            fight = get_input(f"Do you want to fight {self.enemy_name}? (E)")
            player.defense = player.total_str['base'] + player.total_str['temp']

            
            if fight.lower() == 'e':
                print('\nThe fight has started!')
                self.enemy_util = self.enemy[self.enemy_name]

                while player.health['base'] > 0 and self.enemy_util.health > 0:
                    if player.health['base'] > 100:
                        player.health['base'] = 100
                    self.enemy_util.health -= player.damage['base'] + player.weapon['strength'] + player.damage['temp']
                    if player.defense <= self.enemy_util.damage:
                        player.health['base'] -= self.enemy_util.damage - player.defense
                    if player.health['base'] <= 0:
                        player.health['base'] = 0
                    elif self.enemy_util.health <= 0:
                        self.enemy_util.health = 0

                    print(f"Your health: {player.health['base']}, Monster's health: {self.enemy_util.health}")
                    sleep(1)
                if player.health['base'] <= 0:
                    print('You have been defeated by the monster...')
                    map_manager.game_over()
                elif self.enemy_util.health <= 0:
                    print('You have defeated the monster!')
                    self.defeated = True
                    player.cash += self.enemy_util.coin_amt
                    self.description = 'The corpse of the monster lays dead in front of you'
            else:
                print('You chose to not fight the monster.')
        # If defeated: print remains
        # Else:
        #   Ask player to fight (y/n)
        #   If yes: simulate simple combat (lose HP), mark as defeated
        #   Else: skip fight
        pass


class StoreRoom(Room):
    def __init__(self, pos, current_floor):
        super().__init__(pos, current_floor)
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
    def __init__(self, pos, current_floor):
        super().__init__(pos, current_floor)
        self.description = "A glowing portal hums mysteriously."

    def interact(self, player, map_manager):
        for i, keys in enumerate(player.inventory):
            if hasattr(player.inventory[keys], 'level'):
                print(f"\nYou have a {player.inventory[keys].name} which can unlock floor {player.inventory[keys].level}!")

        travel = get_input("Do you want to travel to another floor? (T)")
        if travel.lower() == 't':
            print('\nAvailable floors:')
            available_floors = []

            for i, keys in enumerate(player.inventory):
                if hasattr(player.inventory[keys], 'level'):
                    available_floors.append(player.inventory[keys].level)
                    print(f"- Floor {player.inventory[keys].level}")

            if len(available_floors) == 0:
                print('You do not have any keys to travel to another floor.')
            else:
                floor_choice = int(get_input('Enter the floor number you want to travel to: '))
                if floor_choice in available_floors and floor_choice != map_manager.current_floor:
                    map_manager.current_floor = floor_choice
                    
                    player.position = map_manager.get_start_position()
                    player.visited_rooms[map_manager.current_floor - 1].append(player.position)
                    print(f'\nTraveling to floor {floor_choice}...')
                elif floor_choice == map_manager.current_floor:
                    print('You are already on this floor.')
                else:
                    print('You do not have the key for that floor.')
                    
        else:
            print('You chose not to travel.')
        # If no keys: show message and exit

        # Show available floors to travel (up/down)
        # Let player choose floor
        # If valid: switch map_manager floor and teleport player
        # Else: do nothing
        pass


class BossRoom(Room):
    def __init__(self, pos, current_floor):
        super().__init__(pos, current_floor)
        self.description = "The boss of this floor awaits you!"
        self.defeated = False
        # self.enemies_to_fight = 1
        boss_key = f'floor_{current_floor}'
        self.boss = bosses[boss_key]
        self.enemy_name = self.boss.name
        self.enemy = {str(self.enemy_name): self.boss}

    def interact(self, player, map_manager):
        if self.defeated:
            self.description = 'The corpse of the boss lays dead, broken in front of you'
        else:
            fight = get_input(f"Do you want to fight {self.enemy_name}? (E)")
            player.defense = player.total_str['base'] + player.total_str['temp']
                
            if fight.lower() == 'e':
                print('\nThe fight has started!')
                self.enemy_util = self.enemy[self.enemy_name]

                while player.health['base'] > 0 and self.enemy_util.health > 0:
                    if player.health['base'] > 100:
                        player.health['base'] = 100
                    self.enemy_util.health -= player.damage['base'] + player.weapon['strength'] + player.damage['temp']
                    if player.defense <= self.enemy_util.damage:
                        player.health['base'] -= self.enemy_util.damage - player.defense
                    if player.health['base'] <= 0:
                        player.health['base'] = 0
                    elif self.enemy_util.health <= 0:
                        self.enemy_util.health = 0
                    print(f"Your health: {player.health['base']}, Boss's health: {self.enemy_util.health}")
                    sleep(1)

                if player.health['base'] <= 0:
                    print('You have been defeated by the boss...')
                    map_manager.game_over()
                elif self.enemy_util.health <= 0:
                    print('You have defeated the boss!')
                    self.defeated = True
                    player.cash += self.enemy_util.coin_amt
                    self.description = 'The corpse of the boss lays dead in front of you'
                    player.inventory[self.enemy_util.drop_key.name] = self.enemy_util.drop_key
                    print(f'You found a {self.enemy_util.drop_key.name}!')
            else:
                print('You chose to not fight the boss.')

class LootRoom(Room):
    def __init__(self, pos, current_floor):
        super().__init__(pos, current_floor)
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

