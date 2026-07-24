from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    prompt: str


client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="none",
)


def stream_chat(prompt: str):
    stream = client.chat.completions.create(
        model="mlx-community/Qwen3-8B-4bit",
        temperature=0,
        stream=True,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    for chunk in stream:
        token = chunk.choices[0].delta.content

        if token:
            yield token


@app.post("/streaming-chat")
def chat_api(request: ChatRequest):

    return StreamingResponse(
        stream_chat(request.prompt),
        media_type="text/plain",
    )