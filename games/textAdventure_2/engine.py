import os
import pickle
from map_manager import MapManager
from player import Player
from utils import clear_screen, get_input

SAVE_DIR = "saves"      
NUM_SLOTS = 3         
class GameEngine:
    def __init__(self):
        self.map_manager = None
        self.player = None
        self.running = False

        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)

    def start(self):
        """Show main menu before entering the main loop."""
        while True:
            clear_screen()
            print("====== WELCOME TO THE ADVENTURE GAME ======")
            print("1. New Game")
            print("2. Load Game")
            print("3. Quit")
            print("==========================================")

            choice = get_input("Choose an option (1-3): ")

            if choice == "1":
                self.new_game()
                self.run()
            elif choice == "2":
                if self.load_menu():
                    self.run()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
                input("Press Enter to continue...")


    def new_game(self):
        """Start a new game with fresh map and player."""
        self.map_manager = MapManager()
        self.player = Player(self.map_manager.get_start_position())
        self.running = True
        self.player.add_visited_rooms(self.map_manager)

    def load_menu(self):
        """Let the player choose a slot to load."""
        clear_screen()
        print("====== LOAD GAME ======")
        slots = self.list_save_slots()

        for idx, slot_name in enumerate(slots, start=1):
            exists = os.path.exists(slot_name)
            status = "🟢 Occupied" if exists else "⚪ Empty"
            print(f"{idx}. Slot {idx} - {status}")

        print("0. Back")
        print("=======================")

        choice = get_input(f"Choose a slot to load (1-{NUM_SLOTS}) or 0 to cancel: ")

        if choice == "0":
            return False

        try:
            slot_num = int(choice)
            if 1 <= slot_num <= NUM_SLOTS:
                return self.load_game(slot_num)
            else:
                print("Invalid slot number!")
        except ValueError:
            print("Invalid input!")
        input("Press Enter to continue...")
        return False

    def run(self):
        while self.running:
            clear_screen()
            current_pos = self.map_manager.get_room(self.player.position)
            self.map_manager.display(self.player.position, self.player.visited_rooms)
            print('\nRoom description:', current_pos.description)
            self.display_ui()

            command = get_input("Enter command: w/a/s/d: Move, e: Interact, o: Save, i: Load, l: Stats, p: Inventory, q: Quit\n")
            
            if command in ['w','a','s','d']:
                self.move_player(command)
            elif command == 'e':
                self.interact_room(current_pos)
            elif command == 'o':
                self.save_menu()
            elif command == 'i':
                if self.load_menu():
                    continue
            elif command == 'l':
                self.player.show_stats()
            elif command == 'p':
                self.player.show_inventory()
                input('')
            elif command == 'q':
                print('Thanks for playing!')
                self.running = False
            else:
                print('Command not found.')
                input("Press Enter to continue...")

    def move_player(self, direction):
        pos = self.map_manager.calculate_new_position(self.player.position, direction)
        if self.map_manager.is_valid_position(pos):
            self.player.update_position(pos, self.map_manager)
            room_type = self.map_manager.get_room(self.player.position)

            room_type.enter(self.player, self.map_manager, just_describe=True)
        else:
            print("You can't move there!")
            input("Press Enter to continue...")
  
    def interact_room(self, room):
        room.enter(self.player, self.map_manager, False)

    def display_ui(self):
        print('\n--Controls--')
        print('w/a/s/d: Move, e: Interact, o: Save, i: Load, l: Stats, p: Inventory')
        print('\nLegend: O: You, x: Empty, E: Enemy, $: Shop, @: Portal, !: Loot')


    def list_save_slots(self):
        """Return list of save slot file paths."""
        return [os.path.join(SAVE_DIR, f"slot_{i}.pkl") for i in range(1, NUM_SLOTS + 1)]

    def save_menu(self):
        """Let player choose which slot to save to."""
        clear_screen()
        print("====== SAVE GAME ======")
        slots = self.list_save_slots()

        for idx, slot_name in enumerate(slots, start=1):
            exists = os.path.exists(slot_name)
            status = "🟢 Occupied" if exists else "⚪ Empty"
            print(f"{idx}. Slot {idx} - {status}")

        print("0. Cancel")
        print("=======================")

        choice = get_input(f"Choose a slot to save (1-{NUM_SLOTS}) or 0 to cancel: ")

        if choice == "0":
            return

        try:
            slot_num = int(choice)
            if 1 <= slot_num <= NUM_SLOTS:
                self.save_game(slot_num)
            else:
                print("Invalid slot number!")
        except ValueError:
            print("Invalid input!")
        input("Press Enter to continue...")

    def save_game(self, slot_num):
        """Save current game to chosen slot."""
        if not self.player or not self.map_manager:
            print("No game in progress to save!")
            return

        slot_path = os.path.join(SAVE_DIR, f"slot_{slot_num}.pkl")
        data = {
            "player": self.player,
            "map_manager": self.map_manager
        }

        try:
            with open(slot_path, "wb") as f:
                pickle.dump(data, f)
            print(f"Game saved to Slot {slot_num}!")
        except Exception as e:
            print(f"Error saving game: {e}")

    def load_game(self, slot_num):
        """Load a saved game from a chosen slot."""
        slot_path = os.path.join(SAVE_DIR, f"slot_{slot_num}.pkl")

        if not os.path.exists(slot_path):
            print("That slot is empty!")
            return False

        try:
            with open(slot_path, "rb") as f:
                data = pickle.load(f)
                self.player = data["player"]
                self.map_manager = data["map_manager"]
                self.running = True
            print(f"Game loaded from Slot {slot_num}!")
            return True
        except Exception as e:
            print(f"Error loading game: {e}")
            return False
