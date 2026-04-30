# FIX_PRICE_UX_FINAL_POLISH_COMMIT_NOTE

## Decision

This branch remains focused on price input and cost calculation.

No new domain model is added here:
- no room type registry
- no survey deviation layer
- no wall curvature logic
- no backend persistence

## UX Fixes

- Default room name changed from `Bathroom` to `Ванная`.
- Procurement status is clarified:
  - `Нет цены`
  - `Цена учтена`

## Why

The cost table status means the user entered a price.

The procurement table is not calculated from price. Procurement quantity is calculated from:
- room geometry
- operation rules
- material consumption norms
- package rounding

Therefore `Цена учтена` is clearer than `Цена введена` in the procurement block.

## Files

```text
frontend/prototype/index.html
frontend/prototype/static/app.js
tests/test_price_ux_final_polish.py
```

## Run

```powershell
powershell -ExecutionPolicy Bypass -File scripts/apply_price_ux_final_polish.ps1
pytest
uvicorn app.main:app --reload
```

## Manual Check

```text
1. Open /prototype.
2. Confirm room field uses "Ванная".
3. Click "Рассчитать комнату".
4. Enter prices.
5. Confirm cost table shows "Цена введена".
6. Confirm procurement table shows "Цена учтена".
```

## Commit

```powershell
git add .
git status
git commit -m "fix: polish price UX labels"
git push -u origin feat/price-input-and-cost-calculation
```
