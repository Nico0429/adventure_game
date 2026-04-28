class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Player:
    def __init__(self):
        # Initial stats
        self.health = 100
        self.strength = 10
        self.intelligence = 10
        self.wisdom = 10
        self.inventory = []

    def has_item(self, item_id):
        # We check both the object ID and the formatted name string
        search_id = item_id.lower().replace(" ", "_")
        for item in self.inventory:
            # Check if item object exists and has an ID property
            if hasattr(item, 'id') and item.id == search_id:
                return True
            # Check if item is just a string (fallback)
            if isinstance(item, str) and item.lower().replace(" ", "_") == search_id:
                return True
        return False
    

    def add_item(self, item_data):
        # Supports passing a dict or a simple string
        if isinstance(item_data, str):
            item_id = item_data.lower().replace(" ", "_")
            if not self.has_item(item_id):
                self.inventory.append(Item(item_id, item_data, f"A {item_data}."))
                return True
        elif isinstance(item_data, dict):
            if not self.has_item(item_data['id']):
                new_item = Item(item_data['id'], item_data['name'], item_data['description'])
                self.inventory.append(new_item)
                return True
        return False

    def apply_effect(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, max(0, getattr(self, stat) + value))

    def is_alive(self):
        """Check if the player's health is above zero."""
        return self.health > 0