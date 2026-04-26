"""
Demo Script - Text-Based Walkthrough
Shows how the game logic works without the GUI.
"""

from game_logic import GameEngine
from player import Player


def print_separator(title=""):
    """Print a formatted separator."""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    else:
        print(f"\n{'-'*60}\n")


def demo_game():
    """Run a demonstration of the game logic."""
    
    print("\n" + "="*60)
    print("  THE FORGOTTEN CRYPT - Game Logic Demo")
    print("="*60)
    print("\nThis demo shows the game working without the GUI.")
    print("It demonstrates key features like inventory, stats, and choices.\n")
    
    # Create player and game
    player = Player("Demo Adventurer")
    engine = GameEngine(player)
    
    print(f"Player: {player.name}")
    print(f"Initial Health: {player.stats['health']}")
    print(f"Initial Strength: {player.stats['strength']}\n")
    
    # Get starting room
    print_separator("Starting Location")
    room = engine.get_current_room_data()
    print(f"Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    
    print("Available Choices:")
    for i, choice in enumerate(room['choices']):
        print(f"  {choice['text']}")
    
    # Simulate first choice
    print_separator("Choice 1: Search the entrance")
    engine.process_choice(1)
    room = engine.get_current_room_data()
    print(f"New Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    print(f"Items in inventory: {player.inventory}\n")
    
    # Simulate entering main chamber
    print_separator("Choice 2: Enter the crypt")
    engine.process_choice(0)
    room = engine.get_current_room_data()
    print(f"New Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    
    print("Available Choices:")
    for i, choice in enumerate(room['choices']):
        print(f"  {i+1}. {choice['text']}\n")
    
    # Go to statue and find golden key
    print_separator("Choice 3: Examine the statue")
    engine.process_choice(3)
    room = engine.get_current_room_data()
    print(f"New Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    print(f"Items gained: {player.inventory}\n")
    
    # Return to main chamber
    print_separator("Back to main chamber")
    engine.process_choice(0)
    room = engine.get_current_room_data()
    print(f"Room: {room['title']}")
    
    # Go to dark corridor
    print_separator("Exploring the dark corridor")
    engine.process_choice(0)
    room = engine.get_current_room_data()
    print(f"Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    
    # Encounter the beast
    print_separator("Encountering the Guardian Beast")
    engine.process_choice(0)
    room = engine.get_current_room_data()
    print(f"Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    
    # Try negotiation
    print_separator("Negotiating with the beast")
    engine.process_choice(1)
    room = engine.get_current_room_data()
    print(f"Room: {room['title']}")
    print(f"Description:\n{room['description']}\n")
    
    # Demo inventory and stats system
    print_separator("Checking Player Status")
    print("CHARACTER STATS:")
    print(player.get_stats_display())
    print("\n" + "-"*40)
    print("CHARACTER INVENTORY:")
    print(player.get_inventory_display())
    
    # Show game status
    print_separator("Game Status")
    status = engine.get_game_status()
    print(f"Current Room: {status['room_title']}")
    print(f"Player Health: {status['player_health']}/100")
    print(f"Inventory Count: {status['inventory_count']}")
    print(f"Moves Made: {status['moves_made']}")
    print(f"Game Over: {status['game_over']}")
    
    print("\n" + "="*60)
    print("  Demo Complete!")
    print("="*60)
    print("\nTo play the full game with the GUI, run:")
    print("  python main.py")
    print("\nKey Features Demonstrated:")
    print("  ✓ Story progression and room transitions")
    print("  ✓ Choice-based gameplay")
    print("  ✓ Inventory management (collecting items)")
    print("  ✓ Stats tracking (health, strength, etc.)")
    print("  ✓ Multiple choice options")
    print("  ✓ Game state management")
    print("  ✓ Effect application (stat changes, items)")
    print("\n")


if __name__ == "__main__":
    demo_game()
