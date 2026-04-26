import requests
import json

class NarrativeClient:
    def __init__(self, model="qwen2.5:7b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def get_narrative_stream(self, state):
        # We tell the AI to skip JSON for the stream to ensure speed and stability
        prompt = (
            f"You are the narrator. Use this base description: '{state['base_description']}' "
            f"and rewrite it into two atmospheric paragraphs. "
            f"Player Stats: {state['stats']}. Inventory: {state['inventory']}. "
            f"IMPORTANT: Respond with ONLY the story text. Do not use JSON."
        )
        
        try:
            response = requests.post(
                self.url, 
                json={"model": self.model, "prompt": prompt, "stream": True}, 
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