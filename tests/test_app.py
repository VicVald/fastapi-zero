from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
        }


def test_update_user(client):

    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'pimpolhoflamejante31',
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
            'username': 'bob',
            'email': 'bob@example.com',
            'id': 1,
    }

    error_response = client.put(
        '/users/1000',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'pimpolhoflamejante31',
        }
    )

    assert error_response.status_code == HTTPStatus.NOT_FOUND
    assert error_response.json() == {
            'detail': 'User not found'
    }


def test_delete_user(client):

    response = client.delete(
        'users/1'
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User Deleted'
    }

    error_response = client.delete(
        'users/1'
    )

    assert error_response.status_code == HTTPStatus.NOT_FOUND
    assert error_response.json() == {
            'detail': 'User not found'
    }
