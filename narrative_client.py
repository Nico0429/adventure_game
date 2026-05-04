import requests
import json
import time

class NarrativeClient:
    def __init__(self, model="qwen2.5:7b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def get_narrative_stream(self, state):
        base_text = state.get('base_description', 'You stand in a dark, empty room.')
        
        prompt = (
            "You are a dark fantasy narrator for a Gothic adventure game. Write exclusively in English. "
            f"Use this base description: '{base_text}' and rewrite it into two atmospheric paragraphs. "
            f"The player just took the action: '{state.get('last_action', 'Awaken')}'. "
            f"Player Stats: {state.get('stats', 'N/A')}. Inventory: {state.get('inventory', 'Empty')}. "
            "IMPORTANT: Respond ONLY with the story text in English."
        )
        
        try:
            # Short timeout so the game doesn't hang forever if Ollama is off
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
                        
        except requests.exceptions.RequestException:
            # THE FALLBACK: If Ollama isn't running, just stream the base description nicely
            fallback_msg = "(AI Offline. Falling back to archives...)\n\n"
            for word in fallback_msg.split():
                yield word + " "
                time.sleep(0.05)
                
            for word in base_text.split():
                yield word + " "
                time.sleep(0.03)