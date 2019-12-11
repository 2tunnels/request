# request

Simple [aiohttp](https://aiohttp.readthedocs.io/en/stable/) server for request debugging.

## Docker

Build:

```bash
docker image build -t request .
```

Run:

```bash
docker container run -p 8080:8080 request
```

Tag:

```bash
docker image tag request "2tunnels/request:latest"
docker image tag request "2tunnels/request:$(date +"%Y.%m.%d")-$(git rev-parse --short HEAD)"
```

Push:

```bash
docker image push "2tunnels/request:latest"
docker image push "2tunnels/request:$(date +"%Y.%m.%d")-$(git rev-parse --short HEAD)"
```
