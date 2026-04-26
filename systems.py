# systems.py

class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Player:
    def __init__(self):
        self.health = 100
        self.strength = 10
        self.intelligence = 10
        self.wisdom = 10
        self.inventory = []

    def get_inventory_list(self):
        return self.inventory

    def has_item(self, item_name):
        # Check if the name exists in our list of item objects or strings
        return any(
            (isinstance(i, str) and i == item_name) or 
            (isinstance(i, Item) and i.name == item_name) 
            for i in self.inventory
        )

    def add_item(self, item_data):
        """
        Modified to handle both dictionary data and simple strings.
        """
        # If it's a dictionary (older logic)
        if isinstance(item_data, dict):
            name = item_data.get('name', 'Unknown Item')
            item_id = item_data.get('id', name.lower())
            desc = item_data.get('description', '')
        else:
            # If it's just a string (new logic)
            name = item_data
            item_id = item_data.lower().replace(" ", "_")
            desc = f"A {name}."

        if not self.has_item(name):
            new_item = Item(item_id, name, desc)
            self.inventory.append(new_item)
            return True
        return False

    def remove_item(self, item_name):
        self.inventory = [i for i in self.inventory if (isinstance(i, str) and i != item_name) or (isinstance(i, Item) and i.name != item_name)]

    def apply_effect(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, max(0, getattr(self, stat) + value))