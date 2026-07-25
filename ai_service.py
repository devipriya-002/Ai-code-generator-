from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def generate_code(language, prompt):

    full_prompt = f"""
Generate complete {language} code.

Requirements:
- Write complete working code.
- Add comments.
- Explain the code.
- Mention Time Complexity.
- Mention Space Complexity.

User Prompt:
{prompt}
"""

    response = client.chat.completions.create(
       model="meta-llama/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return response.choices[0].message.content
