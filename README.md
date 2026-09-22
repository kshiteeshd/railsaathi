# Rail Saathi

Train journey companion — FastAPI backend + React + Vite frontend.

## Repo layout

```text
backend/   FastAPI API, SQLAlchemy models, Alembic migrations
frontend/  React + TypeScript + Vite app
data/seed/ Seed data (CSVs/JSON, optional)
```

## Prerequisites

- Python 3.12+ (backend)
- Node 20+ (frontend)
- PostgreSQL 16+ running locally

## Quick start (two terminals)

### 1. Backend

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

copy .env.example .env
# then edit .env: DATABASE_URL, SECRET_KEY

# create DB if needed (psql):
# CREATE DATABASE rail_saathi;

alembic upgrade head

uvicorn app.main:app --reload --port 8000
```

API: `http://127.0.0.1:8000` — health: `http://127.0.0.1:8000/health` — docs: `http://127.0.0.1:8000/docs`

### 2. Frontend (your friend works here)

```bash
cd frontend
npm install

copy .env.example .env
# VITE_API_URL=http://127.0.0.1:8000

npm run dev
```

App: `http://localhost:5173`

## Environment variables

Backend (`backend/.env`, never commit):
- `DATABASE_URL=postgresql+psycopg://USER:PASS@localhost:5432/rail_saathi`
- `SECRET_KEY=` long random — generate: `python -c "import secrets; print(secrets.token_urlsafe(64))"`
- `ALGORITHM=HS256`
- `ACCESS_TOKEN_EXPIRE_MINUTES=30`

Frontend (`frontend/.env`):
- `VITE_API_URL=http://127.0.0.1:8000`

Examples: `backend/.env.example`, `frontend/.env.example`.

## Useful commands

Backend (from `backend/`):
```bash
alembic revision --autogenerate -m "describe change"
alembic upgrade head
pytest
```

Frontend (from `frontend/`):
```bash
npm run dev
npm run build
npm run lint
```

## Contributing / PRs

See `CONTRIBUTING.md`. Short version:
1. `git checkout -b feat/short-name` (or `fix/...`, `frontend/...`, `backend/...`)
2. Keep backend/frontend changes separate when possible.
3. `npm run build` must pass, backend must import (`uvicorn app.main:app` boots).
4. Open PR using the template — include how you tested.

## Security

Never commit `backend/.env`, `frontend/.env`, `node_modules/`, `__pycache__/`, `dist/`. They are git-ignored. If a secret leaks, rotate it immediately.
