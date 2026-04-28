# story_data.py

STORY_DATA = {
    # ==========================================
    # ZONE 1: THE DYNAMIC STARTS
    # ==========================================
    "start": {
        "title": "The Rotting Gates",
        "description": "The main iron gates of the Forgotten Crypt loom before you, rusted shut. A foul wind howls through the bars. To your left is a crumbling graveyard; to your right, a drainage pipe leaking black water.",
        "choices": [
            {"text": "Force the gates open", "next_room": "grand_atrium", "effects": {"health": -10, "stats_add": {"strength": 1}}},
            {"text": "Explore the graveyard", "next_room": "graveyard"},
            {"text": "Crawl into the drain", "next_room": "drowned_corridor", "effects": {"health": -5}}
        ]
    },
    "start_alt_forest": {
        "title": "The Hunter's Pit",
        "description": "You fell through a layer of rotten leaves into an old spiked pit trap. You survived, but you are trapped in the catacombs just beneath the forest floor.",
        "choices": [
            {"text": "Climb out of the pit", "next_room": "grand_atrium", "effects": {"health": -15}},
            {"text": "Loot the skeleton next to you", "next_room": "start_alt_forest", "effects": {"inventory_add": "Iron Shovel"}, "hide_if_owned": "iron_shovel"},
            {"text": "Follow the root tunnels", "next_room": "overgrown_greenhouse"}
        ]
    },
    "start_alt_dungeon": {
        "title": "The Prisoner's Cell",
        "description": "You awaken in a rusted iron cage. The door has rotted off its hinges. Outside the cage is a dark hallway echoing with the sound of distant chanting.",
        "choices": [
            {"text": "Step into the hall", "next_room": "crimson_hall"},
            {"text": "Search the straw bed", "next_room": "start_alt_dungeon", "effects": {"inventory_add": "Bone Shiv"}, "hide_if_owned": "bone_shiv"}
        ]
    },

    # ==========================================
    # ZONE 2: THE UPPER WINGS (Exterior & Nature)
    # ==========================================
    "graveyard": {
        "title": "The Weeping Tombs",
        "description": "Rows of unmarked graves covered in thorny vines. One grave has fresh, loose soil, as if something—or someone—was recently buried.",
        "choices": [
            {"text": "Dig up the grave", "next_room": "graveyard", "effects": {"inventory_add": "Brass Gear"}, "required_item": "iron_shovel", "hide_if_owned": "brass_gear"},
            {"text": "Dig with bare hands", "next_room": "graveyard", "effects": {"health": -20, "inventory_add": "Brass Gear"}, "hide_if_owned": "brass_gear"},
            {"text": "Enter the Mausoleum", "next_room": "grand_atrium"}
        ]
    },
    "overgrown_greenhouse": {
        "title": "The Rotting Menagerie",
        "description": "Glass shatters beneath your boots. This was once a beautiful subterranean garden, but the plants have mutated into pale, writhing vines.",
        "choices": [
            {"text": "Hack through the vines", "next_room": "grand_atrium", "effects": {"health": -10}},
            {"text": "Use the Bone Shiv to cut carefully", "next_room": "grand_atrium", "required_item": "bone_shiv"},
            {"text": "Harvest a glowing mushroom", "next_room": "overgrown_greenhouse", "effects": {"inventory_add": "Luminous Spore"}, "hide_if_owned": "luminous_spore"}
        ]
    },

    # ==========================================
    # ZONE 3: THE CENTRAL HUB
    # ==========================================
    "grand_atrium": {
        "title": "The Grand Atrium",
        "description": "A massive, circular chamber with a broken chandelier shattered on the floor. Four paths branch out: A flooded staircase going down, a set of heavy brass elevator doors, a hallway stained with blood, and the exit to the surface.",
        "choices": [
            {"text": "Descend the flooded stairs", "next_room": "drowned_corridor"},
            {"text": "Enter the Blood Hall", "next_room": "crimson_hall"},
            {"text": "Repair the Elevator", "next_room": "the_abyss", "required_item": "brass_gear"},
            {"text": "Leave the Crypt (Coward's End)", "next_room": "ending_coward"}
        ]
    },

    # ==========================================
    # ZONE 4: THE DROWNED ARCHIVES (Water Route)
    # ==========================================
    "drowned_corridor": {
        "title": "The Flooded Archives",
        "description": "Waist-deep, freezing water ruins the ancient bookshelves here. A giant, blind water-serpent slithers through the dark water, hunting by sound.",
        "choices": [
            {"text": "Wade silently", "next_room": "sunken_chapel"},
            {"text": "Throw a rock to distract it", "next_room": "sunken_chapel"},
            {"text": "Fight the serpent", "next_room": "sunken_chapel", "effects": {"health": -40, "stats_add": {"strength": 3, "intelligence": 2}}}
        ]
    },
    "sunken_chapel": {
        "title": "The Sunken Chapel",
        "description": "An underwater shrine dedicated to a forgotten goddess. An altar rises just above the waterline, holding a pulsing artifact.",
        "choices": [
            {"text": "Take the Sun-Blessed Relic", "next_room": "sunken_chapel", "effects": {"inventory_add": "Sun-Blessed Relic"}, "hide_if_owned": "sun-blessed_relic"},
            {"text": "Return to the Atrium", "next_room": "grand_atrium"}
        ]
    },

    # ==========================================
    # ZONE 5: THE CRIMSON SANCTUM (Cultist Route)
    # ==========================================
    "crimson_hall": {
        "title": "The Hall of Flesh",
        "description": "The walls here breathe. Cultists walk these halls, their faces hidden behind masks of bone. A guard stands before a heavy iron door.",
        "choices": [
            {"text": "Attack the Guard", "next_room": "flesh_crafter_room", "effects": {"health": -30}},
            {"text": "Walk past in disguise", "next_room": "flesh_crafter_room", "required_item": "crimson_robe"},
            {"text": "Sneak into the side quarters", "next_room": "cultist_barracks"}
        ]
    },
    "cultist_barracks": {
        "title": "The Zealot's Quarters",
        "description": "Rows of uncomfortable cots. The room is empty, but a wardrobe stands half-open, a red robe hanging inside.",
        "choices": [
            {"text": "Steal the Crimson Robe", "next_room": "cultist_barracks", "effects": {"inventory_add": "Crimson Robe"}, "hide_if_owned": "crimson_robe"},
            {"text": "Search the footlockers", "next_room": "cultist_barracks", "effects": {"inventory_add": "Crescent Key"}, "hide_if_owned": "crescent_key"},
            {"text": "Return to the Hall", "next_room": "crimson_hall"}
        ]
    },
    "flesh_crafter_room": {
        "title": "The Altar of Modification",
        "description": "A horrifying laboratory where the cultists augment their bodies. The Flesh-Crafter is distracted by his gruesome work. Behind him is a locked vault door.",
        "choices": [
            {"text": "Assassinate him", "next_room": "flesh_crafter_room", "effects": {"health": -10, "inventory_add": "Brass Gear"}, "required_item": "bone_shiv", "hide_if_owned": "brass_gear"},
            {"text": "Fight him openly", "next_room": "flesh_crafter_room", "effects": {"health": -45, "inventory_add": "Brass Gear"}, "hide_if_owned": "brass_gear"},
            {"text": "Unlock Vault Door", "next_room": "treasure_vault", "required_item": "crescent_key"},
            {"text": "Flee back to Atrium", "next_room": "grand_atrium"}
        ]
    },
    "treasure_vault": {
        "title": "The Gilded Vault",
        "description": "Gold coins overflow from stone chests. In the center lies a shield emblazoned with a sun, pulsing with warmth.",
        "choices": [
            {"text": "Take the Sun Shield", "next_room": "treasure_vault", "effects": {"inventory_add": "Sun-Blessed Relic"}, "hide_if_owned": "sun-blessed_relic"},
            {"text": "Drink a health potion from a chest", "next_room": "treasure_vault", "effects": {"health": 50}, "hide_if_owned": "empty_flask"}, # Hacky way to make it a one-time use, we can add 'Empty Flask' to inv
            {"text": "Return to the Lab", "next_room": "flesh_crafter_room"}
        ]
    },

    # ==========================================
    # ZONE 6: THE ENDGAME (The Abyss)
    # ==========================================
    "the_abyss": {
        "title": "The Clockwork Descent",
        "description": "The brass gear groans as the elevator plummets into the depths of the earth. It comes to a crashing halt in absolute darkness. You hear breathing that shakes the stone.",
        "choices": [
            {"text": "Step out with the Sun Relic", "next_room": "abyssal_throne", "required_item": "sun-blessed_relic"},
            {"text": "Step out in the dark", "next_room": "abyssal_throne"},
            {"text": "Eat the Luminous Spore for light", "next_room": "abyssal_throne", "required_item": "luminous_spore"}
        ]
    },
    "abyssal_throne": {
        "title": "The Obsidian Throne",
        "description": "The Shadow King towers over you. He is made of compressed nightmares and forgotten sins. The final battle begins.",
        "choices": [
            {"text": "Banish him with Light", "next_room": "ending_victory", "required_item": "sun-blessed_relic"},
            {"text": "Harness the Spore's magic", "next_room": "ending_spore_victory", "required_item": "luminous_spore"},
            {"text": "Fight him with steel", "next_room": "ending_death", "effects": {"health": -999}}
        ]
    },

    # ==========================================
    # ENDINGS
    # ==========================================
    "ending_victory": {
        "title": "The Dawn Breaker",
        "description": "The relic flares with blinding brilliance, dissolving the Shadow King into smoke. You ride the elevator back to the surface as a hero of legend.",
        "choices": []
    },
    "ending_spore_victory": {
        "title": "The Fungal Host",
        "description": "You consume the spore. Glowing fungus bursts from your veins, granting you horrific power. You tear the King apart, but you can never leave the dark again. You are the new King.",
        "choices": []
    },
    "ending_coward": {
        "title": "A Life of Regret",
        "description": "You turn your back on the crypt and run. You survive, but the nightmares follow you for the rest of your days.",
        "choices": []
    },
    "ending_death": {
        "title": "Claimed by Shadow",
        "description": "The darkness swallows you whole. Your bones will join the thousands of others holding up this accursed place.",
        "choices": [],
        "effects": {"health": -100}
    }
}

def get_room(room_id):
    # Fallback to 'start' if a room ID is missing or mistyped
    return STORY_DATA.get(room_id, STORY_DATA.get("start"))