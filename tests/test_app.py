from fastapi.testclient import TestClient
from fastapi_todo.app import app
from http import HTTPStatus


def test_should_be_able_to_return_ok():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


