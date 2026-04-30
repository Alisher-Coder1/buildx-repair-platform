# feat/frontend-ux-polish-and-api-errors

## Added / Updated

- `frontend/prototype/index.html`
- `frontend/prototype/static/app.js`
- `frontend/prototype/static/styles.css`
- `tests/test_frontend_ux_polish.py`

## Purpose

This phase improves frontend readability without expanding platform scope.

## Improvements

- Russian labels for operations.
- Russian labels for materials.
- Russian labels for stages, surfaces and units.
- Clear explanation for `MISSING_PRICE`.
- Overview cards for:
  - work count
  - material row count
  - package count
  - missing price count
- More useful frontend error messages.
- Better visual treatment of warning blocks.

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
git commit -m "feat: polish frontend prototype UX and API errors"
git push -u origin feat/frontend-ux-polish-and-api-errors
```

## Next Branch

```powershell
feat/prototype-milestone-v0-1-report
```
