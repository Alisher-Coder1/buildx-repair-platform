# feat/material-consumption-engine

## Added / Updated

- `app/domain/material_engine.py`
- `app/services/summary_service.py`
- `app/api/routes/summaries.py`
- `app/schemas/summaries.py`
- `tests/test_material_engine_formulas.py`
- `tests/test_material_consumption_engine.py`
- `tests/test_material_consumption_summary_api.py`

## Purpose

This phase adds Material Consumption Engine.

Backend can now calculate:

- material quantity
- formula type
- loss factor
- layer count
- thickness
- package count
- material consumption summary endpoint

## New Endpoint

```text
GET /api/v1/rooms/{room_id}/material-consumption-summary
```

## Run

```powershell
pytest
uvicorn app.main:app --reload
```

## Commit

```powershell
git add .
git status
git commit -m "feat: add material consumption engine"
git push -u origin feat/material-consumption-engine
```

## Next Branch

```powershell
feat/cost-procurement-summary
```
