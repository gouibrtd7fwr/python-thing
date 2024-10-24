import time
def showEnemy(enemy : dict):
    print(f'// You came across a {enemy['name']}! //')
    print(f'// Stats: HP: {enemy['hp']}, DMG: {enemy['damage']} every {enemy['cld']} seconds. //')
    if (enemy.get('healing')):
        print(f'// Abilities: Healing: {enemy['healing']} every {enemy['healcld']} seconds. //')
def showPlr(plr):
    print(f'// Player stats: HP: {plr['hp']}, DMG: {plr['dmg']}, Cooldown: {plr['cld']} seconds. //')
def fight(enemy, player):