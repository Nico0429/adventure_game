import requests
import json
import re

class NarrativeClient:
    def __init__(self, model="qwen2.5:7b"): # Using your faster model
        self.url = "http://localhost:11434/api/generate"
        self.model = model
        self.lore = "A submerged Gothic crypt. Ancient stone, bioluminescent moss, rusted iron."

    def get_narrative(self, state):
        # Ultra-concise prompt to reduce processing time
        prompt = f"JSON ONLY. {self.lore} State: {json.dumps(state)}. Task: Write 2 paragraphs and 3 choices."
        
        try:
            # Increased timeout to 90s to ensure hardware has time to finish
            response = requests.post(
                self.url, 
                json={
                    "model": self.model, 
                    "prompt": prompt, 
                    "stream": False,
                    "options": {"num_predict": 300, "temperature": 0.7}
                }, 
                timeout=90
            )
            response.raise_for_status()
            raw = response.json().get('response', '')
            match = re.search(r'(\{.*\})', raw, re.DOTALL)
            if match:
                data = json.loads(match.group(1))
                return data.get('story', "..."), data.get('choices', [])
            return "The mists are thick.", []
        except Exception as e:
            return f"The mists deepen. (Check Ollama taskbar) Error: {e}", []