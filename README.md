# requestd

Simple [aiohttp](https://aiohttp.readthedocs.io/en/stable/) server for request debugging.

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
docker image tag requestd "2tunnels/requestd:latest"
docker image tag requestd "2tunnels/requestd:$(date +"%Y.%m.%d")-$(git rev-parse --short HEAD)"
```

Push:

```bash
docker image push "2tunnels/requestd:latest"
docker image push "2tunnels/requestd:$(date +"%Y.%m.%d")-$(git rev-parse --short HEAD)"
```
