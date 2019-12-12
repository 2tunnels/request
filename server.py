from json.decoder import JSONDecodeError

from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    headers = dict(request.headers)
    query = dict(request.query)

    body = await request.text()
    post = dict(await request.post())

    try:
        json = await request.json()
    except JSONDecodeError:
        json = {}

    return web.json_response({
        'method': request.method,
        'version': request.version,
        'host': request.host,
        'headers': headers,
        'query': query,
        'body': body,
        'post': post,
        'json': json,
    })


app = web.Application()
app.add_routes([
    web.route('*', '/', handler),
])
web.run_app(app)
