import enemy
mapWidth = 6
mapHeight = 6

room1 = {
    (0, 0): {'roomDesc': 'Starter Room with a power box', 'inventory':[]},
    (0, 1): {'roomDesc': 'Corridor', 'inventory':[], 'enemies':enemy.enemies[0]},
    (1, 1): {'roomDesc': 'Creepy Room with a key', 'inventory':['key']},
    (1, 0): {'roomDesc': 'Graffitied Room dimly lit', 'inventory':[], 'enemies':enemy.enemies[0]},
    (2, 0): {'roomDesc': 'Dark and scary room', 'inventory':[], },
    (1, 2): {'roomDesc': 'Haunted room', 'inventory':[], 'enemies':enemy.enemies[0]},
    (2, 1): {'roomDesc': 'Portal to another dimension', 'inventory':[]},
    (2, 2): {'roomDesc': 'Sleeping room', 'inventory':[]},
    (0, 2): {'roomDesc': 'Abandoned store still with 1 person', 'inventory':[]},
    (3, 0): {'roomDesc': 'Locked door', 'inventory':[]},
    (2, 3): {'roomDesc': 'Empty room with a flashlight', 'inventory':['flashlight']},
}

room2 = {
    (0, 0): {'roomDesc': 'Starter Room 2.0', 'inventory':[]},
    (1, 0): {'roomDesc': 'Abandoned hospital room', 'inventory':[]},
    (0, 1): {'roomDesc': 'Testing room', 'inventory':[]},
    (1, 1): {'roomDesc': 'Shop', 'inventory':[]},
    (2, 0): {'roomDesc': 'Dark room with a window', 'inventory':['glass'], 'enemies':enemy.enemies[2]},
    (2, 1): {'roomDesc': 'GL1TCH', 'inventory':['GL1TCH']},
    (0, 2): {'roomDesc': 'Haunted room', 'inventory':[], 'enemies':enemy.enemies[1]},
    (1, 2): {'roomDesc': 'Hourglass', 'inventory':['glass', 'sand']},
    (0, 3): {'roomDesc': 'Rocky spring', 'inventory':[]},
    (1, 3): {'roomDesc': 'Mountain', 'inventory':['snow']},
    (0, 4): {'roomDesc': "Mini Boss's throne", 'inventory':[], 'enemies':enemy.enemies[3]},
    (1, 4): {'roomDesc': 'Blacksmith', 'inventory':[]},
    (3, 4): {'roomDesc': 'GLITCHY GATEWAY', 'inventory':[]},
    (1, 5): {'roomDesc': 'The Boss', 'inventory':[], 'enemies':enemy.enemies[4]},
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
    print("========= MAP =========")
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