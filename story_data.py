"""
Story Data Module
Stores all story content, room descriptions, choices, and branching paths.
"""

STORY_DATA = {
    "start": {
        "title": "The Forgotten Crypt",
        "description": """
        You stand at the entrance of an ancient crypt, half-buried in overgrown moss.
        The heavy wooden door creaks as wind passes through. A faint glow emanates from
        within, and you can hear the distant sound of dripping water echoing through stone
        corridors. You grip your worn backpack and take a deep breath.
        
        This is your last chance to find the lost artifact before the guild loses interest
        in funding your expedition.
        """,
        "choices": [
            {
                "text": "1. Enter the crypt cautiously",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {"health": 0}
            },
            {
                "text": "2. Search the entrance for supplies",
                "next_room": "search_entrance",
                "condition": None,
                "effects": {"inventory_add": "Rusty Torch"}
            }
        ]
    },
    
    "search_entrance": {
        "title": "Entrance Search",
        "description": """
        You search around the entrance and find an old torch lying on a stone ledge.
        It's rusty but still usable. Behind it, you notice a weathered sign with ancient
        text, too faded to read clearly. Taking the torch, you feel a bit more prepared.
        """,
        "choices": [
            {
                "text": "1. Enter the crypt with your torch",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "main_chamber": {
        "title": "Grand Chamber",
        "description": """
        You step into a massive circular chamber. Three archways lead in different directions:
        
        - To your LEFT: A dark corridor with strange blue symbols on the walls
        - To your RIGHT: A golden-lit chamber that appears to be a treasury
        - STRAIGHT AHEAD: A staircase spiraling downward into darkness
        
        In the center of the chamber stands a stone statue of a warrior, its eyes seeming to
        follow you. Ancient inscriptions cover the floor in patterns you don't recognize.
        """,
        "choices": [
            {
                "text": "1. Go LEFT down the dark corridor",
                "next_room": "dark_corridor",
                "condition": None,
                "effects": {}
            },
            {
                "text": "2. Go RIGHT to the treasury chamber",
                "next_room": "treasury_chamber",
                "condition": None,
                "effects": {}
            },
            {
                "text": "3. Go STRAIGHT down the spiral stairs",
                "next_room": "spiral_stairs",
                "condition": None,
                "effects": {}
            },
            {
                "text": "4. Examine the stone statue more carefully",
                "next_room": "statue_puzzle",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "dark_corridor": {
        "title": "The Dark Corridor",
        "description": """
        The blue symbols on the walls glow faintly as you venture deeper. The air grows colder,
        and you hear a low, rumbling growl echoing through the passage. You reach a junction
        where the corridor splits into two paths.
        
        On the left wall, you notice a stone door with a keyhole. A large ancient key is
        carved into the stone beside it, suggesting the key you seek might be somewhere nearby.
        
        The growling sound grows louder.
        """,
        "choices": [
            {
                "text": "1. Examine the stone door with the keyhole",
                "next_room": "locked_door_room",
                "condition": None,
                "effects": {}
            },
            {
                "text": "2. Continue forward toward the growling sound",
                "next_room": "beast_encounter",
                "condition": None,
                "effects": {}
            },
            {
                "text": "3. Turn back and explore another path",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "beast_encounter": {
        "title": "The Guardian Beast",
        "description": """
        You round a corner and come face-to-face with a massive stone golem, its eyes
        glowing with an eerie red light. It's covered in magical runes that pulse with power.
        The beast doesn't move, but its gaze locks onto you.
        
        "WHO DARES DISTURB THE CRYPT?" it bellows, the sound shaking the very foundations.
        """,
        "choices": [
            {
                "text": "1. Attack the beast with your strength",
                "next_room": "beast_fight_strong",
                "condition": lambda player: player.stats["strength"] >= 6,
                "condition_fail_room": "beast_fight_weak",
                "effects": {}
            },
            {
                "text": "2. Try to negotiate with the beast",
                "next_room": "beast_negotiate",
                "condition": None,
                "effects": {}
            },
            {
                "text": "3. Run back toward the main chamber",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "beast_fight_strong": {
        "title": "Victory Over the Beast",
        "description": """
        You charge forward with newfound confidence, your body ready for combat. The beast
        swings its massive arm, but you duck and roll beneath it. Using years of training,
        you find the weak point in its armor - the glowing rune on its chest.
        
        A single decisive strike shatters the rune, and the golem crumbles to dust with a
        final, echoing cry. Its fragments dissolve into magical energy that fades away.
        
        Behind where it stood, you find a small stone pedestal with an ornate SILVER KEY.
        """,
        "choices": [
            {
                "text": "1. Take the Silver Key and return to the main chamber",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {"inventory_add": "Silver Key", "health": -10}
            }
        ]
    },
    
    "beast_fight_weak": {
        "title": "Defeat at the Beast's Hands",
        "description": """
        You attempt to fight the beast, but you are no match for its ancient power.
        The creature's arm connects with your body, sending you flying backward. Pain
        shoots through your chest as you crash against the cold stone wall.
        
        As darkness creeps into your vision, you realize this expedition was a mistake.
        Your last thought is of the artifact, forever lost in these ruins...
        """,
        "choices": [],
        "ending_type": "bad_ending"
    },
    
    "beast_negotiate": {
        "title": "Negotiation with the Guardian",
        "description": """
        You raise your hands in a peaceful gesture. "I come seeking the artifact of power,"
        you call out respectfully. "I mean no harm to this sacred place."
        
        The beast's eyes dim slightly as it considers your words. An ancient voice speaks
        in your mind, ancient and weary: "Many have tried before. The artifact is guarded
        by trials. Prove your worthiness by obtaining the three keys scattered throughout
        the crypt. Only then may you claim it."
        
        The beast steps aside, revealing a passage deeper into the crypt.
        """,
        "choices": [
            {
                "text": "1. Thank the beast and continue deeper",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "locked_door_room": {
        "title": "The Sealed Chamber",
        "description": """
        You examine the stone door. It's carved with intricate patterns, and the keyhole
        is shaped like a small crescent moon. You don't have a key, but you notice
        something interesting...
        
        On the ground near the door, you find a COPPER KEY and a worn journal.
        The journal's last entry reads: "The Silver Key opens the true path. Seek the
        warrior's chamber for the wisdom needed."
        """,
        "choices": [
            {
                "text": "1. Take the Copper Key and the journal",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {"inventory_add": "Copper Key", "inventory_add": "Old Journal"}
            },
            {
                "text": "2. Leave and explore other areas",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "treasury_chamber": {
        "title": "The Golden Treasury",
        "description": """
        Your torch illuminates piles of glittering gold coins and jeweled treasures scattered
        across the chamber floor. It's almost overwhelming—riches beyond imagination.
        
        However, the air smells wrong. Sulfurous. As you take a step forward, you hear
        a distinct CLICK beneath your foot. The floor begins to shift!
        
        You realize with horror that this is a trap. The golden riches were bait for thieves.
        Sharp stone spikes begin rising from the floor.
        """,
        "choices": [
            {
                "text": "1. Run back immediately",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {"health": -5}
            },
            {
                "text": "2. Try to grab some treasure before escaping",
                "next_room": "treasure_grab",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "treasure_grab": {
        "title": "Greed's Price",
        "description": """
        As the spikes rise, you desperately reach for the nearest treasures, shoving them
        into your pack. One of the spikes grazes your arm, and you cry out in pain. But you
        escape with several precious gems and a golden amulet.
        
        You leap back through the archway just as the entire chamber collapses behind you,
        sealing off that section of the crypt forever.
        """,
        "choices": [
            {
                "text": "1. Return to the main chamber",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {"inventory_add": "Precious Gems", "inventory_add": "Golden Amulet", "health": -15}
            }
        ]
    },
    
    "spiral_stairs": {
        "title": "The Descent",
        "description": """
        The spiral staircase descends deep into the earth. Your torch flickers and sways
        as you move downward, the walls growing damper with moisture. The air becomes thick
        and hard to breathe.
        
        After what feels like an eternity of descending, you reach a landing. Ahead is a
        massive stone door with three circular slots arranged vertically.
        
        A glowing inscription above the door reads: "Three Keys Shall Unlock the Path of Truth."
        This must be the final chamber!
        """,
        "choices": [
            {
                "text": "1. Examine the three slots more closely",
                "next_room": "final_door",
                "condition": None,
                "effects": {}
            },
            {
                "text": "2. Continue exploring other areas first",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "final_door": {
        "title": "The Chamber of Artifacts",
        "description": """
        You stand before the three slots. Based on the journal you found, you need:
        - A Silver Key (for the warrior's wisdom)
        - A Copper Key (found in the locked chamber)
        - A Golden Key (the rarest of all)
        
        You have {keys_count} of the three keys needed.
        """,
        "choices": [
            {
                "text": "1. Check your inventory for keys",
                "next_room": "check_keys",
                "condition": None,
                "effects": {}
            },
            {
                "text": "2. Continue searching for more keys",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "check_keys": {
        "title": "Checking Your Inventory",
        "description": """
        You count the keys in your possession...
        
        Let me check your current inventory to proceed!
        """,
        "choices": [
            {
                "text": "1. Continue",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {}
            }
        ]
    },
    
    "statue_puzzle": {
        "title": "The Warrior Statue",
        "description": """
        As you examine the statue more closely, you notice something unusual. The statue's
        hand is reaching toward a small compartment in its base. You manage to open it.
        
        Inside, you find a GOLDEN KEY! The statue also bears an inscription that reads:
        "The worthy shall overcome. Strength and wisdom are the keys to victory."
        
        You feel the statue's magic acknowledging your worthiness.
        """,
        "choices": [
            {
                "text": "1. Take the Golden Key",
                "next_room": "main_chamber",
                "condition": None,
                "effects": {"inventory_add": "Golden Key", "stats_add": {"strength": 2}}
            }
        ]
    },
    
    "all_keys_ending": {
        "title": "The Secret of the Crypt",
        "description": """
        With all three keys in hand, you approach the massive stone door. Your hands tremble
        as you insert each key into its corresponding slot.
        
        The mechanism clicks into place, and the door slowly begins to open. A blinding white
        light pours from within, and as your eyes adjust, you see...
        
        THE ARTIFACT OF ETERNAL WISDOM!
        
        It hovers in the center of a pristine chamber, untouched by time. As you grasp it,
        knowledge beyond imagination flows into your mind. The artifact pulses with power,
        confirming what you've always suspected: you were destined to find this.
        
        The crypt begins to glow, and a pathway of light materializes before you, leading
        toward the exit. You've achieved what no explorer has ever accomplished before.
        
        CONGRATULATIONS! You've discovered the SECRET ENDING!
        """,
        "choices": [],
        "ending_type": "secret_ending"
    },
    
    "incomplete_keys_ending": {
        "title": "Partial Success",
        "description": """
        You insert the keys you have into the slots, but one remains empty. The door trembles
        and partially opens, but not enough to reveal the artifact chamber.
        
        A booming voice echoes through the crypt: "You are not ready. Return when you possess
        all that was lost."
        
        The door seals shut, and the stairs back to the entrance illuminate with a soft blue
        light. You've made progress, but the true treasure remains beyond your reach... for now.
        
        You exit the crypt with knowledge and determination to return stronger.
        
        ENDING: Partial Victory (Return and try again!)
        """,
        "choices": [],
        "ending_type": "partial_ending"
    },
    
    "no_keys_ending": {
        "title": "The Empty Chamber",
        "description": """
        You approach the massive door without the necessary keys. You try to force it open,
        but it won't budge. The inscriptions on the wall seem to mock you.
        
        Frustrated and defeated, you realize you've wasted your time. The artifact will remain
        hidden, protected by magic older than civilization itself.
        
        You make your way back to the entrance empty-handed, your expedition a failure.
        
        ENDING: Defeat (The artifact remains lost...)
        """,
        "choices": [],
        "ending_type": "bad_ending"
    }
}


def get_room(room_id):
    """Get a room's data by its ID."""
    return STORY_DATA.get(room_id)


def get_all_rooms():
    """Get all available rooms."""
    return STORY_DATA
