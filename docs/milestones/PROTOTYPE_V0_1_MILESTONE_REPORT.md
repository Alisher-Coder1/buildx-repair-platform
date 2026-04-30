# Buildx Repair Platform — Prototype v0.1 Milestone Report

## Metadata

| Field | Value |
|---|---|
| Document ID | PROTOTYPE_V0_1_MILESTONE_REPORT |
| Version | v0.1 |
| Date | 2026-04-30 |
| Branch | `feat/prototype-milestone-v0-1-report` |
| Status | DRAFT |
| Scope | Backend + Frontend Prototype Flow |
| Test Status | `45 passed` |

---

## 1. Purpose

This document fixes the first working product milestone of the Buildx Repair Platform.

The goal of this milestone is to prove that the platform can already execute a complete room calculation flow:

```text
Project
→ Room
→ Geometry
→ Execution Works
→ Material Consumption
→ Cost Placeholder
→ Procurement List
→ Frontend UI
```

This milestone is not the final product. It is a validated working prototype that proves the core product direction.

---

## 2. Current Product Capability

Prototype v0.1 supports the following user-facing flow:

```text
1. User opens prototype UI.
2. User enters room dimensions.
3. User selects room zone.
4. User selects floor, wall and ceiling coverings.
5. User clicks "Рассчитать комнату".
6. Frontend sends requests to backend API.
7. Backend calculates geometry.
8. Backend generates repair works.
9. Backend calculates required materials.
10. Backend calculates package counts.
11. Backend returns cost summary with MISSING_PRICE warning.
12. Backend returns procurement summary.
13. Frontend renders the result in readable UI.
```

---

## 3. Implemented API Path

The following endpoints are implemented and verified:

```text
GET  /api/v1/health
POST /api/v1/projects
GET  /api/v1/projects/{project_id}
POST /api/v1/projects/{project_id}/rooms
GET  /api/v1/rooms/{room_id}
GET  /api/v1/rooms/{room_id}/core-summary
GET  /api/v1/rooms/{room_id}/execution-summary
GET  /api/v1/rooms/{room_id}/material-consumption-summary
GET  /api/v1/rooms/{room_id}/cost-summary
GET  /api/v1/rooms/{room_id}/procurement-summary
GET  /prototype
```

---

## 4. Implemented Calculation Layers

### 4.1 Geometry Layer

The platform calculates:

```text
floor_area_m2
ceiling_area_m2
wall_area_m2
perimeter_m
```

Example verified room:

```text
length_m = 4.0
width_m = 3.0
height_m = 2.7
```

Expected result:

```text
floor_area_m2 = 12.0
ceiling_area_m2 = 12.0
wall_area_m2 = 37.8
perimeter_m = 14.0
```

### 4.2 Execution Summary Layer

The platform generates repair operations from:

```text
room zone
floor covering
wall covering
ceiling covering
geometry
operations_v1.json
```

Verified operation examples:

```text
Подготовка поверхности пола
Подготовка поверхности стен
Подготовка поверхности потолка
Гидроизоляция пола
Гидроизоляция стен
Штукатурка стен
Покраска потолка
Укладка плитки на стены
Укладка плитки на пол
```

### 4.3 Material Consumption Layer

The platform calculates:

```text
material quantity
base quantity
loss factor
layer count
thickness
package count
```

Verified material examples:

```text
Грунтовка
Гидроизоляция
Штукатурная смесь
Краска для потолка
Плиточный клей
Затирка
Керамогранит
```

### 4.4 Cost Summary Layer

The platform currently returns a cost placeholder with:

```text
MISSING_PRICE
```

This is accepted for Prototype v0.1 because the price catalog is not implemented yet.

Important rule:

```text
Missing price must be a warning, not a calculation blocker.
```

### 4.5 Procurement Summary Layer

The platform groups required materials into a procurement list:

```text
material
required quantity
unit
package count
purchase quantity
price status
```

---

## 5. Frontend Prototype

Frontend is implemented as a static prototype served by FastAPI:

```text
GET /prototype
```

Current frontend capabilities:

```text
room input form
zone selection
covering selection
backend health indicator
summary cards
geometry block
repair works block
material table
cost block with MISSING_PRICE explanation
procurement table
human-readable frontend/API errors
Russian labels for materials, operations, stages, surfaces and units
```

Reason for this approach:

```text
No npm setup
No separate frontend server
No CORS complexity
No build step
Fast product validation
```

---

## 6. Verification Status

Current automated test status:

```text
45 passed
```

Covered areas:

```text
API health
project API
room API
geometry calculation
artifact loader
artifact validation
execution summary
material formulas
material consumption summary
cost summary
procurement summary
prototype API smoke path
frontend prototype availability
frontend UX polish labels
```

---

## 7. Accepted Constraints of Prototype v0.1

The following limitations are accepted for this milestone:

```text
No authentication/RBAC
No user accounts
No project-level aggregation
No real price catalog
No supplier integration
No manual price input UI
No exports to PDF/Excel
No mobile app
No deployment pipeline
No production security hardening
No advanced room geometry
No doors/windows deductions
No multi-room calculation
No full design module
```

These are not bugs. They are intentionally outside Prototype v0.1.

---

## 8. Product Value Already Demonstrated

Prototype v0.1 proves that the platform can remove routine from the early repair planning process.

The user can already see:

```text
how room dimensions become geometry
how selected coverings become repair operations
how operations become materials
how materials become package counts
how package counts become procurement quantities
where price data is missing
```

This confirms the core value chain:

```text
Input
→ Rules
→ Calculation
→ Explanation
→ Procurement preparation
```

---

## 9. Architectural State

Current architecture is still suitable for fast MVP evolution:

```text
FastAPI backend
SQLite runtime database
JSON artifacts as rule/catalog source
deterministic calculation engines
pytest coverage
static frontend prototype
GitHub branch/PR workflow
```

Key architecture principle remains valid:

```text
Do not expand documentation endlessly.
Use documentation to support implementation, not to delay implementation.
```

---

## 10. Risks

| Risk | Status | Mitigation |
|---|---|---|
| Price data missing | Accepted | Add price input/catalog in next stage |
| Static frontend may not scale | Accepted | Replace with React/Next.js later if needed |
| JSON artifacts can become complex | Controlled | Keep validation and artifact schema discipline |
| Room model is simplified | Accepted | Add doors/windows/multi-room after MVP value is visible |
| No auth/security | Accepted | Add before external users or production deployment |

---

## 11. Recommended Next Step

The next highest-value step is:

```text
feat/price-input-and-cost-calculation
```

Purpose:

```text
Allow user to enter prices for calculated procurement items
and convert MISSING_PRICE into real cost totals.
```

Why this is the best next step:

```text
It directly increases visible product value.
It keeps scope small.
It uses existing procurement summary.
It turns the prototype from "material calculator" into "cost planning tool".
It avoids premature expansion into complex modules.
```

Alternative next step:

```text
feat/project-save-and-load-ui
```

Purpose:

```text
Improve usability by allowing users to revisit created projects and rooms.
```

Decision:

```text
Preferred: feat/price-input-and-cost-calculation
```

---

## 12. Milestone Decision

Prototype v0.1 is accepted if the following remain true:

```text
1. Full test suite passes.
2. /prototype opens.
3. User can calculate a room from UI.
4. Geometry is shown.
5. Works are shown.
6. Materials are shown.
7. Cost summary shows MISSING_PRICE.
8. Procurement summary is shown.
9. No new architecture layer is introduced without necessity.
```

Current decision:

```text
ACCEPTED AS PROTOTYPE V0.1
```
