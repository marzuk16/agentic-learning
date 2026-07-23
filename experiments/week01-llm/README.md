# Goal

Local LLM-এর সাথে কথা বলা।

## শিখবে:

- MLX
- Prompt
- System Prompt
- Streaming
- JSON Output

## Files:
- app.py
- llm.py
- prompts.py
- requirements.txt
- README.md

## Deliverable

```json
POST /chat

Request

{
  "message":"Explain Spring Boot"
}

Response

{
   "response":"..."
}
```

## Day wise plan

### Day 1

- LLM কীভাবে কাজ করে
- Tokens
- Context Window s
- MLX দিয়ে local model run
- Python script লিখে prompt পাঠাও

Deliverable:
``hello_llm.py``

### Day 2

- Prompt Engineering
- System Prompt
- Temperature

``prompt_playground.py``

বিভিন্ন prompt compare করো।

### Day 3

- JSON Output
- Structured Response

একটি agent বানাও যা output দেবে:

```json
{
  "summary":"",
  "bugs":[],
  "improvements":[]
}
```

### Day 4

- Reasoning
- FastAPI

``POST /chat``

যেটা local model call করবে।

### Day 5

- Streaming Response
- LLM streaming implement করো।

### Day 6

- Project
- Local Chat API
- GitHub push