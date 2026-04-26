# ⚔️ The Forgotten Crypt - Adventure Game

A complete, text-based adventure game with a graphical interface. Explore an ancient crypt, make impactful decisions, collect items, and discover multiple branching endings.

## Features

✨ **Complete Game Experience**
- 15+ story locations with branching paths
- 3+ distinct endings (including a secret ending)
- Inventory system with item collection
- Character stats (Health, Strength, Intelligence, Wisdom)
- Impactful choices that alter the story based on what you have

🎮 **Game Mechanics**
- Dynamic story progression based on player choices
- Stat-based locks (e.g., need 6+ Strength to defeat the beast)
- Item-based gates (e.g., need a Silver Key to unlock doors)
- Combat encounters with skill checks
- Puzzle solving with key collection

🎨 **GUI Interface**
- Clean, adventure-themed design with dark colors and gold accents
- Story display area with descriptions
- Status sidebar showing health, stats, and inventory
- Choice buttons for easy interaction
- Command buttons for quick actions (Inventory, Stats, Help)

## Project Structure

```
adventure_game/
├── main.py              # GUI and game loop
├── player.py            # Player class with inventory and stats
├── game_logic.py        # Game engine and state management
├── story_data.py        # Story content and branching paths
└── README.md           # This file
```

### Component Breakdown

**`main.py`** - Entry Point & GUI
- Creates the Tkinter GUI window
- Manages the game loop and display updates
- Handles user input through button clicks
- Shows status, inventory, and story text

**`player.py`** - Character Management
- `Player` class manages:
  - Inventory (items the player collects)
  - Stats (Health, Strength, Intelligence, Wisdom)
  - Methods to add/remove items, update stats, check conditions

**`game_logic.py`** - Core Engine
- `GameEngine` class handles:
  - Processing player choices
  - Transitioning between story states
  - Checking win/loss conditions
  - Applying effects (item gains, stat changes)
  - Determining special room logic (final door puzzle)

**`story_data.py`** - Story Content
- Dictionary-based story structure
- Each "room" has:
  - Title and description
  - Available choices
  - Conditional requirements (item checks, stat thresholds)
  - Effects (what happens when you choose)
  - Ending types (for victory/defeat states)

## How to Run

### Prerequisites
- Python 3.6 or higher
- tkinter (built-in with Python)

### Running the Game

```bash
cd adventure_game
python main.py
```

That's it! The game GUI will launch.

## How to Play

1. **Read the Story**: Each location has a description of your surroundings
2. **Make Choices**: Click the choice buttons to decide what to do
3. **Check Inventory**: Click the "Inventory" button to see items you've collected
4. **View Stats**: Click the "Stats" button to see your character's abilities
5. **Restart**: Click "New Game" to start over

### Game Mechanics

**Inventory System**
- Collect items as you explore
- Some items unlock special paths or dialogue
- View items in the status sidebar

**Stats System**
- **Health**: How much damage you can take (starts at 100)
- **Strength**: Physical combat ability (affects combat outcomes)
- **Intelligence**: Problem-solving ability
- **Wisdom**: Magical and spiritual power

Some choices require minimum stats to succeed. For example:
- You need 6+ Strength to defeat the beast in combat
- Certain puzzles require items like keys

**Endings**
The game has multiple endings based on your choices:

1. **Secret Ending** 🎉 - Collect all three keys (Silver, Copper, Golden) to unlock the artifact chamber
2. **Partial Ending** ⭐ - Collect some keys but not all (incomplete victory)
3. **Bad Ending** 💀 - Fail to collect the necessary items or lose all health
4. **Death Ending** 💀 - Your health reaches 0

## Story Overview

You are an adventurer seeking the legendary "Artifact of Eternal Wisdom" hidden in The Forgotten Crypt. The crypt is guarded by ancient magic and dangerous creatures. Your success depends on:

- Finding three special keys hidden throughout the crypt
- Making smart choices about which paths to explore
- Building your character's strength through challenges
- Managing your inventory carefully

### Key Story Locations

- **Grand Chamber**: Central hub with three main paths
- **Dark Corridor**: Path with puzzles and a guardian beast
- **Treasury Chamber**: Riches, but also traps
- **Spiral Stairs**: Descent to the final chamber
- **The Guardian Beast**: Combat encounter with stat-based outcome
- **Final Chamber**: Where the artifact awaits (requires 3 keys)

## Example Playthrough

1. Start at crypt entrance
2. Search entrance, find a torch
3. Enter grand chamber
4. Go left to dark corridor
5. Encounter the guardian beast
6. With strong combat stats, defeat it and get the Silver Key
7. Return and explore statue puzzle, get the Golden Key
8. Find the Copper Key in the locked chamber
9. Reach the final door with all three keys
10. **WIN!** Unlock the secret ending

## Code Quality

- **Object-Oriented Design**: Clean separation of concerns
- **Modular Structure**: Each component has a single responsibility
- **Extensible**: Easy to add new rooms, items, and endings
- **Robust Error Handling**: Invalid inputs are handled gracefully
- **Well-Documented**: Classes and methods have clear docstrings

## Extending the Game

Want to add more content? Here's how:

### Add a New Room

In `story_data.py`:

```python
"new_room": {
    "title": "Room Title",
    "description": "Room description...",
    "choices": [
        {
            "text": "1. Do something",
            "next_room": "destination_room",
            "condition": None,  # or a lambda checking items/stats
            "effects": {"inventory_add": "item_name", "health": -5}
        }
    ]
}
```

### Add Conditional Logic

```python
"choice_with_condition": {
    "text": "2. Use the sword (requires Strength 7+)",
    "next_room": "success_room",
    "condition": lambda player: player.stats["strength"] >= 7,
    "condition_fail_room": "failure_room",
    "effects": {"health": -20}
}
```

### Add Item Checks

```python
"condition": lambda player: player.has_item("Silver Key")
```

## Game Files

All game content is self-contained in four files. No external dependencies required beyond Python's built-in `tkinter`.

---

**Enjoy your adventure! Can you find the Artifact of Eternal Wisdom?** ⚔️✨
