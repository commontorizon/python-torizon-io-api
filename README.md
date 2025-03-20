# Torizon IO API

> ⚠️ **Warning:** </br>
> This project is experimental and developed as part of the Torizon Innovation initiative. This software is not tested for production use. Feedback and contributions are welcomed.

This package contains a set of utilities to help make requests to the Torizon IO API.

If you want to know more about check [Toradex IO API specification](https://app.torizon.io/api/docs/torizon-openapi.yaml).

## Development Prerequisites

- curl
- Python 3.8 or higher
- pip
- Docker

### Python dependencies

```bash
pipx install poetry
```

### Generate OpenAPI client

```bash
docker \
    run \
    --rm \
    -v ${PWD}:/local \
    --user 1000:1000 \
    openapitools/openapi-generator-cli \
    generate -i /local/torizon-openapi.yaml -g python -o /local/generated \
    --additional-properties packageName=torizon_io_api \
    --additional-properties packageVersion=x.x.x \
    --additional-properties projectName=torizon-io-api
```

> ⚠️ **Warning:** </br>
> Replace `x.x.x` with the desired version.

### Build package

```bash
cd generated
poetry build
```

### Publish package

```bash
poetry run twine upload --config-file ../.pypirc dist/*
```

> ⚠️ **Warning:** </br>
> Does not forget to create a `.pypirc` file with the correct credentials.
