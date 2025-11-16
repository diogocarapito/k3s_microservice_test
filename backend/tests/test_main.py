from fastapi.testclient import TestClient
from main import create_api_app

app = create_api_app()
client = TestClient(app)


def test_read_messages():
    response = client.get("/api/messages")
    assert response.status_code == 200
    # assert response.json() == []  # Assuming the DB is empty at the start
