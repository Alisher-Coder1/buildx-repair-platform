# FIX_PRICE_INPUT_REACTIVITY_COMMIT_NOTE

## Problem

During manual check of `feat/price-input-and-cost-calculation`:

```text
Cost rows were calculated correctly.
Overview total was calculated correctly.
Procurement status did not update after price input.
Price input felt sticky because the full cost table was re-rendered on every typed symbol.
```

## Fix

- Do not re-render the full cost table on each price input.
- Update only:
  - row total cell
  - row status cell
  - total cost card
  - overview cards
  - procurement status table
- Add `data-price-total` and `data-price-status` markers.
- Add `updatePriceDerivedViews()`.
- Re-render procurement after each price input.

## Files

```text
frontend/prototype/static/app.js
tests/test_price_input_reactivity_fix.py
docs/checkpoints/FIX_PRICE_INPUT_REACTIVITY_COMMIT_NOTE.md
```

## Manual Check

```text
1. Open /prototype.
2. Click "Рассчитать комнату".
3. Enter multi-digit prices.
4. Check that input no longer sticks.
5. Check that the cost total updates.
6. Check that procurement status changes to "Цена введена".
```

## Commit

```powershell
pytest
git add .
git status
git commit -m "fix: update price input reactivity and procurement status"
git push -u origin feat/price-input-and-cost-calculation
```
