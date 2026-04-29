# Documentation Audit Question Matrix v0.1

## Purpose

This matrix defines how documents are audited before approval or freeze.

## Universal Audit Questions

For every document, auditor must check:

1. Does the document answer all its key questions?
2. Is its purpose clear?
3. Is scope clear?
4. Are MVP, Out of Scope and Future Scope separated?
5. Does it define its hierarchy level?
6. Does it define its implementation block?
7. Does it list directly related documents?
8. Does it list upstream dependencies?
9. Does it list downstream dependencies?
10. Does it avoid duplicating another document?
11. Does it identify likely conflict points?
12. Does it define source-of-truth responsibility?
13. Are requirements testable?
14. Are errors and edge cases described where relevant?
15. Does the document avoid implementation-tool lock-in?
16. Can a developer or AI coding agent implement the related block without guessing?
17. Are unresolved questions moved to `backlog/open_questions.md`?
18. Does the document have acceptance criteria?
19. Does it have freeze criteria?
20. Does it require expert review?

## Cross-Document Governance Questions

1. Does this document conflict with MVP Scope?
2. Does it conflict with Domain Model?
3. Does it require JSON artifact fields not defined in artifact spec?
4. Does it introduce API fields not defined in API Contract?
5. Does it introduce UI states not covered by UI/UX spec?
6. Does it introduce validation behavior not covered by Validation Spec?
7. Does it introduce tests not covered by Testing Spec?
8. Does it duplicate another document’s source-of-truth responsibility?


## Dependency Map Audit Questions

Before a document is approved or frozen, auditor must check `docs/audit/documentation_dependency_map_v0.1.md` and answer:

1. Is the document listed in the dependency map?
2. Is the document placed in the correct document pack?
3. Are upstream dependencies correct?
4. Are directly related documents correct?
5. Are downstream dependencies correct?
6. Are likely conflict risks identified?
7. Are documents that must be updated together identified?
8. Does the document duplicate another source of truth?
9. Does the document need registry updates?
10. Does the correct AI reading pack exist for this implementation area?

## Required Control Files for Audit

Every documentation audit must use:

```text
docs/00_documentation_index.md
docs/documentation_registry_v0.1.yaml
docs/audit/documentation_audit_question_matrix_v0.1.md
docs/audit/documentation_dependency_map_v0.1.md
```

## Audit Result Options

```text
PASS
PASS_WITH_NOTES
NEEDS_REVISION
BLOCKED
REQUIRES_EXPERT_REVIEW
```

## Freeze Audit

Before FROZEN status:

- [ ] All blocking questions resolved.
- [ ] All related docs reviewed.
- [ ] No source-of-truth conflict.
- [ ] Acceptance criteria complete.
- [ ] Change rules present.
- [ ] Registry entry updated.
- [ ] Dependency map checked and updated if needed.
