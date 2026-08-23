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



# Agentic AI Engineering

## 1. Python for AI Applications

* Project Structure
* Dependency Management (uv)
* Type Hints
* OOP & Design Patterns
* Async / Await
* Configuration Management
* Error Handling
* Logging
* Testing

## 2. LLM Fundamentals

* Tokens & Context Window
* Prompt Engineering
* Structured Output
* Streaming
* Local LLM Inference
* Model Parameters
* Token Management

## 3. AI Backend Development

* FastAPI
* REST API
* Dependency Injection
* Lifespan
* Async API
* Streaming Response
* API Authentication
* API Versioning

## 4. Database & Storage

* PostgreSQL
* SQLAlchemy ORM
* Transactions
* Repository Pattern
* JSONB
* Database Indexing
* Redis
* Caching
* Session State

## 5. Vector Search & RAG

* Embeddings
* pgvector
* Document Ingestion
* Code Ingestion
* Chunking
* Metadata
* Vector Search
* Semantic Search
* Hybrid Search
* Reranking
* Context Construction
* RAG Evaluation

## 6. Repository Intelligence

* Repository Indexing
* File Traversal
* File Filtering
* Language Detection
* Code Parsing
* AST
* Symbol Extraction
* Code Chunking
* Dependency Analysis
* Incremental Indexing

## 7. Tool Calling

* Tool Definition
* Tool Schema
* Function Calling
* Tool Selection
* Tool Execution
* Tool Results
* Tool Validation
* Tool Error Handling
* Tool Permissions

## 8. Agent Workflow

* Agent State
* State Management
* Agent Loop
* Planning
* Task Decomposition
* Sequential Workflow
* Parallel Workflow
* Conditional Workflow
* Retry
* Failure Recovery

## 9. MCP

* Model Context Protocol
* MCP Client
* MCP Server
* MCP Tools
* MCP Resources
* MCP Prompts
* Tool Integration

## 10. Multi-Agent Systems

* Planner Agent
* Repository Agent
* Kubernetes Agent
* Documentation Agent
* Reviewer Agent
* Agent Communication
* Agent Delegation
* Agent Coordination
* Parallel Agents
* Multi-Agent Orchestration

## 11. Agent Memory

* Short-Term Memory
* Working Memory
* Long-Term Memory
* Conversation Memory
* Retrieval Memory
* Memory Storage
* Memory Retrieval

## 12. AI Code Assistant

* Code Search
* Semantic Code Search
* Code Understanding
* Definition Search
* Reference Search
* Dependency Analysis
* Code Review
* Bug Detection
* Refactoring Suggestions

## 13. Kubernetes Intelligence

* Manifest Analysis
* Deployment Review
* Service Review
* Ingress Review
* Resource Review
* Security Review
* Configuration Review
* Kubernetes Best Practices

## 14. Documentation Generation

* README Generation
* API Documentation
* Architecture Documentation
* Code Documentation
* Deployment Documentation

## 15. AI Evaluation

* Retrieval Evaluation
* Agent Evaluation
* Tool Selection Evaluation
* Answer Evaluation
* Hallucination Detection
* Task Success Rate
* Evaluation Dataset

## 16. Observability

* Logging
* Metrics
* Distributed Tracing
* LLM Tracing
* Agent Tracing
* Tool Tracing
* Token Usage
* Latency Monitoring
* OpenTelemetry

## 17. Guardrails & Security

* Input Validation
* Output Validation
* Prompt Injection
* Tool Permissions
* Authentication
* Authorization
* Rate Limiting
* Secrets Management
* Sandbox Execution

## 18. Deployment

* Docker
* Docker Compose
* Containerization
* Kubernetes
* ConfigMap
* Secrets
* Health Checks
* Resource Limits
* HPA
* Rolling Deployment

## 19. Production AI System

* Scalability
* Reliability
* Fault Tolerance
* Async Processing
* Background Jobs
* Caching
* Cost Optimization
* Model Management
* AI System Architecture
