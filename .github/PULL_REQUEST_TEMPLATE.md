## What does this PR change?

<!-- frontend / backend / docs? One-line summary. -->

## Area

- [ ] frontend
- [ ] backend
- [ ] docs / chores

## API contract changed?

- [ ] No
- [ ] Yes — details: <!-- routes, request/response shapes, migration needed? -->

## How I tested

<!-- Commands + results, e.g.: npm run build ✅, visited /health, alembic upgrade head -->

- [ ] `npm run lint` / `npm run build` (frontend PRs)
- [ ] `uvicorn app.main:app` boots + `/health` ok (backend PRs)
- [ ] Manual check: <!-- pages clicked, curl, screenshots -->

## Checklist

- [ ] No `.env`, `node_modules/`, `dist/`, `__pycache__/` committed
- [ ] No hardcoded `http://127.0.0.1:8000` (uses `VITE_API_URL`)
- [ ] Branch is small and focused
