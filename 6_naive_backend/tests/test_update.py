import pytest
from starlette.testclient import TestClient

from todo_server.app_factory import create_app


@pytest.mark.update
def test_update():
    app = create_app()
    client = TestClient(app)
    total = 5
    done_id = 1
    for i in range(1, total):
        client.post('/todos', json={
            'text': f'Do item {i}',
            'done': False
        })

    client.put(f'/todos/{done_id}', json={'done': True})

    expected = [{
        'id': i,
        'done': i == done_id,
        'text': f'Do item {i}',
    } for i in range(1, total)]

    response = client.get('/todos')

    assert response.json() == expected
