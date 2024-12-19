from fastapi.testclient import TestClient

def test_webhook_endpoint(client: TestClient):
    payload = {
        "event_type": "message_received",
        "data": {},
        "timestamp": "2024-03-14T12:00:00Z"
    }
    
    response = client.post("/webhook", json=payload)
    assert response.status_code == 200 