# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple RESTful API using FastAPI that supports CRUD operations for a resource (e.g., "items"). Focus on Pydantic models, routing, request validation, and running an ASGI server.

## 📝 Tasks

### 🛠️	Build the API core

#### Description
Implement a FastAPI application that provides endpoints to create, read, update, and delete items stored in memory. The app should validate requests with Pydantic models and return appropriate HTTP status codes.

#### Requirements
Completed project should:

- Define a Pydantic model for `Item` (fields: `id` (int, optional), `name` (str), `description` (optional str), `price` (float)).
- Implement endpoints:
  - `GET /items` — return list of items
  - `GET /items/{item_id}` — return a single item or `404`
  - `POST /items` — create a new item and return `201`
  - `PUT /items/{item_id}` — update an existing item or return `404`
  - `DELETE /items/{item_id}` — delete an item or return `404`
- Use in-memory storage (dictionary or list) for simplicity
- Validate input via Pydantic and return meaningful error responses
- Include example `curl` commands to exercise each endpoint
- Provide clear instructions to run the app with `uvicorn`


### 🛠️	Optional: Enhancements

#### Description
Add one or more improvements to the basic API to enhance functionality, robustness, or developer experience.

#### Requirements
Optional features may include:

- Persist data to a simple JSON file or SQLite database
- Add pagination to `GET /items`
- Add query filtering or search
- Add request/response examples and OpenAPI metadata
- Add basic authentication for write endpoints


---

## How to run (local)

Install dependencies and start the server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Example `curl`:

```bash
# Create an item
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"name":"Sample","description":"A sample item","price":9.99}'

# List items
curl http://127.0.0.1:8000/items

# Get specific item
curl http://127.0.0.1:8000/items/1
```
