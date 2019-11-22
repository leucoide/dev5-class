import pytest
from starlette.testclient import TestClient

from todo_server.app_factory import create_app


@pytest.mark.create
def test_update():
    app = create_app()
    client = TestClient(app)
    total = 5
    for i in range(1, total):
        client.post('/todos', json={
            'text': f'Do item {i}',
            'done': False
        })

    expected = [{
        'id': i,
        'done': False,
        'text': f'Do item {i}',
    } for i in range(1, total)]

    response = client.get('/todos')

    assert response.json() == expected
