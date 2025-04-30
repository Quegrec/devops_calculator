import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_e2e_add():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/add", params={"a": 7, "b": 3})
        assert response.status_code == 200
        assert response.json()["result"] == 10

@pytest.mark.asyncio
async def test_e2e_divide_by_zero():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get("/divide", params={"a": 10, "b": 0})
        assert response.status_code == 200
        assert response.json()["error"] == "Cannot divide by zero."
