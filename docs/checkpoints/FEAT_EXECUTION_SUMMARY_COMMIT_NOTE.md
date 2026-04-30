# feat/execution-summary

## Added / Updated

- `app/domain/execution_engine.py`
- `app/services/summary_service.py`
- `app/api/routes/summaries.py`
- `app/schemas/summaries.py`
- `app/main.py`
- `tests/test_execution_summary.py`
- `tests/test_execution_summary_api.py`

## Purpose

This phase adds deterministic execution summary generation.

Backend can now return repair operations for a room based on:

- room zone
- selected floor covering
- selected wall covering
- selected ceiling covering
- room geometry
- `operations_v1.json`

## Also Fixed

- Replaced deprecated FastAPI `@app.on_event("startup")` with `lifespan`.

## Run

```powershell
pytest
uvicorn app.main:app --reload
```

## Commit

```powershell
git add .
git status
git commit -m "feat: add execution summary generation"
git push -u origin feat/execution-summary
```

## Next Branch

```powershell
feat/material-consumption-engine
```
