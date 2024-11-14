import math
from enemy import *

stored = 0
e_stored = 0

def showEnemy(enemy : dict):
    print(f'// You came across a {enemy["name"]}! //')
    print(f'// Stats: HP: {enemy["hp"]}, DMG: {enemy["damage"]} every {enemy["cld"]} seconds. //')
    if (enemy.get("healing")):
        print(f'// Abilities: Healing: {enemy["healing"]} every {enemy["healcld"]} seconds. //')

def showPlr(plr):
    print(f'// Player stats: HP: {plr["hp"]}, DMG: {plr["damage"]}, Cooldown: {plr["cld"]} seconds, Coins: {plr['coins']} coins. //')

def fight(enemy, player):
    seconds = 0
    enemy_hp = enemy["hp"]
    while True:
        global stored
        global e_stored
        # Calculations and some logic
        plrDPS = player["damage"] / player["cld"]
        enemyDPS = enemy["damage"] / enemy["cld"]
        player["hp"] -= enemyDPS
        enemy_hp -= plrDPS
        if enemy_hp <= 0:
            enemy_hp = 0
        # Player healing
        if player['healing'] / player['healcld'] % 1 != 0:
            if player['hp'] < player['hp_cap']:
                healer = math.floor(player['healing'] / player['healcld'])
                remainder = (player['healing'] / player['healcld'] % 1)
                stored += remainder
                if stored >= 1:
                    player['hp'] += stored
                    stored = 0
                player['hp'] += healer
                if player['hp'] > player['hp_cap']:
                    player['hp'] = player['hp_cap']
        else:
            if player['hp'] < player['hp_cap']:
                player['hp'] += player['healing'] / player['healcld']
                if player['hp'] > player['hp_cap']:
                    player['hp'] = player['hp_cap']
        # Enemy healing
        if enemy.get('healing') != None and enemy.get('healcld') != None and enemy['healing'] / enemy['healcld'] % 1 != 0:
            if enemy_hp < enemy['hp_cap']:
                e_healer = math.floor(enemy['healing'] / enemy['healcld'])
                e_remainder = (enemy['healing'] / enemy['healcld'] % 1)
                e_stored += e_remainder
                if e_stored >= 1:
                    enemy_hp += e_stored
                    e_stored = 0
                enemy_hp += e_healer
                if enemy_hp > enemy['hp_cap']:
                    enemy_hp = enemy['hp_cap']
            else:
                if enemy_hp < enemy['hp_cap']:
                    enemy_hp += enemy['healing'] / enemy['healcld']
                    if enemy_hp > enemy['hp_cap']:
                        enemy_hp = enemy['hp_cap']
        seconds += 1
        # Printing out
        print(f"// {seconds} seconds have passed. Your HP is {math.floor(player["hp"])}. The enemy's HP is {math.floor(enemy_hp)}. //")
        if player["hp"] <= 0 or enemy_hp <= 0:
            return player
        