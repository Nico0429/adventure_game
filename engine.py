# engine.py
import threading
from systems import Player
from narrative_client import NarrativeClient
import story_data

class GameEngine:
    def __init__(self, gui=None):
        self.player = Player()
        self.narrative = NarrativeClient()
        self.gui = gui
        self.current_room = "start"
        self.sys_msg = None

    def start(self):
        threading.Thread(target=self.update_game, args=("Awaken",), daemon=True).start()

    def handle_choice(self, idx):
        room_data = story_data.get_room(self.current_room)
        choices = room_data.get('choices', [])
        
        if idx >= len(choices): return
        choice = choices[idx]

        # 1. APPLY EFFECTS IMMEDIATELY
        effects = choice.get("effects", {})
        if "inventory_add" in effects:
            item_name = effects["inventory_add"]
            self.player.add_item(item_name) # Passing string to our new flexible add_item
            self.sys_msg = f"Picked up: {item_name}"
        
        if "health" in effects:
            self.player.apply_effect("health", effects["health"])
            
        if "stats_add" in effects:
            for stat, val in effects["stats_add"].items():
                self.player.apply_effect(stat, val)

        # 2. UPDATE LOCATION
        self.current_room = choice.get('next_room', self.current_room)
        
        # 3. START NARRATION THREAD
        threading.Thread(target=self.update_game, args=(choice['text'],), daemon=True).start()

    def update_game(self, action_taken):
        official_data = story_data.get_room(self.current_room)
        if not official_data: return

        state = {
            "base_description": official_data['description'],
            "stats": {"hp": self.player.health, "str": self.player.strength},
            "inventory": [i.name if hasattr(i, 'name') else i for i in self.player.inventory],
            "last_action": action_taken
        }
        
        choices = official_data.get('choices', [])
        if self.gui:
            self.gui.prepare_for_stream(self.sys_msg, [])
            self.gui.update_status_vitals()
            self.sys_msg = None

            for word_chunk in self.narrative.get_narrative_stream(state):
                self.gui.stream_text(word_chunk)

            self.gui.update_choices(choices)