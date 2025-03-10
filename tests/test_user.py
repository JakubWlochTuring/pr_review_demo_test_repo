import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["username"] == "johndoe"

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    assert "password" not in data

def test_delete_user():
    user_data = {}
    
