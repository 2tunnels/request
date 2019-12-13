from aiohttp.test_utils import TestClient

from requestd import create_application


async def test_simple_get_request(aiohttp_client):
    client: TestClient = await aiohttp_client(create_application())
    response = await client.get('/')

    assert response.status == 200
    assert await response.json() == {
        'method': 'GET',
        'version': [1, 1],
        'host': f'{client.server.host}:{client.server.port}',
        'path': '/',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': f'{client.server.host}:{client.server.port}',
            'User-Agent': 'Python/3.8 aiohttp/3.6.2',
        },
        'query': None,
        'body': None,
        'post': None,
        'json': None,
    }


async def test_simple_post_request(aiohttp_client):
    client: TestClient = await aiohttp_client(create_application())
    response = await client.post('/signup', data={
        'username': 'john',
        'password': 'qwerty',
    })

    assert response.status == 200
    assert await response.json() == {
        'method': 'POST',
        'version': [1, 1],
        'host': f'{client.server.host}:{client.server.port}',
        'path': '/signup',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Length': '29',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': f'{client.server.host}:{client.server.port}',
            'User-Agent': 'Python/3.8 aiohttp/3.6.2',
        },
        'query': None,
        'body': 'username=john&password=qwerty',
        'post': {
            'username': 'john',
            'password': 'qwerty',
        },
        'json': None,
    }
