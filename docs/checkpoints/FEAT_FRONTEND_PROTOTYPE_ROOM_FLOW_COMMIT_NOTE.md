# feat/frontend-prototype-room-flow

## Added / Updated

- `frontend/prototype/index.html`
- `frontend/prototype/static/styles.css`
- `frontend/prototype/static/app.js`
- `app/main.py`
- `tests/test_frontend_prototype.py`

## Purpose

This phase adds the first visible frontend prototype.

The frontend is served by FastAPI at:

```text
http://127.0.0.1:8000/prototype
```

## Why Static Frontend First

This avoids:

```text
npm setup
separate frontend server
CORS setup
build step
deployment complexity
```

It allows fast product validation.

## User Flow

```text
Create Project
→ Create Room
→ Core Summary
→ Execution Summary
→ Material Consumption Summary
→ Cost Summary
→ Procurement Summary
```

## Run

```powershell
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/prototype
```

## Test

```powershell
pytest
```

## Commit

```powershell
git add .
git status
git commit -m "feat: add frontend prototype room flow"
git push -u origin feat/frontend-prototype-room-flow
```

## Next Branch

```powershell
feat/frontend-ux-polish-and-api-errors
```
