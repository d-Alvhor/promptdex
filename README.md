# PromptDex

PromptDex is a local-first Pokédex of prompts for storing, searching, rating, favoriting, and copying AI prompts. It runs on your machine with FastAPI, SQLite, SQLAlchemy, and a simple HTML/CSS/JS frontend.

## Features

- Create, edit, and delete prompts
- Search by title, body, category, or tag
- Filter by category, tag, and favorites
- Mark prompts as favorites
- Rate prompts from 1 to 5 stars
- Copy prompt text to the clipboard
- Track the last used date when a prompt is copied
- Persist data locally in SQLite

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Run Locally

```powershell
uv sync
uv run uvicorn promptdex.main:app --reload --host 127.0.0.1 --port 8000
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

Prompt data is stored in `promptdex.db` in the project root by default.

## Development

Run tests:

```powershell
uv run pytest
```

Run linting:

```powershell
uv run ruff check .
```

Format code:

```powershell
uv run ruff format .
```

## API

- `GET /api/prompts`
- `POST /api/prompts`
- `GET /api/prompts/{id}`
- `PUT /api/prompts/{id}`
- `DELETE /api/prompts/{id}`
- `POST /api/prompts/{id}/use`
- `GET /api/categories`
