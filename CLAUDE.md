# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Official Python SDK for the [img-src.io](https://img-src.io) image CDN API. The code was originally bootstrapped from the OpenAPI spec at `api/openapi.json` in the main repo and is now maintained manually — edit files directly. The per-file `DO NOT EDIT` headers are historical. API changes should still go to [img-src-io/api](https://github.com/img-src-io/api) first to keep the spec in sync.

Package name: `img-src` (import as `img_src`). Python >=3.9.2. Uses `httpx` for HTTP, `pydantic` v2 for models.

## Commands

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Test
pytest                    # run all tests
pytest tests/test_foo.py  # run single test file
pytest -k "test_name"     # run single test by name

# Type checking
mypy src/
pyright

# Lint
pylint src/

# Build & publish
uv build
uv publish --token $PYPI_TOKEN   # or: ./scripts/publish.sh
```

CI runs `pytest` across Python 3.9–3.12 on push/PR to `main`.

## Architecture

```
src/img_src/
├── sdk.py              # Imgsrc — main entry point, lazy-loads resource modules
├── sdkconfiguration.py # SDKConfiguration dataclass (server, auth, retry, timeout)
├── basesdk.py          # BaseSDK — shared HTTP request logic for all resources
├── httpclient.py       # HttpClient/AsyncHttpClient protocols (wraps httpx)
├── images.py           # Images resource (upload, list, search, get, delete, signed URL)
├── presets.py          # Presets resource (CRUD, Pro plan)
├── settings.py         # Settings resource (get/update)
├── usage.py            # Usage resource (get stats)
├── models/             # 47 Pydantic models + TypedDict variants (request/response types)
├── errors/             # ImgsrcError → ErrorResponse, ResponseValidationError, etc.
├── types/              # BaseModel config, Nullable, OptionalNullable, UNSET sentinel
├── utils/              # Serialization, retries, query params, security, URL templating
├── _hooks/             # SDK lifecycle hooks (init, before/after request, success/error)
└── _version.py         # Version info
```

**Key patterns:**
- `Imgsrc` class uses `__getattr__` + `_sub_sdk_map` for lazy-loading resource classes (`images`, `presets`, `settings`, `usage`)
- Each resource class extends `BaseSDK` and receives `SDKConfiguration` from the parent
- Supports both sync and async via context managers (`with Imgsrc(...)` / `async with Imgsrc(...)`)
- Auth: Bearer token (`bearer_auth` param) — can be a string or callable for dynamic tokens
- All response objects wrap data models with `HTTPMetadata` (raw request/response access)
- `UNSET` sentinel distinguishes "not provided" from `None` in optional nullable fields
- Models have both Pydantic class and TypedDict variants for flexibility

