# 45 Documentation Writing Methodology and Style Guide

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_45 |
| File Name | 45_documentation_writing_methodology_and_style_guide.md |
| Version | v0.1 |
| Status | DRAFT |
| Owner | Documentation Architect |
| Hierarchy Level | Level 0 — Documentation Process / Writing Standard |
| Implementation Block | Documentation production, writing quality, markdown style |
| Source of Truth Responsibility | How documentation files must be written |
| Directly Related Documents | 00_documentation_index.md, 13_document_acceptance_and_governance.md, documentation_audit_question_matrix_v0.1.md, documentation_dependency_map_v0.1.md, document_template.md |
| Upstream Dependencies | 00_documentation_index.md |
| Downstream Dependencies | All documentation files |
| Duplication Check | Must not duplicate the detailed governance workflow or audit matrix |
| Conflict Check | Must align with document_template.md |
| Requires Expert Review | No |

## Purpose

This document defines how every documentation file must be written so that documentation remains clear, testable, audit-ready and implementation-ready.

## Writing Standard

Every document must be:

- structured;
- unambiguous;
- testable;
- source-of-truth aware;
- linked to related documents;
- separated into MVP and Future Scope;
- free of tool-specific binding;
- written for humans and AI agents.

## Mandatory Metadata

Every numbered document must include:

- Document ID;
- File Name;
- Version;
- Status;
- Owner;
- Hierarchy Level;
- Implementation Block;
- Source of Truth Responsibility;
- Directly Related Documents;
- Upstream Dependencies;
- Downstream Dependencies;
- Duplication Check;
- Conflict Check;
- Requires Expert Review.

## Requirement Writing Rules

Bad:

```text
Make material calculation convenient.
```

Good:

```text
Material Summary must include material_id, quantity, unit, package_size, package_count, formula_type, loss_factor and source_operation_id.
If material rule is missing, system must return ERR_MATERIAL_RULE_MISSING and block procurement summary generation.
```

## MVP vs Future Separation

Every document must explicitly separate:

```text
In Scope
Out of Scope
Future Scope
```

Future ideas must not silently enter MVP.

## Forbidden Writing Patterns

Avoid unclear wording:

```text
approximately
somehow
smartly
conveniently
better
modern without criteria
as needed
```

Replace with measurable criteria.

## Markdown Rules

Use:

- `#`, `##`, `###` headings;
- Markdown tables for structured metadata;
- code blocks for JSON/YAML examples;
- checklists for acceptance criteria;
- stable identifiers for requirements and rules.

## Traceability Requirement

Important requirements should be traceable to:

```text
Document → Requirement → Module → API/Test → Status
```

## Tool-Neutral Requirement

Documentation must not bind implementation to a specific coding tool.

Use:

```text
developer
implementation executor
AI coding agent
team
```

Do not require:

```text
Claude Code
Cursor
specific assistant
```

## Acceptance Criteria

This style guide is accepted if:

- [ ] It defines mandatory document structure.
- [ ] It defines metadata requirements.
- [ ] It defines requirement-writing rules.
- [ ] It separates MVP/Future writing rules.
- [ ] It defines audit-readiness expectations.
- [ ] It supports human and AI use.


## Dependency Writing Rule

Every document must describe its document relationships consistently with:

- `docs/documentation_registry_v0.1.yaml`
- `docs/audit/documentation_dependency_map_v0.1.md`

The following relationship fields are mandatory:

- Directly Related Documents;
- Upstream Dependencies;
- Downstream Dependencies;
- Duplication Check;
- Conflict Check.

If a document introduces a new dependency, the dependency map and registry must be updated in the same change.
