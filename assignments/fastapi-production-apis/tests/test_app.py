import pytest
from httpx import AsyncClient
from app import app

@pytest.mark.asyncio
async def test_crud():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create
        r = await ac.post("/items", json={"name":"Test","description":"x","price":1.23})
        assert r.status_code == 201
        item = r.json()
        item_id = item["id"]

        # Read
        r = await ac.get(f"/items/{item_id}")
        assert r.status_code == 200

        # Update
        r = await ac.put(f"/items/{item_id}", json={"name":"Test2","description":"y","price":2.34})
        assert r.status_code == 200
        assert r.json()["name"] == "Test2"

        # Delete
        r = await ac.delete(f"/items/{item_id}")
        assert r.status_code == 204

        # Not found
        r = await ac.get(f"/items/{item_id}")
        assert r.status_code == 404
