# 27 — Development Methodology and Coding Standards

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_27 |
| File Name | `27_development_methodology_and_coding_standards.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 5 — Implementation Discipline |
| Implementation Block | Development methodology, architecture rules, coding standards, testing gates |
| Criticality | CRITICAL |
| Source of Truth Responsibility | Defines how Prototype v0.1 must be implemented without architectural chaos |
| Directly Related Documents | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md`, `08_material_consumption_engine_spec.md`, `10_api_contract.md`, `26_validation_and_error_handling_spec.md`, `12_testing_and_release_spec.md` |
| Upstream Dependencies | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md`, `08_material_consumption_engine_spec.md`, `10_api_contract.md`, `26_validation_and_error_handling_spec.md` |
| Downstream Dependencies | Backend implementation, frontend implementation, tests, releases, CI |
| Duplication Check | This document defines implementation discipline only. It must not redefine domain entities, formulas, API contracts or validation codes. |
| Conflict Check | Code implementation must follow this document unless a Change Request changes the methodology. |

---

## 1. Purpose

This document defines how Prototype v0.1 must be implemented.

The goal is to move from documentation to working code quickly without creating a fragile, chaotic codebase.

This document exists to answer:

```text
How do we write the backend?
How do we keep business logic out of the UI?
How do we structure files?
How do we test calculations?
How do we avoid silent fallback?
How do we know the prototype is ready?
```

---

## 2. Main Development Principle

```text
Build the smallest correct vertical slice first.
```

The first implementation target:

```text
Project
→ Room
→ Geometry
→ JSON artifacts
→ Execution summary
→ Material consumption summary
→ Cost summary
→ Procurement summary
→ API
→ tests
```

Do not implement future layers before this works.

---

## 3. Technology Stack for Prototype v0.1

### Backend

```text
Python 3.11+
FastAPI
Pydantic
SQLAlchemy
SQLite
pytest
```

### Data

```text
JSON artifacts in data/artifacts/
```

### Frontend later

```text
Next.js
TypeScript
modern guided UI
```

Frontend starts only after backend core is working.

---

## 4. Architecture Style

Prototype v0.1 must use:

```text
modular monolith
domain-first architecture
rule-driven logic
test-supported implementation
strict validation
no silent fallback
```

It must not use:

```text
microservices
distributed architecture
complex event sourcing
premature multi-tenant SaaS architecture
AI-generated hidden logic
business logic in frontend
```

---

## 5. Backend Folder Structure

Recommended initial structure:

```text
app/
  main.py
  core/
    config.py
    errors.py
    responses.py
  db/
    base.py
    session.py
    models.py
  api/
    routes/
      health.py
      projects.py
      rooms.py
      summaries.py
  schemas/
    project.py
    room.py
    summaries.py
    errors.py
  domain/
    geometry.py
    execution_engine.py
    material_engine.py
    cost_engine.py
    procurement_engine.py
  artifacts/
    loader.py
    validators.py
  services/
    project_service.py
    room_service.py
    summary_service.py
tests/
  test_geometry.py
  test_artifact_loader.py
  test_artifact_validation.py
  test_project_room_api.py
  test_execution_summary.py
  test_material_engine_formulas.py
  test_material_engine_errors.py
  test_cost_procurement_summary.py
data/
  artifacts/
