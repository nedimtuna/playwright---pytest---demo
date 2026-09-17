import pytest

pytestmark = pytest.mark.api

def test_get_user(api_client):
    response = api_client.get("/users/2")

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == 2
    assert body["data"]["email"]
    
def test_get_non_existing_user(api_client):
    response = api_client.get("/users/23")

    assert response.status_code == 404
    assert response.json() == {}
    
def test_create_user(api_client):
    payload = {
        "name": "Nedim",
        "job": "QA Engineer",
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Nedim"
    assert body["job"] == "QA Engineer"
    assert body["id"]
    assert body["createdAt"]    
    
def test_update_user(api_client):
    payload = {
        "name": "Nedim",
        "job": "Senior QA Engineer",
    }

    response = api_client.put("/users/2", payload)

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert body["updatedAt"]
    
def test_delete_user(api_client):
    response = api_client.delete("/users/2")

    assert response.status_code == 204
    assert response.text == ""        