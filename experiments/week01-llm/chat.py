from pydantic import BaseModel
from openai import OpenAI
from fastapi import FastAPI


class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="dummy",
)


def chat(prompt: str) -> str:
    response = client.chat.completions.create(
        model="mlx-community/Qwen3-8B-4bit",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content


app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat_api(request: ChatRequest):

    answer = chat(request.prompt)

    return ChatResponse(
        response=answer
    )



# uv run uvicorn experiments.week01-llm.chat:app --reload