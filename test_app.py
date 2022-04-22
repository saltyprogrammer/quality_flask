import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_clien() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
