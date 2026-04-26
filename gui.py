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
        
        btn_s = {"bg": self.panel_bg, "fg": self.accent_gold, "width": 8, "font": ("Arial", 8, "bold"), "relief": tk.FLAT}
        tk.Button(self.nav_frame, text="INV", command=self.show_inventory, **btn_s).pack(side=tk.LEFT, padx=2)
        tk.Button(self.nav_frame, text="RESET", command=self.reset_game, **btn_s).pack(side=tk.LEFT, padx=2)

        self.choices_container = tk.Frame(self.action_bar, bg=self.bg_dark)
        self.choices_container.pack(side=tk.RIGHT, padx=20)

    def update_display(self, story, sys_msg, choices):
        self.story_text.config(state=tk.NORMAL)
        self.story_text.delete(1.0, tk.END)
        if sys_msg: self.story_text.insert(tk.END, f"» {sys_msg}\n\n", "sys")
        self.story_text.insert(tk.END, story)
        self.story_text.tag_config("sys", foreground=self.accent_gold)
        self.story_text.config(state=tk.DISABLED)

        self.vitals_lbl.config(text=f"HP: {self.player.health}\nSTR: {self.player.strength}\nINT: {self.player.intelligence}")
        for w in self.inv_frame.winfo_children(): w.destroy()
        for i in self.player.inventory: tk.Label(self.inv_frame, text=f"• {i.name}", bg=self.panel_bg, fg="white").pack(anchor="w", padx=5)

        for w in self.choices_container.winfo_children(): w.destroy()
        for i, c in enumerate(choices):
            tk.Button(self.choices_container, text=c['text'].upper(), bg=self.panel_bg, fg=self.accent_neon,
                      font=("Arial", 9, "bold"), padx=10, pady=5, command=lambda idx=i: self.on_click(idx)).pack(side=tk.LEFT, padx=5)

    def on_click(self, idx):
        self.story_text.config(state=tk.NORMAL)
        self.story_text.insert(tk.END, "\n\n(Consulting the mists...)", "sys")
        self.story_text.config(state=tk.DISABLED)
        self.root.update_idletasks()
        self.engine.handle_choice(idx)

    def show_inventory(self):
        inv = [i.name for i in self.player.inventory]
        messagebox.showinfo("Inventory", "\n".join(inv) if inv else "Empty.")

    def reset_game(self):
        if messagebox.askyesno("Reset", "Restart?"):
            self.engine.__init__()
            self.engine.gui = self
            self.engine.start()