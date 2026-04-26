"""
Game Logic Module
Handles the core game engine - processing choices, managing game state,
and determining win/loss conditions.
"""

from story_data import get_room, STORY_DATA
from player import Player


class GameEngine:
    """Core game engine that manages game state and processes player choices."""
    
    def __init__(self, player=None):
        """
        Initialize the game engine.
        
        Args:
            player (Player): The player object. Creates new if not provided.
        """
        self.player = player or Player()
        self.current_room = "start"
        self.game_over = False
        self.ending_type = None
        self.move_history = []
    
    def get_current_room_data(self):
        """
        Get the data for the current room.
        
        Returns:
            dict: The current room's data
        """
        return get_room(self.current_room)
    
    def process_choice(self, choice_index):
        """
        Process the player's choice and transition to the next room.
        
        Args:
            choice_index (int): The index of the choice (0-based)
            
        Returns:
            tuple: (success, message, next_room)
        """
        room_data = self.get_current_room_data()
        
        if not room_data:
            return False, "Error: Room not found", None
        
        choices = room_data.get("choices", [])
        
        if choice_index < 0 or choice_index >= len(choices):
            return False, "Invalid choice. Please select a valid option.", None
        
        choice = choices[choice_index]
        
        # Check if choice has a condition
        if "condition" in choice and choice["condition"]:
            condition = choice["condition"]
            
            # If condition is a callable, evaluate it
            if callable(condition):
                if not condition(self.player):
                    # Condition failed - go to alternate room if specified
                    if "condition_fail_room" in choice:
                        next_room = choice["condition_fail_room"]
                    else:
                        return False, "You don't meet the requirements for this choice.", None
            else:
                # Simple boolean condition (legacy)
                if not condition:
                    return False, "You don't meet the requirements for this choice.", None
        else:
            next_room = choice.get("next_room", self.current_room)
        
        # Apply effects from the choice
        effects = choice.get("effects", {})
        self.player.apply_effects(effects)
        
        # Track movement
        self.move_history.append(self.current_room)
        
        # Transition to next room
        self.current_room = next_room
        
        # Check if we've reached an ending
        new_room_data = self.get_current_room_data()
        if new_room_data and "ending_type" in new_room_data:
            self.game_over = True
            self.ending_type = new_room_data["ending_type"]
        
        # Check if player died
        if not self.player.is_alive():
            self.game_over = True
            self.ending_type = "death"
        
        return True, "Choice processed successfully", next_room
    
    def get_processed_description(self, room_data):
        """
        Get the room description with variables substituted.
        
        Args:
            room_data (dict): The room data
            
        Returns:
            str: The processed description
        """
        description = room_data.get("description", "")
        
        # Replace placeholders with actual values
        keys_count = self.player.count_keys()
        description = description.replace("{keys_count}", str(keys_count))
        
        return description.strip()
    
    def check_and_determine_ending(self):
        """
        Check the current room and determine if special ending conditions apply.
        This handles the final door logic based on collected keys.
        
        Returns:
            tuple: (should_transition, new_room, description)
        """
        if self.current_room == "final_door":
            keys_count = self.player.count_keys()
            
            if self.player.has_all_keys():
                # All three keys - secret ending
                return True, "all_keys_ending", "Proceeding with all keys..."
            elif keys_count > 0:
                # Partial keys
                return True, "incomplete_keys_ending", "You have some keys but not all..."
            else:
                # No keys
                return True, "no_keys_ending", "You approach the door without the necessary keys..."
        
        return False, None, None
    
    def handle_special_rooms(self):
        """
        Handle special room logic that requires custom processing.
        Returns True if special handling was applied.
        """
        if self.current_room == "final_door":
            should_transition, new_room, _ = self.check_and_determine_ending()
            if should_transition:
                self.move_history.append(self.current_room)
                self.current_room = new_room
                
                new_room_data = self.get_current_room_data()
                if new_room_data and "ending_type" in new_room_data:
                    self.game_over = True
                    self.ending_type = new_room_data["ending_type"]
                
                return True
        
        return False
    
    def get_available_choices(self):
        """
        Get the available choices for the current room.
        
        Returns:
            list: List of choice dictionaries
        """
        room_data = self.get_current_room_data()
        return room_data.get("choices", []) if room_data else []
    
    def validate_choice(self, choice_index):
        """
        Validate if a choice index is valid for the current room.
        
        Args:
            choice_index (int): The choice index to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        choices = self.get_available_choices()
        return 0 <= choice_index < len(choices)
    
    def reset_game(self):
        """Reset the game to the starting state."""
        self.player.reset()
        self.current_room = "start"
        self.game_over = False
        self.ending_type = None
        self.move_history = []
    
    def is_game_over(self):
        """
        Check if the game is over.
        
        Returns:
            bool: True if game is over, False otherwise
        """
        return self.game_over
    
    def get_game_status(self):
        """
        Get the current game status.
        
        Returns:
            dict: Status information
        """
        room_data = self.get_current_room_data()
        return {
            "current_room": self.current_room,
            "game_over": self.game_over,
            "ending_type": self.ending_type,
            "player_health": self.player.stats["health"],
            "player_alive": self.player.is_alive(),
            "inventory_count": len(self.player.inventory),
            "moves_made": len(self.move_history),
            "room_title": room_data.get("title", "Unknown") if room_data else "Unknown"
        }
    
    def get_ending_message(self):
        """
        Get the ending message based on the current ending type.
        
        Returns:
            str: The ending message
        """
        if self.ending_type == "secret_ending":
            return "🎉 SECRET ENDING DISCOVERED! You have achieved the ultimate goal!"
        elif self.ending_type == "bad_ending":
            return "💀 GAME OVER - You have met an unfortunate end."
        elif self.ending_type == "death":
            return "💀 GAME OVER - Your health has been depleted."
        elif self.ending_type == "partial_ending":
            return "⭐ PARTIAL SUCCESS - You made progress, but the true treasure remains."
        else:
            return "GAME OVER"
    
    def can_use_command(self, command):
        """
        Check if the game is in a state where commands can be processed.
        
        Args:
            command (str): The command to check
            
        Returns:
            bool: True if command can be processed
        """
        # Allow inventory and stats commands even when game is over
        if command.lower() in ["inventory", "stats", "help"]:
            return True
        
        # Disallow story choices when game is over
        if self.game_over:
            return False
        
        return True
    
    def start(self):
        """Initializes the game display with the starting room."""
        if self.gui:
            # Get the initial room data
            room_data = self.get_current_room_data()
            description = self.get_processed_description(room_data)
            choices = self.get_available_choices()
            # Update the GUI display
            self.gui.update_display(description, None, choices)
