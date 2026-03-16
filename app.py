import ollama

class AIAgent:
    def __init__(self, model="deepseek-coder"):
        self.model = model
    
    def execute(self, task):
        response = ollama.generate(model=self.model, prompt=task)
        return response['response']

# Usage
agent = AIAgent()
result = agent.execute("Explain AI automation")
print(result)
