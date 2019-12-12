from json.decoder import JSONDecodeError

from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    headers = dict(request.headers) or None
    query = dict(request.query) or None

    body = await request.text() or None
    post = dict(await request.post()) or None

    try:
        json = await request.json()
    except JSONDecodeError:
        json = None

    return web.json_response({
        'method': request.method,
        'version': request.version,
        'host': request.host,
        'path': request.path,
        'headers': headers,
        'query': query,
        'body': body,
        'post': post,
        'json': json,
    })


app = web.Application()
app.add_routes([
    web.route('*', '/{path:.*}', handler),
])
