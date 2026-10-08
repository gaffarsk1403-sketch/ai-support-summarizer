from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_summarize_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    response = client.post(
        "/summarize",
        json={
            "case_id": "CASE-1001",
            "customer_message": "My payment was charged twice and I need help.",
            "agent_notes": "Customer contacted support this morning.",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["case_id"] == "CASE-1001"
    assert body["summary"]
    assert body["next_actions"]
