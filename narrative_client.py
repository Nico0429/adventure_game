import requests
import json

class NarrativeClient:
    def __init__(self, model="qwen2.5:7b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def get_narrative_stream(self, state):
        prompt = (
            "You are a dark fantasy narrator for a Gothic adventure game. "
            "Write exclusively in English. Do not use any other languages. " # Strict language constraint
            f"Use this base description: '{state.get('base_description', '')}' "
            "and rewrite it into two atmospheric, cinematic paragraphs. "
            f"The player just took the action: '{state.get('last_action', 'Awaken')}'. "
            f"Player Stats: {state.get('stats', 'N/A')}. "
            f"Inventory: {state.get('inventory', 'Empty')}. "
            "IMPORTANT: Respond ONLY with the story text in English."
        )
        
        try:
            response = requests.post(
                self.url, 
                json={
                    "model": self.model, 
                    "prompt": prompt, 
                    "stream": True,
                    "options": {
                        "temperature": 0.7, # Lower temperature = more stable language
                        "top_p": 0.9
                    }
                }, 
                stream=True,
                timeout=90
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode('utf-8'))
                    yield chunk.get('response', '')
                    if chunk.get('done'):
                        break
        except Exception as e:
            yield f"\n(The mists are too thick to see through: {e})"