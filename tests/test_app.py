from fastapi.testclient import TestClient

from project_1.app import app

client = TestClient(app)
