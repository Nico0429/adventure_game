"""
Main Module - Entry Point.
"""
import tkinter as tk
import sys

try:
    from engine import GameEngine # Use the local logic, not the AI client
    from gui import AdventureGameGUI
except ImportError as e:
    print(f"Error: Missing game files! {e}")
    sys.exit(1)

def main():
    root = tk.Tk()
    engine = GameEngine()
    app = AdventureGameGUI(root, engine)


    root.mainloop()

if __name__ == "__main__":
    main()