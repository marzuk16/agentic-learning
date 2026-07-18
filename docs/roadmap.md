চমৎকার। এখন আমি তোমার জন্য "No-Fluff Learning List" দিচ্ছি। অর্থাৎ, যেগুলো পড়লেই হবে—অপ্রয়োজনীয় ২০টা course করার দরকার নেই।

Phase 1 (Week 1–2): LLM Basics
1. LangChain Academy (Free)

এখান থেকে শুধু:

LLM Basics
Prompting
Structured Output
Tool Calling

সব lesson শেষ করার দরকার নেই। Agent-related অংশে ফোকাস করো।

2. DeepLearning.AI

শুধু এই বিষয়গুলো:

Prompt Engineering
Function Calling
RAG

এক সপ্তাহের মধ্যে শেষ করা সম্ভব।

Phase 2 (Week 3–4): LangGraph ⭐

এটা সবচেয়ে গুরুত্বপূর্ণ।

পড়ার ক্রম:

StateGraph
Nodes
Edges
Conditional Edge
Memory
Human in the Loop

Goal: Documentation পড়ে নিজে ছোট graph বানানো।

Phase 3 (Week 5): MCP

শিখো:

MCP Server
MCP Client
Tools
Resources

তারপর File System Tool বানাও।

Phase 4 (Week 6): RAG

শিখো:

Embedding
Chunking
Retriever
Vector Store

তারপর:

Project:

Spring Boot Documentation Chat
Phase 5 (Week 7)

FastAPI

তুমি Backend Engineer।

FastAPI তোমার কাছে খুব সহজ লাগবে।

বানাও

POST /chat

POST /review

POST /generate-doc
Phase 6 (Week 8)

Observability

Production Agent-এ এটা খুব দরকার।

শিখো:

Prompt Logs
Token Usage
Traces
Evaluation
Phase 7

Multi Agent

Planner

↓

Researcher

↓

Coder

↓

Reviewer

↓

Answer

যে GitHub Repository-গুলো দেখবে

এগুলো পড়ো, কিন্তু copy-paste কোরো না। Flow বোঝার চেষ্টা করো।

LangGraph examples
MCP examples
Qdrant examples
FastAPI examples
YouTube Channels (কম কিন্তু ভালো)
LangChain (official)
Anthropic (MCP, agent concepts)
Microsoft Developer (AI engineering)
AI Engineer (community channel)

একসঙ্গে অনেক creator অনুসরণ না করে ২–৩টি ভালো source-এ থাকাই ভালো।

Books (ঐচ্ছিক)

যদি পড়তে ভালো লাগে:

Designing Machine Learning Systems — production thinking গড়ে তুলতে সাহায্য করবে।
Designing Data-Intensive Applications — distributed systems বোঝার জন্য এখনও দারুণ প্রাসঙ্গিক।
তোমার জন্য Challenge 🎯

আমি তোমাকে একটি ১২ সপ্তাহের Capstone দেব। প্রতি সপ্তাহে তুমি code লিখবে, আমি review করব।

Week 1 Goal:

Local MLX model দিয়ে chat API বানাও।
FastAPI দিয়ে /chat endpoint তৈরি করো।

Request:

{
  "message": "Explain Spring Boot"
}

Response:

{
  "response": "..."
}
Code GitHub-এ push করো।

এরপর repository link বা code share করলে আমি:

Architecture review করব
Clean code feedback দেব
Performance ও scalability নিয়ে পরামর্শ দেব
পরের week's task দেব

এভাবে ১২ সপ্তাহ শেষে তোমার হাতে শুধু শেখা নয়, একটি interview-ready portfolioও থাকবে।