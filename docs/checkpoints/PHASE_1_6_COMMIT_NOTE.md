# Phase 1.6 — Domain Model

## Added / Updated

- `docs/05_domain_model.md`
- `docs/audit/phase_1_6_domain_model_self_audit_v0.1.md`

## Purpose

This phase turns MVP scope into concrete domain entities, fields, enums and relationships.

## Why This Matters

Without a domain model we cannot safely write:

- Pydantic schemas
- SQLAlchemy models
- API contract
- JSON artifacts
- validation rules
- calculation engines
- frontend types
- tests

## Recommended Commit

```bash
git add docs/05_domain_model.md docs/audit/phase_1_6_domain_model_self_audit_v0.1.md docs/checkpoints/PHASE_1_6_COMMIT_NOTE.md
git commit -m "docs: add domain model specification"
git push -u origin docs/phase-1-6-domain-model
```

## Pull Request

Open PR:

```text
docs/phase-1-6-domain-model → main
```

## Next Step

`Phase 1.7 — Full Specification: 06_json_artifacts_spec.md`