```

This structure may be adjusted during implementation, but responsibilities must remain separated.

---

## 6. Layer Responsibilities

### 6.1 API Layer

Responsible for:

```text
HTTP routes
request parsing
response envelope
status codes
calling services
```

Not responsible for:

```text
formulas
material calculations
artifact rule matching
business decisions
```

### 6.2 Service Layer

Responsible for:

```text
orchestrating domain modules
loading project/room data
calling calculation engines
returning summary objects
```

Not responsible for:

```text
raw formulas
hardcoded material norms
UI formatting
```

### 6.3 Domain Layer

Responsible for:

```text
geometry formulas
execution generation
material calculations
cost/procurement logic
deterministic rules
```

Not responsible for:

```text
HTTP
database sessions
frontend layout
```

### 6.4 Artifact Layer

Responsible for:

```text
loading JSON artifacts
validating artifact structure
checking references
exposing artifact data to engines
```

Not responsible for:

```text
calculating material quantities
API response formatting
```

### 6.5 DB Layer

Responsible for:

```text
Project persistence
Room persistence
SQLite setup
basic migrations or table creation
```

Prototype v0.1 should not store every generated summary unless required.

Recommended:

```text
store Project and Room
calculate summaries on request
```

---

## 7. Coding Standards

### 7.1 General

```text
Readable code over clever code.
Small functions.
Explicit inputs and outputs.
No hidden global state for business logic.
No silent fallback.
No broad except without structured error.
No business logic in route functions.
```

### 7.2 Python

```text
Use type hints.
Use Pydantic models for request/response schemas.
Use Decimal or controlled float strategy for calculations.
Use dataclasses or Pydantic models for internal domain objects when useful.
Keep calculation functions pure where possible.
```

### 7.3 Naming

```text
project_id
room_id
material_id
operation_id
rule_id
norm_id
package_id
```

Use names from Domain Model and JSON Artifacts.

Do not invent alternate names such as:

```text
matId
workId
calcRule
roomGuid
```

unless explicitly mapped.

---

## 8. Calculation Standards

### 8.1 Formula Location

Formulas must live in domain modules:

```text
app/domain/geometry.py
app/domain/material_engine.py
```

They must not live in:

```text
API routes
frontend components
database models
JSON files as executable logic
```

### 8.2 Formula Tests

Every formula must have a numeric test.

Minimum required:

```text
floor_area
ceiling_area
perimeter
wall_area
area_based material calculation
layer_based material calculation
thickness_based material calculation
linear_based material calculation
package_count
```

### 8.3 Package Count

Package count must use:

```text
ceil(material_quantity / package_size)
```

No rounding-down is allowed.

---

## 9. Validation Standards

Implementation must follow:

```text
26_validation_and_error_handling_spec.md
```

Required behavior:

```text
invalid input -> structured error
missing artifact -> structured error
missing rule -> structured error
missing norm -> structured error
missing package -> structured error
```

Forbidden behavior:

```text
returning empty list when rule missing
returning zero when norm missing
assuming default package size
guessing thickness
guessing layer count
```

---

## 10. API Standards

Implementation must follow:

```text
10_api_contract.md
```

Every endpoint must return:

```text
success
data or errors
warnings
meta
```

API routes must not return raw internal exceptions.

---

## 11. JSON Artifact Standards

Implementation must follow:

```text
06_json_artifacts_spec.md
```

Artifact loader must:

```text
load all required artifact files
parse JSON
validate required keys
check duplicate IDs
check references
raise structured errors
```

---

## 12. Testing Strategy

### 12.1 Test Priority

Implementation must add tests in this order:

```text
1. Geometry tests
2. Artifact loader tests
3. Artifact reference validation tests
4. Material formula tests
5. Material engine error tests
6. Project/Room API tests
7. Summary API tests
8. Cost/Procurement summary tests
```

### 12.2 Test Rule

No engine is accepted without tests.

### 12.3 Numeric Assertions

Tests must check concrete numeric values, not only response shape.

Example:

```text
wall_area_m2 must equal 37.80 for 4m x 3m x 2.7m room
wall paint package_count must equal 2
laminate package_count must equal 7
```

---

## 13. Implementation Sequence

The backend must be implemented in this sequence:

### Step 1 — Project Skeleton

```text
create app/
create tests/
configure FastAPI
configure pytest
add health endpoint
```

### Step 2 — Database Core

```text
SQLAlchemy setup
SQLite database
Project model
Room model
basic session handling
```

### Step 3 — Schemas

```text
ProjectCreate
ProjectRead
RoomCreate
RoomRead
ErrorResponse
Summary schemas
```

### Step 4 — Geometry

```text
geometry functions
core-summary endpoint
geometry tests
```

### Step 5 — Artifact Loader

```text
load JSON files
validate IDs
validate references
artifact tests
```

### Step 6 — Execution Summary

```text
generate operations from room + coverings + zone
execution-summary endpoint
tests
```

### Step 7 — Material Engine

```text
formula functions
rule matching
norm/package resolution
material summary endpoint
tests
```

### Step 8 — Cost/Procurement

```text
basic cost summary
missing price warnings
procurement aggregation
tests
```

### Step 9 — README + Run Report

```text
run instructions
test instructions
known limitations
```

---

## 14. Git Branch Strategy

Documentation branches:

```text
docs/phase-...
```

Code branches:

```text
feat/backend-project-room-core
feat/geometry-engine
feat/artifact-loader
feat/execution-summary
feat/material-consumption-engine
feat/cost-procurement-summary
```

Bugfix branches:

```text
fix/package-count-rounding
fix/missing-rule-error
```

Technical branches:

```text
chore/pytest-setup
chore/github-actions
```

`main` must stay stable.

---

## 15. Definition of Done for Backend Prototype Core

Backend prototype core is done when:

```text
1. FastAPI app runs locally.
2. Health endpoint works.
3. Project can be created.
4. Room can be created.
5. Core geometry summary works.
6. Artifact loader works.
7. Execution summary works.
8. Material consumption summary works.
9. Cost summary works with missing price warnings.
10. Procurement summary works.
11. Structured errors work.
12. Required tests pass.
13. README explains how to run backend.
```

---

## 16. Quality Gates

Before merging any code PR:

```text
pytest must pass
no unrelated files
no .env committed
no generated junk files
no business logic in API route
no formula without test
no silent fallback
```

---

## 17. What Not To Do

Do not implement now:

```text
auth/RBAC
payments
subscriptions
supplier marketplace
mobile app
contractor workflow
client workflow
legal docs
smart home
HVAC
full production deployment
```

Do not build frontend before backend core gives stable API responses.

---

## 18. Acceptance Criteria

This document is accepted if:

```text
1. It defines implementation architecture.
2. It defines folder structure.
3. It defines layer responsibilities.
4. It defines coding standards.
5. It defines testing order.
6. It defines backend implementation sequence.
7. It defines branch strategy.
8. It defines quality gates.
9. It clearly says when to start code.
```

---

## 19. Freeze Criteria

This document can be frozen when:

```text
1. MVP Scope is accepted.
2. Domain Model is accepted.
3. JSON Artifacts spec is accepted.
4. Material Engine spec is accepted.
5. API Contract is accepted.
6. Validation spec is accepted.
7. Implementation sequence is approved.
```

---

## 20. Final Decision

After this document is accepted, documentation is sufficient to start backend implementation.

Next phase becomes:

```text
feat/backend-project-room-core
```

The goal of that code phase:

```text
FastAPI app + SQLite + Project + Room + Geometry + tests
```
