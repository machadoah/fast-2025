from fastapi import status
from fastapi.testclient import TestClient

from fasttodo.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Assert


def test_health_deve_retornar_ok_e_html():
    client = TestClient(app)  # Arrange

    response = client.get('/health')  # Act

    assert response.status_code == status.HTTP_200_OK  # Assert
    assert (
        response.headers['content-type'] == 'text/html; charset=utf-8'
    )  # Assert

    assert (
        response.text
        == """
<html>
<head>
    <title>FastAPI Health Check</title>
</head>
<body>
    <h1>FastAPI Health Check</h1>
    <p>Status: OK</p>
</body>
</html>
"""
    )
