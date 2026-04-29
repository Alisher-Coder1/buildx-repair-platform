# feat/artifact-loader

## Added

- `.gitignore`
- `app/artifacts/exceptions.py`
- `app/artifacts/loader.py`
- `app/artifacts/validators.py`
- artifact error codes in `app/core/errors.py`
- artifact loader tests
- artifact validation tests

## Important cleanup

If `__pycache__` files are tracked, remove them from Git index before commit:

```powershell
git rm -r --cached tests/__pycache__
```

Then check:

```powershell
git status
```

## Commit

```powershell
git add .
git status
git commit -m "feat: add artifact loader and validation"
git push -u origin feat/artifact-loader
```

## Next Branch

```powershell
feat/execution-summary
```
