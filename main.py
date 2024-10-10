from util import *
from map import *
from character import *
from inventory import *

plrPos = (0,0)
currentRoom = 0
currentInventory = []

# funcs
def movePlr(direction):
    global plrPos
    global currentRoom
    if direction in directions: 
        newPos = (plrPos[0] + directions[direction][0],
                  plrPos[1] + directions[direction][1])
        if newPos in rooms[currentRoom]:
            room = rooms[currentRoom][plrPos]
            if len(room['inventory']) > 0:
                if 'Key' in room['inventory']:
                    item = {'name': 'Key', 'pos': plrPos}
                    currentInventory.append(item)
                    print('// You just got a', item['name'] + '! Your current inventory is:', currentInventory)
            if newPos == exitPlace[currentRoom]:
                currentRoom += 1
                print('// You moved to the next room! //')
                plrPos = (0,0)
                input('// Enter to go to the new room! //')
            else:
                plrPos = newPos
                print('You are in', rooms[currentRoom][plrPos]['roomDesc'], 'and at coordinates', plrPos)
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