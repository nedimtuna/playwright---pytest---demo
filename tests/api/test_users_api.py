import pytest

pytestmark = pytest.mark.api


def test_get_user(api_client):
    response = api_client.get("/users/2")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()

    expected_fields = {
        "id",
        "email",
        "first_name",
        "last_name",
        "avatar",
    }

    assert expected_fields.issubset(body["data"].keys())

    assert body["data"]["id"] == 2
    assert isinstance(body["data"]["id"], int)
    assert isinstance(body["data"]["email"], str)
    assert body["data"]["email"]


def test_get_non_existing_user(api_client):
    response = api_client.get("/users/23")

    assert response.status_code == 404
    assert "application/json" in response.headers["Content-Type"]
    assert response.json() == {}


def test_register_user_without_password(api_client):
    payload = {
        "email": "eve.holt@reqres.in",
    }

    response = api_client.post("/register", payload)

    assert response.status_code == 400
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()

    assert "error" in body
    assert isinstance(body["error"], str)
    assert body["error"]


def test_create_user(api_client):
    payload = {
        "name": "Nedim",
        "job": "QA Engineer",
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()

    expected_fields = {
        "name",
        "job",
        "id",
        "createdAt",
    }

    assert expected_fields.issubset(body.keys())

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]

    assert isinstance(body["id"], str)
    assert body["id"]

    assert isinstance(body["createdAt"], str)
    assert body["createdAt"]


def test_update_user(api_client):
    payload = {
        "name": "Nedim",
        "job": "Senior QA Engineer",
    }

    response = api_client.put("/users/2", payload)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()

    expected_fields = {
        "name",
        "job",
        "updatedAt",
    }

    assert expected_fields.issubset(body.keys())

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]

    assert isinstance(body["updatedAt"], str)
    assert body["updatedAt"]


def test_partial_update_user(api_client):
    payload = {
        "job": "QA Automation Engineer",
    }

    response = api_client.patch("/users/2", payload)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()

    expected_fields = {
        "job",
        "updatedAt",
    }

    assert expected_fields.issubset(body.keys())

    assert body["job"] == payload["job"]
    assert isinstance(body["updatedAt"], str)
    assert body["updatedAt"]


def test_delete_user(api_client):
    response = api_client.delete("/users/2")

    assert response.status_code == 204
    assert response.text == ""
