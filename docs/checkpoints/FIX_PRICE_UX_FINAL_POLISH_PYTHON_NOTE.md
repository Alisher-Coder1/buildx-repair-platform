# APPLY PRICE UX FINAL POLISH VIA PYTHON

## Why

PowerShell 5.1 can break UTF-8 Cyrillic text in `.ps1` files if encoding is not handled exactly.
This Python patch avoids that risk by using Unicode escape sequences inside the script.

## Run

```powershell
python scripts/apply_price_ux_final_polish.py
pytest
```

## Expected

The tests in `tests/test_price_ux_final_polish.py` should pass.

## Manual check

```text
/prototype shows "Ванная"
Cost table shows "Цена введена"
Procurement table shows "Цена учтена" after prices are entered
```
