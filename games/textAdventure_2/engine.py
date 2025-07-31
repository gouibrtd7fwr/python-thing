import os
import pickle
from map_manager import MapManager
from player import Player
from utils import clear_screen, get_input

class GameEngine:
    def __init__(self):
        # Initialize map manager and player
        # Set a variable to keep the game running
        self.map_manager = MapManager()  # Replace with actual MapManager instance
        self.player = Player(self.map_manager.get_start_position())       # Replace with Player starting at correct position
        self.running = True      # Replace with True
        pass

    def run(self):
        while self.running == True:
            clear_screen()
            current_pos = self.map_manager.get_room(self.player.position)
            self.map_manager.display(self.player.position, self.player.visited_rooms)
            print('\nRoom description:', current_pos.description)
            self.display_ui()
            command = get_input("Enter command: w/a/s/d: Move, e: Interact, o: Save, i: Load, l: Stats, p: Inventory, q: Quit\n")
            if command in ['w','a','s','d']:
                self.move_player(command)
            elif command == 'e':
                self.interact_room()
            elif command == 'o':
                self.save_game()
            elif command == 'i':
                self.load_game()
            elif command == 'l':
                self.player.show_stats()
            elif command == 'p':
                self.player.show_inventory()
            elif command == 'q':
                print('Thanks for playing!')
                self.running = False
            else:
                print('Command not found.')
                command = get_input("Enter command: w/a/s/d: Move, e: Interact, o: Save, i: Load, l: Stats, p: Inventory, q: Quit\n")
        # Main game loop
        # - Clear screen
        # - Get current room
        # - Display map and room description
        # - Show UI
        # - Handle player input
        #   (move, interact, inventory, stats, save, load, quit)
        pass

    def move_player(self, direction):
        # Calculate new position based on direction (w/a/s/d)
        # If valid:
        #   - Update player position
        #   - Describe the room (not interact)
        #   - Remove temporary effects
        # Else:
        #   - Tell the player they can't move there
        pass

    def interact_room(self, room):
        room.enter(self.player, self.map_manager, False)
        # Call room.enter() with just_describe = False
        # This means interacting, not just viewing
        pass

    def display_ui(self):
        print('\n--Controls--')
        print('w/a/s/d: Move, e: Interact, o: Save, i: Load, l: Stats, p: Inventory')
        print('\nLegend: O: You, x: Empty, E: Enemy, $: Shop, @: Portal, !: Loot')
        pass

    def save_game(self):
        # Save map_manager and player to a file using pickle
        pass

    def load_game(self):
        # Load map_manager and player from file using pickle
        # Handle the case where the file doesn't exist
        pass
