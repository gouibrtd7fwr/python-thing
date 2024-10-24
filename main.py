from util import *
from map import *
from character import *
from inventory import *

plrPos = (0,0)
currentRoom = 0
player = {'maxhp': 100, 'damage': 5, 'coins': 0, 'inventory': [], 'cld': 1.25, 'healing': 1, 'healcld': 1}
curMonster = {}

# funcs
def movePlr(direction):
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
                plrPos = newPos
                print('You are in', room['roomDesc'], 'and at coordinates', plrPos)
                room = rooms[currentRoom][plrPos]
            if len(room['inventory']) > 0:
                roomItems = room['inventory']
                for i in roomItems:
                    item = {'name': i, 'pos': plrPos}
                    if item not in player['inventory']:
                        player['inventory'].append(item)
                        print('// You just got a', item['name'] + '! Your current inventory is:', player['inventory'])
        else:
            print('no.')

def startnew():
    clearScreen()
    input('// Enter to Start //')
    print('// Started game! //' )
    while True:
        global currentRoom
        global plrPos
        drawMap(plrPos, currentRoom)
        movePlr(input('W, A, S, or D?'))
        input('// Enter to Continue //')
        clearScreen()
startnew()