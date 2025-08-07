from data.floors import floor_1
from room import EmptyRoom, MonsterRoom, StoreRoom, PortalRoom, BossRoom, LootRoom

class MapManager:
    def __init__(self):
        # Initialize floors dictionary with:
        # - floor_1 and floor_2 layouts
        # - empty 'rooms' dict for each floor
        # Set current floor to 1
        # Make sure the current floor's rooms are initialized
        self.floors = {
            1: {"layout": floor_1, "rooms": {}}
        }
        self.current_floor = 1
        self.__ensure_rooms_initialized(self.current_floor)

    def __ensure_rooms_initialized(self, floor_number):
            floor_data = self.floors[floor_number]
            if not floor_data['rooms']:
                floor_data["rooms"] = self.__generate_rooms(floor_data["layout"])
        # If the floor's 'rooms' dict is empty:
        # - generate rooms using _generate_rooms()
        # - store them in the floor's 'rooms' field

    def __generate_rooms(self, layout):
        room_types = {
            " ": EmptyRoom,
            "E": MonsterRoom,
            "$": StoreRoom,
            "@": PortalRoom,
            "B": BossRoom,
            "!": LootRoom
        }

        rooms = {}
        for pos, symbol in layout.items():
            room_class = room_types.get(symbol, EmptyRoom)
            rooms[pos] = room_class(pos)
        print(f"Generated rooms for layout: {rooms}")
        return rooms
        # For each symbol in the layout:
        # - Map it to the corresponding room type
        # - Create room instances at the given position
        # - Return the completed dict of position:room

    def display(self, player_pos, visited=None):
        layout = self.floors[self.current_floor]["layout"]
        visited = visited or set()

        width = 7
        height = 5
        print('\n-- Floor', self.current_floor, 'Map --')
        border = "+===" * width + "+"

        for y in range(height):
            print(border)
            row = '|'
            for x in range(width):
                pos = (x, y)
                if pos == player_pos:
                    cell = "X"
                elif pos in layout:
                    if pos in visited:
                        cell = layout[pos]
                    else:
                        cell = "?"
                else:
                    cell = ""
                row += f" {cell} |"
            print(row)
        print(border)
        
        # Draw the map grid (5 rows x 7 columns)
        # Use the layout of the current floor
        # Show @ for player, actual symbol for visited, ? for unexplored
        # Print a legend at the end
        pass

    def get_start_position(self):
        layout = self.floors[self.current_floor]["layout"]
        for pos, symbol in layout.items():
            if symbol == " ":
                return pos
        return (0,0)
        # Return the first position in layout where symbol is "."
        # If none found, return default (0, 0)
        pass

    def calculate_new_position(self, pos, direction):
        x,y = pos
        if direction == 'w': y -= 1
        elif direction == 's': y += 1
        elif direction == 'a': x -= 1
        elif direction == 'd': x += 1
        return (x, y)
    
        # Return new (x, y) position based on direction: w/a/s/d
        pass

    def is_valid_position(self, pos):
        return pos in self.floors[self.current_floor]["layout"]
        # Return True if position exists in current floor's layout
        pass

    def get_room(self, pos):
        result = self.floors[self.current_floor]["rooms"].get(pos, EmptyRoom(pos))
        # print(f"Getting room at position {pos} on floor {result}")
        return result

        # Return the room object at the given position
        # Default to EmptyRoom if not found
        pass

    # def switch_floor(self, floor_number):
    #     # Change current_floor to floor_number (if valid)
    #     # Ensure that floor's rooms are initialized
    #     pass
