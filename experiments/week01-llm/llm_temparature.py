from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="none"
)


prompt = [
    {
        "role": "user",
        "content": "Explain Docker"
    }
]

# Temperature শুধু token selection-এর randomness নিয়ন্ত্রণ করে।
# Model-এর intelligence বা capability একই থাকে।
# range 0.0 - 1.5+

response = client.chat.completions.create(
    model="mlx-community/Qwen3-8B-4bit",
    temperature=0.7,
    messages=prompt
)

print(response.choices[0].message.content)