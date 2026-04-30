# feat/price-input-and-cost-calculation

## Added / Updated

- `frontend/prototype/static/app.js`
- `frontend/prototype/static/styles.css`
- `tests/test_price_input_cost_calculation_frontend.py`

## Purpose

This phase converts the existing `MISSING_PRICE` placeholder into an interactive frontend cost calculation.

## What Changed

- User can enter price per package in the cost table.
- Frontend calculates row total:
  - `package_count × unit_price`
- Frontend calculates preliminary material total.
- Entered prices are stored in browser `localStorage`.
- Overview block now shows preliminary cost total.
- Procurement status updates from:
  - `Цена не указана`
  - to `Цена введена`
- No new backend module is introduced.

## Why Frontend First

This is the fastest safe implementation because:

```text
backend already returns procurement and package_count
price input is a prototype interaction
no database migration is needed
no auth/user ownership is needed yet
no API contract risk is introduced
```

Backend persistence can be added later when project save/load becomes necessary.

## Run

```powershell
pytest
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/prototype
```

## Manual Check

```text
1. Click "Рассчитать комнату".
2. Scroll to "Стоимость".
3. Enter price per package for several materials.
4. Verify row total changes.
5. Verify preliminary total changes.
6. Verify overview total changes.
```

## Commit

```powershell
git add .
git status
git commit -m "feat: add price input and frontend cost calculation"
git push -u origin feat/price-input-and-cost-calculation
```

## Next Recommended Branch

```powershell
git checkout -b feat/project-save-and-load-ui
```
