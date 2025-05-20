from fastapi import status
from fastapi.testclient import TestClient

from fasttodo.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Assert
