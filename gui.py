import tkinter as tk
from tkinter import scrolledtext, messagebox
from player import Player

class AdventureGameGUI:
    def __init__(self, root, engine):
        self.root = root
        self.engine = engine
        self.player = engine.player
        # Terraria/retro pixel-art palette
        self.palette = {
            "bg_dark": "#1a1c23",
            "panel_bg": "#2a2d37",
            "border_dark": "#181a20",
            "gold": "#fadb5f",
            "slime_green": "#7ffb4e",
            "mana_blue": "#38bdf8",
            "damage_red": "#ff4444",
            "offwhite": "#f1f5f9",
            "button_disabled": "#475569",
            "button_hover": "#23253a",
            "button_active_fg": "#7ffb4e",
            "button_active_bg": "#23253a",
        }
        self.font_main = ("Courier New", 13, "bold")
        self.font_title = ("Fixedsys", 28, "bold")
        self.font_sidebar = ("Terminal", 11, "bold")
        self.font_inv = ("Courier New", 11)
        self.font_btn = ("Courier New", 11, "bold")
        self.font_tag_sys = ("Courier New", 12, "bold")
        self.font_tag_damage = ("Courier New", 12, "bold")

        self.root.title("⚓ THE FORGOTTEN CRYPT")
        self.root.geometry("1100x800")
        self.root.configure(bg=self.palette["bg_dark"])
        self.setup_ui()
        self.engine.gui = self
        self.engine.start()

    def setup_ui(self):
        # 1. TOP: Title Label
        tk.Label(
            self.root,
            text="⚓ THE FORGOTTEN CRYPT ⚓",
            bg=self.palette["bg_dark"],
            fg=self.palette["gold"],
            font=self.font_title,
            pady=18,
            bd=4,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=4,
        ).pack(side=tk.TOP, pady=(10, 0))

        # 2. BOTTOM: Action Bar (Pack this BEFORE the container so it doesn't get pushed off-screen)
        self.action_bar = tk.Frame(
            self.root,
            bg=self.palette["bg_dark"],
            pady=18,
            bd=4,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=4,
        )
        self.action_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(0, 10))

        self.nav_frame = tk.Frame(self.action_bar, bg=self.palette["bg_dark"])
        self.nav_frame.pack(side=tk.LEFT, padx=10)

        # Red Reset Button
        self.reset_btn = tk.Button(
            self.nav_frame,
            text="RESET",
            command=self.reset_game,
            bg=self.palette["damage_red"],
            fg=self.palette["offwhite"],
            activebackground="#cc0000",
            activeforeground=self.palette["gold"],
            font=self.font_btn,
            width=10,
            bd=4,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=3,
            cursor="hand2",
        )
        self.reset_btn.pack(side=tk.LEFT, padx=2)

        self.choices_container = tk.Frame(self.action_bar, bg=self.palette["bg_dark"])
        self.choices_container.pack(side=tk.RIGHT, padx=10)

        # 3. MIDDLE: Container (Packed last so it fills exactly the space remaining)
        container = tk.Frame(
            self.root,
            bg=self.palette["bg_dark"],
            bd=4,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=4,
        )
        container.pack(fill=tk.BOTH, expand=True, padx=18, pady=10)

        self.story_text = scrolledtext.ScrolledText(
            container,
            bg=self.palette["panel_bg"],
            fg=self.palette["offwhite"],
            font=self.font_main,
            wrap=tk.WORD,
            bd=4,
            relief=tk.SOLID,
            padx=18,
            pady=18,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=4,
            insertbackground=self.palette["offwhite"],
        )
        self.story_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.story_text.config(state=tk.DISABLED)

        # Configure Text Tags
        self.story_text.tag_config("sys", foreground=self.palette["gold"], font=self.font_tag_sys)
        self.story_text.tag_config("damage", foreground=self.palette["damage_red"], font=self.font_tag_damage)

        sidebar = tk.Frame(
            container,
            bg=self.palette["panel_bg"],
            width=220,
            bd=4,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=4,
        )
        sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=(12, 0), pady=2)
        sidebar.pack_propagate(False)


        tk.Label(
            sidebar,
            text="VITALS",
            bg=self.palette["panel_bg"],
            fg=self.palette["gold"],
            font=self.font_sidebar,
            bd=3,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=3,
            pady=4,
        ).pack(pady=(10, 2), fill=tk.X, padx=4)

        # --- Retro Health Bar ---
        self.hp_text_lbl = tk.Label(
            sidebar,
            text="HP: 100/100",
            bg=self.palette["panel_bg"],
            fg=self.palette["damage_red"],
            font=self.font_sidebar,
        )
        self.hp_text_lbl.pack(pady=(2, 0), padx=8, anchor="w")

        self.hp_canvas = tk.Canvas(
                sidebar,
                width=180,
                height=22,
                bg=self.palette["panel_bg"], # Matches sidebar to hide native background
                bd=0,                        # Strips native Tkinter borders
                highlightthickness=0,        # Strips the focus ring
            )
        self.hp_canvas.pack(pady=(2, 8), padx=8, anchor="w")    

        self.vitals_lbl = tk.Label(
            sidebar,
            bg=self.palette["panel_bg"],
            fg=self.palette["offwhite"],
            font=self.font_sidebar,
            justify=tk.LEFT,
            anchor="w",
        )
        self.vitals_lbl.pack(fill=tk.X, padx=8)

        tk.Label(
            sidebar,
            text="INVENTORY",
            bg=self.palette["panel_bg"],
            fg=self.palette["gold"],
            font=self.font_sidebar,
            bd=3,
            relief=tk.RIDGE,
            highlightbackground=self.palette["border_dark"],
            highlightthickness=3,
            pady=4,
        ).pack(pady=(16, 2), fill=tk.X, padx=4)
        
        self.inv_frame = tk.Frame(sidebar, bg=self.palette["panel_bg"])
        self.inv_frame.pack(fill=tk.BOTH, expand=True, padx=6, pady=2)

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
                continue  # Skip this button, but the next button keeps its original_idx

            # 2. LOCK LOGIC
            req_id = c.get("required_item")
            has_req = self.engine.player.has_item(req_id) if req_id else True

            btn_text = c['text'].upper()
            btn_state = tk.NORMAL
            btn_fg = self.palette["mana_blue"]
            btn_bg = self.palette["panel_bg"]
            btn_active_bg = self.palette["button_hover"]
            btn_active_fg = self.palette["slime_green"]
            btn_disabled_fg = self.palette["button_disabled"]

            if not has_req:
                btn_text = f"LOCKED ({req_id.replace('_', ' ')})"
                btn_state = tk.DISABLED
                btn_fg = btn_disabled_fg
                btn_active_fg = btn_disabled_fg

            btn = tk.Button(
                self.choices_container,
                text=btn_text,
                bg=btn_bg,
                fg=btn_fg,
                font=self.font_btn,
                padx=14,
                pady=8,
                bd=4,
                relief=tk.RIDGE,
                highlightbackground=self.palette["border_dark"],
                highlightthickness=3,
                state=btn_state,
                activebackground=btn_active_bg,
                activeforeground=btn_active_fg,
                cursor="hand2",
                command=lambda idx=original_idx: self.on_click(idx)
            )
            btn.pack(side=tk.LEFT, padx=7)

            # Add hover effect (only for enabled buttons)
            if btn_state == tk.NORMAL:
                def on_enter(e, b=btn):
                    b.config(bg=self.palette["button_hover"], fg=self.palette["slime_green"])
                def on_leave(e, b=btn):
                    b.config(bg=btn_bg, fg=btn_fg)
                btn.bind("<Enter>", on_enter)
                btn.bind("<Leave>", on_leave)


    def update_status_vitals(self):
        """Syncs GUI with the current engine player and refreshes the sidebar."""
        # Ensure the GUI is looking at the NEW player object after a reset
        self.player = self.engine.player

       # --- Health Bar ---
        hp = getattr(self.player, 'health', 100)
        max_hp = 100
        hp_clamped = max(0, min(hp, max_hp))
        
        # Exact dimensions of the canvas
        c_width = 180
        c_height = 22
        fill_w = int(c_width * (hp_clamped / max_hp))
        
        self.hp_canvas.delete("all")
        
        # 1. Draw empty health background (Dark slate)
        self.hp_canvas.create_rectangle(0, 0, c_width, c_height, fill=self.palette["border_dark"], outline="")
        
        # 2. Draw filled health (Red)
        if fill_w > 0:
            self.hp_canvas.create_rectangle(0, 0, fill_w, c_height, fill=self.palette["damage_red"], outline="")
            
        # 3. Draw a crisp pixel border over the top of it all
        self.hp_canvas.create_rectangle(1, 1, c_width, c_height, outline=self.palette["offwhite"], width=2)
        
        # Update HP text
        self.hp_text_lbl.config(text=f"HP: {hp}/{max_hp}")

        # Update Vitals (no HP here)
        self.vitals_lbl.config(
            text=f"STR: {self.player.strength}\nINT: {self.player.intelligence}",
            fg=self.palette["offwhite"],
            bg=self.palette["panel_bg"],
        )

        # Clear and Redraw Inventory
        for w in self.inv_frame.winfo_children():
            w.destroy()

        for item in self.player.inventory:
            name = item.name if hasattr(item, 'name') else str(item)
            tk.Label(
                self.inv_frame,
                text=f"• {name}",
                bg=self.palette["panel_bg"],
                fg=self.palette["offwhite"],
                font=self.font_inv,
                anchor="w",
                padx=4,
            ).pack(anchor="w", padx=2, pady=1)

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
            name = item if isinstance(item, str) else getattr(item, 'name', 'Item')
            tk.Label(
                self.inv_frame,
                text=f"• {name}",
                bg=self.palette["panel_bg"],
                fg=self.palette["offwhite"],
                font=self.font_inv,
                anchor="w",
                padx=4,
            ).pack(anchor="w", padx=2, pady=1)