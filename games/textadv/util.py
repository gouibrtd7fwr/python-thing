import os
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')