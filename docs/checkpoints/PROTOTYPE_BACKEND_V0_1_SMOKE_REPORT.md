# Prototype Backend v0.1 — Smoke Report

## Metadata

| Field | Value |
|---|---|
| Report ID | PROTOTYPE_BACKEND_V0_1_SMOKE_REPORT |
| Created | 2026-04-30 |
| Branch | `feat/prototype-api-smoke-report` |
| Status | DRAFT |
| Scope | Backend API smoke path |

---

## 1. Purpose

This report verifies the first complete backend prototype path.

The goal is not to add new business logic.

The goal is to prove that the backend can execute the core product flow end-to-end.

---

## 2. Verified API Path

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
```

---

## 3. Test Scenario

Room input:

```json
{
  "room_name": "Bathroom",
  "length_m": 4.0,
  "width_m": 3.0,
  "height_m": 2.7,
  "zone": "WET",
  "floor_covering": "COATING_FLOOR_PORCELAIN_TILE",
  "wall_covering": "COATING_WALL_CERAMIC_TILE",
  "ceiling_covering": "COATING_CEILING_WATER_BASED_PAINT"
}
```

Expected geometry:

```text
floor_area_m2 = 12.0
ceiling_area_m2 = 12.0
perimeter_m = 14.0
wall_area_m2 = 37.8
```

Expected operation categories:

```text
preparation
waterproofing
wall tile installation
floor tile installation
ceiling painting
```

Expected material categories:

```text
porcelain tile
tile adhesive
grout
waterproofing
primer / paint materials depending on artifact rules
```

Expected cost behavior:

```text
MISSING_PRICE warning
grand_total = null
```

Expected procurement behavior:

```text
purchase list exists
package_count exists
purchase_quantity exists
```

---

## 4. Acceptance Criteria

Prototype Backend v0.1 smoke path is accepted if:

```text
1. All smoke test endpoints return successful responses where expected.
2. Core geometry returns expected numeric values.
3. Execution summary returns repair operations.
4. Material consumption summary returns calculated material items.
5. Cost summary returns MISSING_PRICE warning instead of blocking.
6. Procurement summary returns grouped purchase items.
7. Full pytest suite passes.
```

---

## 5. Current Product Capability

At this milestone, backend supports:

```text
Project creation
Room creation
Geometry calculation
Artifact loading and validation
Execution summary generation
Material quantity calculation
Package count calculation
Cost summary placeholder with missing price warning
Procurement purchase list generation
```

---

## 6. Known Limits

Prototype Backend v0.1 does not yet include:

```text
frontend UI
auth/RBAC
real price catalog
supplier integration
manual price input
project-level aggregation
PDF/Excel export
production deployment
```

---

## 7. Next Recommended Stage

```text
frontend/prototype-room-flow
```

or, if backend hardening is preferred first:

```text
feat/api-polish-and-error-normalization
```
