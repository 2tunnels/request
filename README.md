# requestd

Simple [aiohttp](https://aiohttp.readthedocs.io/en/stable/) server for request debugging.

## Example

```bash
http POST https://requestd.2tunnels.com/api/users X-Custom-Header:Foobar order_by==name name=john age=10
```

Response:

```json
{
    "body": "{\"name\": \"john\", \"age\": \"10\"}",
    "headers": {
        "Accept": "application/json, */*",
        "Accept-Encoding": "gzip",
        "Content-Length": "29",
        "Content-Type": "application/json",
        "Host": "requestd.2tunnels.com",
        "User-Agent": "HTTPie/1.0.3",
        "X-Custom-Header": "Foobar",
        "X-Forwarded-For": "1.1.1.1",
        "X-Forwarded-Host": "requestd.2tunnels.com",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
        "X-Original-Forwarded-For": "8.8.8.8",
        "X-Real-IP": "8.8.8.8",
        "X-Scheme": "https"
    },
    "host": "requestd.2tunnels.com",
    "json": {
        "age": "10",
        "name": "john"
    },
    "method": "POST",
    "path": "/api/users",
    "post": null,
    "query": {
        "order_by": "name"
    },
    "version": [
        1,
        1
    ]
}
```

## Development

Clone:

```bash
git clone git@github.com:2tunnels/requestd.git
```

Install dependencies using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

Test:

```bash
pytest -x
```

Run:

```bash
./run.py
```

## Docker

Build:

```bash
docker image build -t requestd .
```

Run:

```bash
docker container run -p 8080:8080 request
```

Tag:

```bash
docker image tag requestd "2tunnels/requestd:latest" && docker image tag requestd "2tunnels/requestd:0.1.1"
```

Push:

```bash
docker image push "2tunnels/requestd:latest" && docker image push "2tunnels/requestd:0.1.1"
```
