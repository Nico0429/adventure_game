import threading
import random
import time
from systems import Player
from narrative_client import NarrativeClient
import story_data

class GameEngine:
    def __init__(self, gui=None):
        self.player = Player()
        self.narrative = NarrativeClient()
        self.gui = gui
        self.damage_msg = None
        # Dynamic Start Scenario
        start_options = ["start", "start_alt_forest", "start_alt_dungeon"]
        self.current_room = random.choice([opt for opt in start_options if opt in story_data.STORY_DATA])
        self.sys_msg = None

    def start(self):
        threading.Thread(target=self.update_game, args=("Awaken",), daemon=True).start()

    def handle_choice(self, idx):
        room_data = story_data.STORY_DATA.get(self.current_room)
        choices = room_data.get('choices', [])
        if idx >= len(choices): return
        choice = choices[idx]

        # Reset messages at the start of choice handling
        self.sys_msg = None 
        self.damage_msg = None # NEW

        effects = choice.get("effects", {})
        if "inventory_add" in effects:
            item_name = effects["inventory_add"]
            if self.player.add_item(item_name):
                self.sys_msg = f"Found: {item_name}"
        
        if "health" in effects:
            val = effects["health"]
            self.player.apply_effect("health", val)
            # NEW: Check if damage was taken
            if val < 0:
                self.damage_msg = f"YOU TOOK {abs(val)} DAMAGE!"
            elif val > 0:
                # Optional: Add a healing note to the system message
                heal_text = f"Recovered {val} HP"
                self.sys_msg = f"{self.sys_msg} | {heal_text}" if self.sys_msg else heal_text
            
        if "stats_add" in effects:
            for stat, val in effects["stats_add"].items():
                self.player.apply_effect(stat, val)

        self.current_room = choice.get('next_room', self.current_room)
        threading.Thread(target=self.update_game, args=(choice['text'],), daemon=True).start()

    def update_game(self, action_taken):
        # Death Check
        if not self.player.is_alive():
            self.gui.prepare_for_stream("💀 YOU HAVE DIED", [])
            for chunk in self.narrative.get_narrative_stream({"base_description": "The adventurer collapses, life fading as the crypt claims another soul.", "stats": {}, "inventory": []}):
                self.gui.stream_text(chunk)
            time.sleep(3) # Let them read their fate
            self.reset_logic()
            return

        official_data = story_data.STORY_DATA.get(self.current_room)
        state = {
            "location": official_data.get('title', 'Unknown'),
            "base_description": official_data.get('description', ''),
            "stats": {"hp": self.player.health, "str": self.player.strength, "int": self.player.intelligence},
            "inventory": [getattr(i, 'id', i) for i in self.player.inventory],
            "last_action": action_taken
        }
        
        choices = official_data.get('choices', [])
        
        if self.gui:
            # Capture both messages and clear them from engine
            current_sys = self.sys_msg
            current_dmg = self.damage_msg
            self.sys_msg = None
            self.damage_msg = None
            
            # Pass BOTH to prepare_for_stream
            self.gui.prepare_for_stream(current_sys, current_dmg, [])
            self.gui.update_status_vitals()
            
            for word_chunk in self.narrative.get_narrative_stream(state):
                self.gui.stream_text(word_chunk)
            
            self.gui.update_choices(choices)

    def reset_logic(self):
        """Wipes player data and picks a random starting scenario."""
        self.player = Player()
        self.sys_msg = "A new journey begins..."
        self.damage_msg = None  # <--- NEW: Wipe it clean on reset
        
        # Define possible starting IDs from your story_data.py
        start_nodes = ["start", "start_alt_forest", "start_alt_dungeon"]
        valid_starts = [node for node in start_nodes if node in story_data.STORY_DATA]
        self.current_room = random.choice(valid_starts) if valid_starts else "start"
        
        # If the game is already running, refresh the UI
        if self.gui:
            self.gui.player = self.player 
            self.start()

    def handle_death(self):
        """Narrates death and then resets the game."""
        if self.gui:
            # Update to match new signature (sys_msg, damage_msg, choices)
            self.gui.prepare_for_stream("💀 YOU HAVE PERISHED", "HP REACHED 0", [])
            
            death_state = {
                "base_description": "Your strength fails you. The darkness of the crypt closes in, claiming your soul forever.",
                "stats": {"hp": 0, "str": self.player.strength},
                "inventory": [getattr(i, 'name', i) for i in self.player.inventory]
            }

            for chunk in self.narrative.get_narrative_stream(death_state):
                self.gui.stream_text(chunk)
            
            time.sleep(3) 
            self.reset_logic()