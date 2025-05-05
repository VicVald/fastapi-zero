import pytest
from fastapi.testclient import TestClient

from project_1.app import app


# Reduz redundâncio no código
@pytest.fixture
def client():
    return TestClient(app)
