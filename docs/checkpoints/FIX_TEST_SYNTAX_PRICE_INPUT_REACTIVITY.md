# FIX_TEST_SYNTAX_PRICE_INPUT_REACTIVITY

## Problem

`pytest` failed during collection because `tests/test_price_input_reactivity_fix.py`
contained an invalid Python string with unescaped double quotes.

## Fix

The problematic assertion was changed to use single-quoted Python string syntax:

```python
assert 'input.addEventListener("input", () => {' in response.text
```

## Files

```text
tests/test_price_input_reactivity_fix.py
```

## Run

```powershell
pytest
```
