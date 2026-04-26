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

    def has_item(self, item_id):
        return any(item.id == item_id for item in self.inventory)

    def add_item(self, item_data):
        if not self.has_item(item_data['id']):
            new_item = Item(item_data['id'], item_data['name'], item_data['description'])
            self.inventory.append(new_item)
            return True
        return False

    def remove_item(self, item_id):
        self.inventory = [i for i in self.inventory if i.id != item_id]

    def apply_effect(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, max(0, getattr(self, stat) + value))