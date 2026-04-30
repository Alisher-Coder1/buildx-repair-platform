# feat/cost-procurement-summary

## Added / Updated

- `app/domain/cost_engine.py`
- `app/domain/procurement_engine.py`
- `app/services/summary_service.py`
- `app/api/routes/summaries.py`
- `app/schemas/summaries.py`
- `tests/test_cost_procurement_summary.py`
- `tests/test_cost_procurement_summary_api.py`

## Purpose

This phase adds cost and procurement summaries.

Backend can now return:

- cost-summary
- procurement-summary
- missing price warnings
- grouped purchase list
- purchase_quantity

## New Endpoints

```text
GET /api/v1/rooms/{room_id}/cost-summary
GET /api/v1/rooms/{room_id}/procurement-summary
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
git commit -m "feat: add cost and procurement summaries"
git push -u origin feat/cost-procurement-summary
```

## Next Branch

```powershell
feat/prototype-api-smoke-report
```
