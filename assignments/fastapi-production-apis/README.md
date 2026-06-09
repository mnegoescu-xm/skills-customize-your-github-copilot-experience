# 📘 Assignment: API Design with FastAPI — Production-Ready Endpoints

## 🎯 Objective

Design and implement a production-oriented REST API using FastAPI. Students will focus on request validation with Pydantic, clear response models, error handling, OpenAPI metadata, basic testing, and run the app with `uvicorn`.

## 📝 Tasks

### 🛠️	Design and implement the API

#### Description
Create a FastAPI service that exposes CRUD endpoints for an `Item` resource and demonstrates production-minded practices: response models, error handling, dependency injection for shared resources, and OpenAPI documentation.

#### Requirements
Completed project should:

- Use Pydantic models for request/response validation and examples
- Return appropriate HTTP status codes and error responses
- Include descriptive operation summaries and OpenAPI metadata
- Demonstrate dependency injection (e.g., a simple repository or settings dependency)
- Include basic logging and a clear startup/shutdown lifecycle hook
- Provide `curl` examples and instructions to run with `uvicorn`


### 🛠️	Add tests and CI-friendly checks

#### Description
Provide a small automated test suite that verifies main endpoints using `pytest` and an HTTP client.

#### Requirements
Tests should:

- Validate creating, reading, updating, and deleting an item
- Assert correct status codes and response shapes
- Be runnable with `pytest`


---

## How to run (local)

Install dependencies and start the server:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Example `curl`:

```bash
# Create an item
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name":"Sample","description":"A sample item","price":9.99}'

# List items
curl http://127.0.0.1:8000/items
```