# Quick Start Guide - The Forgotten Crypt

## Installation & Running

### Windows Users
Simply double-click `run_game.bat` or run in command prompt:
```cmd
python main.py
```

### Mac/Linux Users
```bash
python3 main.py
```

## System Requirements
- Python 3.6 or higher
- tkinter (comes with Python on Windows and Mac)
- No external dependencies needed!

## First Time Playing - Tips

1. **You start outside a crypt** - You must decide how to enter
2. **Collect items as you explore** - Items unlock special paths
3. **Watch your health** - Some encounters will damage you
4. **Build your strength** - You'll need to be strong for some challenges
5. **Find the three keys** - Silver Key, Copper Key, and Golden Key
6. **Reach the final chamber** - With all three keys, you can claim the artifact

## Key Commands

- **Click any choice button** - Make a story decision
- **Click "Inventory"** - View items you're carrying
- **Click "Stats"** - Check your health and abilities  
- **Click "Help"** - Read game instructions
- **Click "New Game"** - Start over (erases progress)

## Story Highlights

### The Three Keys

**Golden Key** 🔑
- Found by examining the warrior statue in the main chamber
- Grants you +2 Strength for solving the puzzle

**Silver Key** 🔑
- Obtained by defeating or negotiating with the guardian beast
- Located in the dark corridor
- Different outcomes based on your strength

**Copper Key** 🔑
- Found in the sealed stone chamber
- Comes with an ancient journal that hints at the final puzzle

### The Endings

1. **SECRET ENDING** 🎉 (Best Ending)
   - Collect all 3 keys and reach the final chamber
   - Claim the Artifact of Eternal Wisdom
   - Achievement: Discover the ultimate secret!

2. **PARTIAL ENDING** ⭐ (Good Ending)
   - Reach the final chamber with only some keys
   - Partial door opens, you must return stronger
   - Can't claim the artifact yet

3. **BAD ENDING** 💀 (Fail)
   - Defeat the guardian beast without enough strength
   - Get crushed by the golem
   - Adventure ends here

4. **DEATH ENDING** 💀 (Failure)
   - Run out of health in the treasury trap
   - Health reduced too much
   - Crypt wins

## Recommended Walkthrough

For your first playthrough, try this sequence:

1. Start → Search entrance (get torch)
2. Enter crypt → Examine statue (get golden key, +2 strength)
3. Go to dark corridor → Check locked door (get copper key & journal)
4. Continue to beast → Try negotiation (avoids combat)
5. Return to chamber → Explore spiral stairs
6. Reach final door → Use all 3 keys
7. **SECRET ENDING!** 🎉

Alternative: If you're strong enough (6+ Strength):
- You can fight the beast instead of negotiating
- Defeating it also gives you the silver key directly

## Game Structure

### File Breakdown

| File | Purpose |
|------|---------|
| `main.py` | GUI and game loop |
| `player.py` | Character, inventory, and stats |
| `game_logic.py` | Game engine and choices |
| `story_data.py` | All story content |
| `demo.py` | Non-GUI demo of gameplay |
| `run_game.bat` | Windows launcher |
| `README.md` | Full documentation |

### How It All Works

1. **main.py** creates the window and controls display
2. **game_logic.py** processes your choices
3. **player.py** tracks your inventory and stats
4. **story_data.py** provides all the story content
5. Your choices change what items you have
6. Items/stats unlock new story paths
7. Multiple endings based on your decisions

## Testing Without GUI

Want to see the game in action without running the full GUI?

```bash
python demo.py
```

This shows a complete sample gameplay walkthrough in the terminal.

## Troubleshooting

**"ModuleNotFoundError: No module named 'tkinter'"**
- Windows: Reinstall Python and check "tcl/tk and IDLE" option
- Mac: Install python-tk via `brew install python-tk`
- Linux: `sudo apt install python3-tk`

**Game won't start**
- Make sure you're in the `adventure_game` folder
- Check Python is installed: `python --version`
- Try: `python main.py` (Windows) or `python3 main.py` (Mac/Linux)

**Game runs but GUI looks wrong**
- This is normal on some systems with scaling
- Try resizing the window
- Game is still fully functional

## Want to Extend the Game?

See `README.md` for instructions on:
- Adding new rooms
- Creating conditional choices
- Adding items and stat effects
- Creating new endings

## Have Fun!

The game is fully playable and ready to explore. Good luck finding the Artifact of Eternal Wisdom! 🗝️⚔️✨

For more details, see `README.md` in the game folder.
