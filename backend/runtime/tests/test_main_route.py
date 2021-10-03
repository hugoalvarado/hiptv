import app
from chalice.test import Client


def test_index_returns_hello():
    with Client(app.app) as client:
        response = client.http.get('/')
        assert response.status_code == 200
        assert response.json_body == {"hello": "world"}
