import tkinter as tk
from tkinter import scrolledtext, messagebox

class AdventureGameGUI:
    def __init__(self, root, engine):
        self.root = root
        self.engine = engine
        self.player = engine.player
        self.bg_dark = "#05070a"
        self.panel_bg = "#0f172a"
        self.accent_neon = "#38bdf8"
        self.accent_gold = "#fbbf24"
        self.text_offwhite = "#f1f5f9"
        
        self.root.title("⚓ THE FORGOTTEN CRYPT")
        self.root.geometry("1100x800")
        self.root.configure(bg=self.bg_dark)
        self.setup_ui()
        self.engine.gui = self
        self.engine.start()

    def setup_ui(self):
        tk.Label(self.root, text="⚓ THE FORGOTTEN CRYPT ⚓", bg=self.bg_dark, 
                 fg=self.accent_neon, font=("Georgia", 24, "bold"), pady=20).pack()

        container = tk.Frame(self.root, bg=self.bg_dark)
        container.pack(fill=tk.BOTH, expand=True, padx=20)

        self.story_text = scrolledtext.ScrolledText(container, bg=self.panel_bg, fg=self.text_offwhite,
                                                   font=("Verdana", 11), wrap=tk.WORD, bd=0, padx=15, pady=15)
        self.story_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.story_text.config(state=tk.DISABLED)
        
        # --- NEW: Configure Text Tags for Colors ---
        self.story_text.tag_config("sys", foreground=self.accent_gold, font=("Verdana", 11, "italic"))
        self.story_text.tag_config("damage", foreground="#ff4444", font=("Verdana", 11, "bold"))

        sidebar = tk.Frame(container, bg=self.panel_bg, width=200)
        sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="VITALS", bg=self.panel_bg, fg=self.accent_gold, font=("Arial", 10, "bold")).pack(pady=10)
        self.vitals_lbl = tk.Label(sidebar, bg=self.panel_bg, fg=self.text_offwhite, font=("Courier", 10), justify=tk.LEFT)
        self.vitals_lbl.pack()

        tk.Label(sidebar, text="INVENTORY", bg=self.panel_bg, fg=self.accent_gold, font=("Arial", 10, "bold")).pack(pady=10)
        self.inv_frame = tk.Frame(sidebar, bg=self.panel_bg)
        self.inv_frame.pack(fill=tk.BOTH, expand=True)

        self.action_bar = tk.Frame(self.root, bg=self.bg_dark, pady=20)
        self.action_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.nav_frame = tk.Frame(self.action_bar, bg=self.bg_dark)
        self.nav_frame.pack(side=tk.LEFT, padx=20)
        
        btn_s = {"fg": self.accent_gold, "width": 8, "font": ("Arial", 8, "bold"), "relief": tk.FLAT}
        
        # Red Reset Button
        self.reset_btn = tk.Button(self.nav_frame, text="RESET", command=self.reset_game, 
                                  **btn_s, bg="#ff4444", activebackground="#cc0000")
        self.reset_btn.pack(side=tk.LEFT, padx=2)

        self.choices_container = tk.Frame(self.action_bar, bg=self.bg_dark)
        self.choices_container.pack(side=tk.RIGHT, padx=20)

    def prepare_for_stream(self, sys_msg, damage_msg, choices):
        """Updated to handle an optional red damage message."""
        self.story_text.config(state=tk.NORMAL)
        self.story_text.delete(1.0, tk.END)
        
        # Insert standard system message (gold)
        if sys_msg: 
            self.story_text.insert(tk.END, f"» {sys_msg}\n", "sys")
            
        # Insert damage message (red)
        if damage_msg:
            self.story_text.insert(tk.END, f"🩸 {damage_msg}\n", "damage")
            
        # Add spacing before the story text starts
        if sys_msg or damage_msg:
            self.story_text.insert(tk.END, "\n")
            
        self.story_text.config(state=tk.DISABLED)
        self.update_choices(choices) 
        self.root.update()

    def stream_text(self, chunk):
        self.story_text.config(state=tk.NORMAL)
        self.story_text.insert(tk.END, chunk)
        self.story_text.see(tk.END)
        self.story_text.config(state=tk.DISABLED)
        self.root.update() # Keeps the window responsive during background thread output

    def update_choices(self, choices):
        for w in self.choices_container.winfo_children():
            w.destroy()
            
        self.reset_btn.config(state=tk.NORMAL)
        
        # We use enumerate(choices) to keep track of the REAL index in story_data
        for original_idx, c in enumerate(choices):
            # 1. HIDE LOGIC
            hide_id = c.get("hide_if_owned")
            if hide_id and self.engine.player.has_item(hide_id):
                continue # Skip this button, but the next button keeps its original_idx

            # 2. LOCK LOGIC
            req_id = c.get("required_item")
            has_req = self.engine.player.has_item(req_id) if req_id else True

            btn_text = c['text'].upper()
            btn_state = tk.NORMAL
            btn_fg = self.accent_neon

            if not has_req:
                btn_text = f"LOCKED ({req_id.replace('_', ' ')})"
                btn_state = tk.DISABLED
                btn_fg = "#475569"

            # Pass original_idx so the engine always picks the right action
            tk.Button(
                self.choices_container, 
                text=btn_text, 
                bg=self.panel_bg, 
                fg=btn_fg,
                font=("Arial", 9, "bold"), 
                padx=10, pady=5, 
                state=btn_state,
                command=lambda idx=original_idx: self.on_click(idx)
            ).pack(side=tk.LEFT, padx=5)


    def update_status_vitals(self):
        """Syncs GUI with the current engine player and refreshes the sidebar."""
        # Ensure the GUI is looking at the NEW player object after a reset
        self.player = self.engine.player
        
        # Update Vitals
        hp = getattr(self.player, 'health', 100)
        self.vitals_lbl.config(text=f"HP: {hp}\nSTR: {self.player.strength}\nINT: {self.player.intelligence}")
        
        # Clear and Redraw Inventory
        for w in self.inv_frame.winfo_children():
            w.destroy()
            
        for item in self.player.inventory:
            name = item.name if hasattr(item, 'name') else str(item)
            tk.Label(self.inv_frame, text=f"• {name}", bg=self.panel_bg, fg="white").pack(anchor="w", padx=5)

    def on_click(self, idx):
        # LOCKOUT: Disable all buttons to prevent race conditions
        for child in self.choices_container.winfo_children():
            if isinstance(child, tk.Button):
                child.config(state=tk.DISABLED)
        self.reset_btn.config(state=tk.DISABLED)

        self.story_text.config(state=tk.NORMAL)
        self.story_text.insert(tk.END, "\n\n(Consulting the mists...)", "sys")
        self.story_text.config(state=tk.DISABLED)
        self.root.update()
        self.engine.handle_choice(idx)

    def reset_game(self):
        if messagebox.askyesno("Reset", "Restart the journey?"):
            # Use the engine's built-in reset logic to clear everything properly
            if hasattr(self.engine, 'reset_logic'):
                self.engine.reset_logic()
            else:
                # Fallback if reset_logic isn't defined
                self.engine.player = Player()
                self.engine.current_room = "start"
                self.engine.sys_msg = None
                self.engine.start()

    def update_inventory_display(self):
        """Refreshes the inventory sidebar."""
        for w in self.inv_frame.winfo_children(): 
            w.destroy()
        for item in self.player.inventory: 
            # Check if item is a string or object based on your player.py
            name = item if isinstance(item, str) else getattr(item, 'name', 'Item')
            tk.Label(self.inv_frame, text=f"• {name}", 
                    bg=self.panel_bg, fg="white").pack(anchor="w", padx=5)