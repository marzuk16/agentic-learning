from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="none"
)


without_system_prompt = [
    {
        "role": "user",
        "content": "Explain Docker"
    }
]

with_system_prompt = [
    {
        "role": "system",
        "content": """
You are a senior backend architect.

Always:
- Explain simply
- Give Spring Boot examples
- Use Markdown
- End with interview questions
"""
    },
    {
        "role": "user",
        "content": "Explain Docker"
    }
]

without_system_prompt_response = client.chat.completions.create(
    model="mlx-community/Qwen3-8B-4bit",
    messages=without_system_prompt
)

print(without_system_prompt_response.choices[0].message.content)

print("\n-----------------------------------------------------\n")

with_system_prompt_response = client.chat.completions.create(
    model="mlx-community/Qwen3-8B-4bit",
    messages=with_system_prompt
)

print(with_system_prompt_response.choices[0].message.content)