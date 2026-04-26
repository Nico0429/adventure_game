"""
Player Module
Manages player character data including inventory and stats.
"""


class Player:
    """Represents the player character with inventory and stats."""
    
    def __init__(self, name="Adventurer"):
        """Initialize a new player with default stats and empty inventory."""
        self.name = name
        self.inventory = []
        self.stats = {
            "health": 100,
            "strength": 5,
            "intelligence": 5,
            "wisdom": 5
        }
    
    def add_item(self, item_name):
        """
        Add an item to the player's inventory.
        
        Args:
            item_name (str): The name of the item to add
        """
        if item_name and item_name not in self.inventory:
            self.inventory.append(item_name)
            return True
        return False
    
    def remove_item(self, item_name):
        """
        Remove an item from the player's inventory.
        
        Args:
            item_name (str): The name of the item to remove
            
        Returns:
            bool: True if item was removed, False if not found
        """
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            return True
        return False
    
    def has_item(self, item_name):
        """
        Check if player has an item in inventory.
        
        Args:
            item_name (str): The name of the item to check
            
        Returns:
            bool: True if item is in inventory, False otherwise
        """
        return item_name in self.inventory
    
    def get_inventory_display(self):
        """
        Get a formatted string showing all inventory items.
        
        Returns:
            str: Formatted inventory display
        """
        if not self.inventory:
            return "Your inventory is empty."
        
        items_list = "\n".join(f"  • {item}" for item in self.inventory)
        return f"Current Inventory ({len(self.inventory)} items):\n{items_list}"
    
    def update_stat(self, stat_name, value):
        """
        Update a player stat by adding/subtracting a value.
        
        Args:
            stat_name (str): The name of the stat to update
            value (int): The value to add (can be negative)
        """
        if stat_name in self.stats:
            self.stats[stat_name] += value
            # Ensure health doesn't go below 0
            if stat_name == "health" and self.stats[stat_name] < 0:
                self.stats[stat_name] = 0
            # Ensure stats don't go below 0
            elif self.stats[stat_name] < 0:
                self.stats[stat_name] = 0
    
    def set_stat(self, stat_name, value):
        """
        Set a player stat to a specific value.
        
        Args:
            stat_name (str): The name of the stat to set
            value (int): The value to set
        """
        if stat_name in self.stats:
            self.stats[stat_name] = max(0, value)
    
    def get_stat(self, stat_name):
        """
        Get the current value of a stat.
        
        Args:
            stat_name (str): The name of the stat to retrieve
            
        Returns:
            int: The stat value, or None if stat doesn't exist
        """
        return self.stats.get(stat_name)
    
    def get_stats_display(self):
        """
        Get a formatted string showing all player stats.
        
        Returns:
            str: Formatted stats display
        """
        stats_lines = []
        stats_lines.append(f"Character: {self.name}")
        stats_lines.append("-" * 30)
        stats_lines.append(f"Health:      {self.stats['health']}/100")
        stats_lines.append(f"Strength:    {self.stats['strength']}/10")
        stats_lines.append(f"Intelligence: {self.stats['intelligence']}/10")
        stats_lines.append(f"Wisdom:      {self.stats['wisdom']}/10")
        
        return "\n".join(stats_lines)
    
    def is_alive(self):
        """
        Check if the player is still alive.
        
        Returns:
            bool: True if health > 0, False otherwise
        """
        return self.stats["health"] > 0
    
    def apply_effects(self, effects):
        """
        Apply multiple effects to the player (inventory changes, stat changes, etc).
        
        Args:
            effects (dict): Dictionary of effects to apply.
                           Example: {
                               "inventory_add": "item_name",
                               "health": -10,
                               "strength": 2,
                               "stats_add": {"strength": 2, "health": -5}
                           }
        """
        if not effects:
            return
        
        # Handle inventory additions
        if "inventory_add" in effects:
            item = effects["inventory_add"]
            self.add_item(item)
        
        # Handle individual stat changes
        for stat_name in ["health", "strength", "intelligence", "wisdom"]:
            if stat_name in effects and effects[stat_name] != 0:
                self.update_stat(stat_name, effects[stat_name])
        
        # Handle stat additions (alternative format)
        if "stats_add" in effects:
            for stat_name, value in effects["stats_add"].items():
                self.update_stat(stat_name, value)
    
    def count_keys(self):
        """
        Count how many keys the player has (for the final puzzle).
        
        Returns:
            int: Number of keys in inventory
        """
        keys = [item for item in self.inventory if "Key" in item]
        return len(keys)
    
    def has_all_keys(self):
        """
        Check if the player has all three special keys needed for the final chamber.
        
        Returns:
            bool: True if player has Silver Key, Copper Key, and Golden Key
        """
        return (self.has_item("Silver Key") and 
                self.has_item("Copper Key") and 
                self.has_item("Golden Key"))
    
    def reset(self):
        """Reset the player to initial state."""
        self.inventory = []
        self.stats = {
            "health": 100,
            "strength": 5,
            "intelligence": 5,
            "wisdom": 5
        }
