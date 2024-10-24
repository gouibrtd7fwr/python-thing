import enemy
mapWidth = 6
mapHeight = 6

room1 = {
    (0, 0): {'roomDesc': 'Starter Room with a power box', 'inventory':[]},
    (0, 1): {'roomDesc': 'Corridor', 'inventory':[]},
    (1, 1): {'roomDesc': 'Creepy Room with a key', 'inventory':['key']},
    (1, 0): {'roomDesc': 'Graffitied Room dimly lit', 'inventory':[]},
    (2, 0): {'roomDesc': 'Dark and scary room', 'inventory':[], 'enemies':enemy.enemies[0]},
    (1, 2): {'roomDesc': 'Haunted room', 'inventory':[], 'enemies':enemy.enemies[0]},
    (2, 1): {'roomDesc': 'Portal to another dimension', 'inventory':[]},
    (2, 2): {'roomDesc': 'Sleeping room', 'inventory':[]},
    (0, 2): {'roomDesc': 'Abandoned store still with 1 person', 'inventory':[]},
    (3, 0): {'roomDesc': 'Locked door', 'inventory':[]},
    (2, 3): {'roomDesc': 'Empty room with a flashlight', 'inventory':['flashlight']},
}

room2 = {
    (0, 0): {'roomDesc': 'Starter Room 2.0', 'inventory':[]},
}

rooms = [room1, room2]
exitPlace = [(3,0), (4,3)]
# directions
directions = {
    's': (0,1),
    'w': (0,-1),
    'd': (1,0),
    'a': (-1,0)
}

def drawMap(plrPos, currentRoom):
    for y in range(mapHeight):
        for x in range(mapWidth):
            if (x,y) == plrPos:
                print('X', end=" ")
            elif (x,y) in rooms[currentRoom]:
                print('O', end=" ")
            else:
                print('.', end=" ")
        print()
    print("\n")