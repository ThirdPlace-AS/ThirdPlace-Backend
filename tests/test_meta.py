from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_meta_reports_blocked_disposition() -> None:
    resp = client.get("/meta")
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "thirdplace-backend"
    assert body["version"] == "0.0.0"
    # The service must honestly report it is not V2.2-certified.
    assert body["disposition"] == "BLOCKED_NOT_V22_CERTIFIED"
