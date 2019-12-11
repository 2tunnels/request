from aiohttp import web


async def handler(request: web.Request) -> web.Response:
    return web.json_response({
        'method': request.method,
        'headers': dict(request.headers),
        'query': dict(request.query),
        'post': dict(await request.post()),
    })


app = web.Application()
app.add_routes([
    web.route('*', '/', handler),
])
web.run_app(app)
