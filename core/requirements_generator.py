import requests

def generate_requirements(code_snippet):

    prompt = f"""
You are a senior software requirements engineer.

Analyze the code and create:

1. Functional Requirements
2. Non-Functional Requirements
3. User Stories
4. Edge Cases
5. Assumptions

CODE:
{code_snippet}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]