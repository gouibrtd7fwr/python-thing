import os
import pickle
from map_manager import MapManager
from player import Player
from utils import clear_screen, get_input

class GameEngine:
    def __init__(self):
        # Initialize map manager and player
        # Set a variable to keep the game running
        self.map_manager = None  # Replace with actual MapManager instance
        self.player = None       # Replace with Player starting at correct position
        self.running = None      # Replace with True
        pass

    def run(self):
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
        # Call room.enter() with just_describe = False
        # This means interacting, not just viewing
        pass

    def display_ui(self):
        # Print control instructions and map legend
        pass

    def save_game(self):
        # Save map_manager and player to a file using pickle
        pass

    def load_game(self):
        # Load map_manager and player from file using pickle
        # Handle the case where the file doesn't exist
        pass
