from util import *
from map import *
from character import *
from inventory import *
from enemy import *

plrPos = (0,0)
currentRoom = 0
player = {'hp': 100, 'hp_cap': 100, 'damage': 5, 'coins': 0, 'inventory': [], 'cld': 1.25, 'healing': 1, 'healcld': 1, 'defeated': []}
stillPlaying = True

# funcs
def movePlr(direction):
    global player
    global plrPos
    global currentRoom
    if direction in directions: 
        newPos = (plrPos[0] + directions[direction][0],
                  plrPos[1] + directions[direction][1])
        if newPos in rooms[currentRoom]:
            room = rooms[currentRoom][plrPos]
            if newPos == exitPlace[currentRoom]:
                for item in player['inventory']:
                    if item['name'] == 'key':
                        currentRoom += 1
                        print('// You moved to the next room! //')
                        plrPos = (0,0)
                        input('// Enter to go to the new room! //')
                        return
                print("// You don't have the key... You can't unlock it! //")
                plrPos = newPos
                print('You are in', room['roomDesc'], 'and at coordinates', plrPos)
                return
            else:
                previousRoom = plrPos
                plrPos = newPos
                room = rooms[currentRoom][plrPos]
                clearScreen()
                drawMap(newPos, currentRoom)
                print('You are in', room['roomDesc'], 'and at coordinates', plrPos)
                roomEnemy = room.get('enemies')
                is_alive = True
                for enemy in player['defeated']:
                        if plrPos == enemy['spawnPos'] and currentRoom == enemy['room']:
                            is_alive = False
                if roomEnemy and is_alive:
                    print("========= ENEMY =========")
                    showEnemy(roomEnemy)
                    print("========= PLAYER =========")
                    showPlr(player)
                    option = input('// Do you want to fight it? (y/n)? // \n>>> ')
                    if option == 'n':
                        print('// You have returned back to the last room. //')
                        plrPos = previousRoom
                        return
                    player = fight(roomEnemy, player)
                    if player["hp"] <= 0:
                        print('// You have died. //')
                        global stillPlaying
                        stillPlaying = False
                    else:
                        defeated_enemy = {'name': roomEnemy['name'], 'spawnPos': plrPos, 'room': currentRoom}
                        player['defeated'].append(defeated_enemy)
                        player['coins'] += roomEnemy['reward']
                    plrPos = newPos
                room = rooms[currentRoom][plrPos]
                if len(room['inventory']) > 0:
                    roomItems = room['inventory']
                    for i in roomItems:
                        item = {'name': i, 'pos': plrPos}
                        if item not in player["inventory"]:
                            player["inventory"].append(item)
                            print('// You just got a', item['name'] + '! Your current inventory is:', player['inventory'])
        else:
            print('no.')

def startnew():
    clearScreen()
    input('// Enter to Start //')
    print('// Started game! //' )
    while stillPlaying:
        global currentRoom
        global plrPos
        drawMap(plrPos, currentRoom)
        movePlr(input('W, A, S, or D? \n>>>'))
        input('// Enter to Continue //')
        clearScreen()
startnew()