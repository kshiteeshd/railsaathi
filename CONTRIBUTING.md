# Contributing to Rail Saathi

This repo is split so two people can work without stepping on each other:
- **Frontend owner:** everything under `frontend/`
- **Backend owner:** everything under `backend/`

## Setup

Follow `README.md` — backend needs Postgres + `backend/.env`, frontend needs `frontend/.env` with `VITE_API_URL`.

## Branching

- `main` is protected — always work on a branch + PR.
- Name: `frontend/short-thing`, `backend/short-thing`, `fix/short-thing`, `docs/short-thing`.
- One PR = one concern. Don't mix frontend + backend refactors in one PR unless the API contract changed.

## Before opening a PR

Frontend (from `frontend/`):
```bash
npm install
npm run lint
npm run build
```

Backend (from `backend/` with venv active):
```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload --port 8000
# visit /health and /docs
```

- Never commit `.env`, `node_modules/`, `dist/`, `__pycache__/`, `*.pyc`, `*.db`.
- API contract changes (new/changed routes, request/response shapes) must be described in the PR so the other side can update.
- Frontend must read the API URL from `VITE_API_URL`, no hardcoded `localhost:8000` in new code.

## PR process

1. Push branch, open PR against `main` with the template filled.
2. Other person reviews. Address comments, keep the PR small.
3. Squash-merge when checks pass.
