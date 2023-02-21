from fastapi.testclient import TestClient
from hello_world.app import app

client = TestClient(app)

def test_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello SAM World"}