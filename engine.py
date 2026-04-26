from systems import Player, Item
from narrative_client import NarrativeClient

class GameEngine:
    def __init__(self, gui=None):
        self.player = Player()
        self.narrative = NarrativeClient()
        self.gui = gui
        self.current_location = "The Sunken Gates"
        self.last_choices = []
        self.sys_msg = None

    def start(self):
        self.update_game("Awaken")

    def update_game(self, action_taken):
        state = {
            "location": self.current_location,
            "inventory": [i.id for i in self.player.inventory],
            "stats": {"hp": self.player.health, "str": self.player.strength, "int": self.player.intelligence},
            "last_action": action_taken
        }
        
        story, choices = self.narrative.get_narrative(state)
        self.last_choices = choices
        if self.gui:
            self.gui.update_display(story, self.sys_msg, choices)
            self.sys_msg = None

    def handle_choice(self, idx):
        if not self.last_choices or idx >= len(self.last_choices): 
            return
            
        choice = self.last_choices[idx]
        
        # Item Requirement Check
        req = choice.get('required_item')
        if req and not self.player.has_item(req):
            self.sys_msg = f"Locked: Missing {req.replace('_', ' ')}."
            # Update display immediately without calling LLM
            self.gui.update_display(self.gui.story_text.get(1.0, "end-1c"), self.sys_msg, self.last_choices)
            return

        # Effects
        if 'effect' in choice:
            eff = choice['effect']
            if 'add_item' in eff:
                if self.player.add_item(eff['add_item']):
                    self.sys_msg = f"Found: {eff['add_item']['name']}"
            if 'stat' in eff:
                self.player.apply_effect(eff['stat'], eff['value'])

        self.current_location = choice.get('next_location', self.current_location)
        self.update_game(choice['text'])