from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from promptdex.main import create_app


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    app = create_app(f"sqlite:///{tmp_path / 'promptdex.db'}")
    with TestClient(app) as test_client:
        yield test_client


def create_prompt(client: TestClient, **overrides: object) -> dict:
    payload = {
        "title": "Refactor buddy",
        "body": "Help me refactor this Python module without changing behavior.",
        "category": "Coding",
        "tags": ["python", "codex"],
        "rating": 4,
        "favorite": False,
    }
    payload.update(overrides)

    response = client.post("/api/prompts", json=payload)

    assert response.status_code == 201
    return response.json()


def test_create_and_list_prompts(client: TestClient) -> None:
    prompt = create_prompt(client)

    response = client.get("/api/prompts")

    assert response.status_code == 200
    assert response.json() == [prompt]
    assert prompt["id"] == 1
    assert prompt["tags"] == ["python", "codex"]
    assert prompt["created_at"]
    assert prompt["updated_at"]
    assert prompt["last_used_at"] is None


def test_search_category_and_tag_filters(client: TestClient) -> None:
    create_prompt(client, title="Debug crash", category="Debugging", tags=["errors", "python"])
    create_prompt(client, title="Launch email", category="Marketing", tags=["copy", "campaign"])

    search_response = client.get("/api/prompts", params={"search": "crash"})
    category_response = client.get("/api/prompts", params={"category": "Marketing"})
    tag_response = client.get("/api/prompts", params={"tag": "python"})

    assert [prompt["title"] for prompt in search_response.json()] == ["Debug crash"]
    assert [prompt["title"] for prompt in category_response.json()] == ["Launch email"]
    assert [prompt["title"] for prompt in tag_response.json()] == ["Debug crash"]


def test_update_favorite_and_rating(client: TestClient) -> None:
    prompt = create_prompt(client)

    response = client.put(
        f"/api/prompts/{prompt['id']}",
        json={"favorite": True, "rating": 5, "tags": ["python", "keeper"]},
    )

    assert response.status_code == 200
    updated = response.json()
    assert updated["favorite"] is True
    assert updated["rating"] == 5
    assert updated["tags"] == ["python", "keeper"]


def test_use_prompt_sets_last_used_at_and_returns_body(client: TestClient) -> None:
    prompt = create_prompt(client, body="Copy exactly this useful prompt.")

    response = client.post(f"/api/prompts/{prompt['id']}/use")

    assert response.status_code == 200
    used = response.json()
    assert used["body"] == "Copy exactly this useful prompt."
    assert used["last_used_at"] is not None


def test_delete_prompt(client: TestClient) -> None:
    prompt = create_prompt(client)

    response = client.delete(f"/api/prompts/{prompt['id']}")

    assert response.status_code == 204
    assert client.get("/api/prompts").json() == []
