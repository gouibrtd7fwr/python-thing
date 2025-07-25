from data.floors import floor_1, floor_2
from room import EmptyRoom, MonsterRoom, StoreRoom, PortalRoom, BossRoom

class MapManager:
    def __init__(self):
        # Initialize floors dictionary with:
        # - floor_1 and floor_2 layouts
        # - empty 'rooms' dict for each floor
        # Set current floor to 1
        # Make sure the current floor's rooms are initialized
        self.floors = None
        self.current_floor = None
        pass

    def _ensure_rooms_initialized(self, floor_number):
        # If the floor's 'rooms' dict is empty:
        # - generate rooms using _generate_rooms()
        # - store them in the floor's 'rooms' field
        pass

    def _generate_rooms(self, layout):
        # For each symbol in the layout:
        # - Map it to the corresponding room type
        # - Create room instances at the given position
        # - Return the completed dict of position:room
        pass

    def display(self, player_pos, visited=None):
        # Draw the map grid (5 rows x 7 columns)
        # Use the layout of the current floor
        # Show @ for player, actual symbol for visited, ? for unexplored
        # Print a legend at the end
        pass

    def get_start_position(self):
        # Return the first position in layout where symbol is "."
        # If none found, return default (0, 0)
        pass

    def calculate_new_position(self, pos, direction):
        # Return new (x, y) position based on direction: w/a/s/d
        pass

    def is_valid_position(self, pos):
        # Return True if position exists in current floor's layout
        pass

    def get_room(self, pos):
        # Return the room object at the given position
        # Default to EmptyRoom if not found
        pass

    def switch_floor(self, floor_number):
        # Change current_floor to floor_number (if valid)
        # Ensure that floor's rooms are initialized
        pass
