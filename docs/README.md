                 User
                  |
                  |
              FastAPI
                  |
             Agent Workflow
                  |
       ┌──────────┼──────────┐
       |          |          |
   PostgreSQL   pgvector   Redis
       |          |          |
  Metadata    Knowledge   Memory
  Users       Vectors     Cache


  এখানে আগের সবকিছু একসাথে।

Architecture:

                 User
                   │
             FastAPI API
                   │
              Planner Agent
         ┌─────────┼─────────┐
         │         │         │
 Repository   Kubernetes   Documentation
   Agent        Agent         Agent
         │         │         │
         └─────────┼─────────┘
                   │
             Reviewer Agent
                   │
              Final Response

Features

- Repository Analysis
- RAG
- MCP
- Multi-Agent
- Code Review
- Kubernetes Review
- Documentation Generation
- REST API
- Docker
- Kubernetes Deployment