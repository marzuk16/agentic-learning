from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="none"
)

response = client.chat.completions.create(
    model="mlx-community/Qwen3-8B-4bit",
    messages=[
        {
            "role": "user",
            "content": "Write Hello World in Python"
        }
    ],
    extra_body={
    "chat_template_kwargs": {
        "enable_thinking": False
    }
}
)

# print(response)
print(response.choices[0].message)