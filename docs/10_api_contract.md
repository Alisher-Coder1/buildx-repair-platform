# 10 — API Contract

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_10 |
| File Name | `10_api_contract.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 4 — Interface Truth |
| Implementation Block | FastAPI endpoints, request/response contracts, API errors |
| Criticality | CRITICAL |
| Source of Truth Responsibility | Defines Prototype v0.1 backend API endpoints and response structures |
| Upstream Dependencies | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md`, `08_material_consumption_engine_spec.md` |
| Downstream Dependencies | FastAPI implementation, frontend integration, API tests, UI forms, summaries |

---

## 1. Purpose

This document defines the API contract for Prototype v0.1.

The API must support the first vertical slice:

```text
Project → Room → Core Summary → Execution Summary → Material Consumption Summary → Cost Summary → Procurement Summary
```

The API exposes results from domain and engine layers. It must not contain hidden business logic.

---

## 2. API Principles

```text
1. Simple enough for Prototype v0.1.
2. Deterministic.
3. Structured errors only.
4. No silent fallback.
5. Frontend must not calculate material quantities.
6. API fields must trace to Domain Model or Engine output.
7. Future auth/RBAC-ready, but not required for Prototype v0.1.
```

---

## 3. Base Path

```text
/api/v1
```

---

## 4. Standard Response Envelope

### Success

```json
{
  "success": true,
  "data": {},
  "warnings": [],
  "meta": {
    "trace_id": "optional"
  }
}
```

### Error

```json
{
  "success": false,
  "errors": [
    {
      "error_code": "ERR_REQUIRED_FIELD_MISSING",
      "message": "Required field is missing.",
      "field": "length_m",
      "entity": "Room",
      "severity": "BLOCKING",
      "details": {}
    }
  ],
  "warnings": [],
  "meta": {
    "trace_id": "optional"
  }
}
```

Rule:

```text
If blocking errors exist, API must return success=false.
```

---

## 5. HTTP Status Policy

| Situation | HTTP Status |
|---|---:|
| Successful create | 201 |
| Successful read | 200 |
| Validation error | 422 |
| Not found | 404 |
| Artifact/rule/norm calculation blocked | 422 |
| Internal error | 500 |

---

## 6. Required Error Codes

```text
ERR_REQUIRED_FIELD_MISSING
ERR_OUT_OF_RANGE
ERR_INVALID_ENUM_VALUE
ERR_EXTRA_FIELD_FORBIDDEN
ERR_UNSUPPORTED_COVERING
ERR_MATERIAL_RULE_MISSING
ERR_MATERIAL_NORM_MISSING
ERR_PACKAGE_SIZE_MISSING
ERR_INVALID_QUANTITY
ERR_ARTIFACT_FILE_MISSING
ERR_ARTIFACT_JSON_INVALID
ERR_ARTIFACT_DUPLICATE_ID
ERR_ARTIFACT_REFERENCE_INVALID
ERR_ARTIFACT_REQUIRED_FIELD_MISSING
ERR_ARTIFACT_INVALID_ENUM_VALUE
ERR_INTERNAL_CALCULATION_ERROR
ERR_NOT_FOUND
```

---

## 7. Endpoint Summary

| Method | Endpoint | Purpose | Prototype |
|---|---|---|---:|
| POST | `/api/v1/projects` | Create project | yes |
| GET | `/api/v1/projects/{project_id}` | Get project | yes |
| POST | `/api/v1/projects/{project_id}/rooms` | Create room | yes |
| GET | `/api/v1/rooms/{room_id}` | Get room | yes |
| GET | `/api/v1/rooms/{room_id}/core-summary` | Geometry/core summary | yes |
| GET | `/api/v1/rooms/{room_id}/execution-summary` | Generated operations | yes |
| GET | `/api/v1/rooms/{room_id}/material-consumption-summary` | Material quantities/packages | yes |
| GET | `/api/v1/rooms/{room_id}/cost-summary` | Basic cost summary | yes |
| GET | `/api/v1/rooms/{room_id}/procurement-summary` | Purchase list | yes |
| GET | `/api/v1/health` | Health check | recommended |

Optional after prototype core:

```text
GET /api/v1/projects/{project_id}/material-consumption-summary
GET /api/v1/projects/{project_id}/cost-summary
GET /api/v1/projects/{project_id}/procurement-summary
```

---

## 8. POST /api/v1/projects

### Request

```json
{
  "project_name": "Apartment Renovation"
}
```

### Validation

```text
project_name required
project_name must not be empty
extra fields forbidden
```

### Success — 201

```json
{
  "success": true,
  "data": {
    "project_id": "uuid",
    "project_name": "Apartment Renovation",
    "status": "DRAFT",
    "created_at": "2026-04-29T00:00:00Z",
    "updated_at": "2026-04-29T00:00:00Z"
  },
  "warnings": [],
  "meta": {}
}
```

---

## 9. GET /api/v1/projects/{project_id}

### Success — 200

```json
{
  "success": true,
  "data": {
    "project_id": "uuid",
    "project_name": "Apartment Renovation",
    "status": "DRAFT",
    "rooms": [],
    "created_at": "2026-04-29T00:00:00Z",
    "updated_at": "2026-04-29T00:00:00Z"
  },
  "warnings": [],
  "meta": {}
}
```

### Not Found — 404

```json
{
  "success": false,
  "errors": [
    {
      "error_code": "ERR_NOT_FOUND",
      "message": "Project not found.",
      "field": "project_id",
      "entity": "Project",
      "severity": "BLOCKING",
      "details": {}
    }
  ],
  "warnings": [],
  "meta": {}
}
```

---

## 10. POST /api/v1/projects/{project_id}/rooms

### Request

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

### Validation

```text
project_id must exist
room_name required
0.5 <= length_m <= 100.0
0.5 <= width_m <= 100.0
0.5 <= height_m <= 10.0
zone must be DRY/WET/KITCHEN
floor_covering must be valid floor coating
wall_covering must be valid wall coating
ceiling_covering must be valid ceiling coating
extra fields forbidden
```

### Success — 201

```json
{
  "success": true,
  "data": {
    "room_id": "uuid",
    "project_id": "uuid",
    "room_name": "Bathroom",
    "length_m": 4.0,
    "width_m": 3.0,
    "height_m": 2.7,
    "zone": "WET",
    "floor_covering": "COATING_FLOOR_PORCELAIN_TILE",
    "wall_covering": "COATING_WALL_CERAMIC_TILE",
    "ceiling_covering": "COATING_CEILING_WATER_BASED_PAINT",
    "status": "READY_FOR_CALCULATION"
  },
  "warnings": [],
  "meta": {}
}
```

---

## 11. GET /api/v1/rooms/{room_id}

Returns stored room input data.

---

## 12. GET /api/v1/rooms/{room_id}/core-summary

### Success — 200

```json
{
  "success": true,
  "data": {
    "room_id": "uuid",
    "room_name": "Bathroom",
    "zone": "WET",
    "geometry": {
      "length_m": 4.0,
      "width_m": 3.0,
      "height_m": 2.7,
      "floor_area_m2": 12.0,
      "ceiling_area_m2": 12.0,
      "perimeter_m": 14.0,
      "wall_area_m2": 37.8
    },
    "coverings": {
      "floor_covering": "COATING_FLOOR_PORCELAIN_TILE",
      "wall_covering": "COATING_WALL_CERAMIC_TILE",
      "ceiling_covering": "COATING_CEILING_WATER_BASED_PAINT"
    }
  },
  "warnings": [],
  "meta": {}
}
```

---

## 13. GET /api/v1/rooms/{room_id}/execution-summary

Returns generated operations.

Minimal operation item:

```json
{
  "operation_id": "OPR_FLOOR_PREP",
  "operation_name": "Floor surface preparation",
  "stage": "STG_PREP",
  "surface_type": "FLOOR",
  "quantity": 12.0,
  "unit": "M2",
  "source_rule_id": "generated-or-artifact-rule-id",
  "sort_order": 100,
  "is_required": true,
  "warnings": []
}
```

---

## 14. GET /api/v1/rooms/{room_id}/material-consumption-summary

Returns material quantities and package counts.

Minimal material item:

```json
{
  "item_id": "generated-id",
  "source_operation_id": "OPR_WALL_PAINT",
  "rule_id": "RULE_WALL_PAINT",
  "material_id": "MAT_PAINT_WALLS",
  "material_name": "Wall paint",
  "formula_type": "LAYER_BASED",
  "base_quantity": 37.8,
  "calculated_quantity": 12.47,
  "unit": "LITER",
  "loss_factor": 1.1,
  "layer_count": 2,
  "thickness_mm": null,
  "package_id": "PKG_PAINT_WALLS_10L",
  "package_size": 10,
  "package_count": 2,
  "warnings": []
}
```

Blocking calculation errors must return 422 with `success=false`.

---

## 15. GET /api/v1/rooms/{room_id}/cost-summary

Prototype cost is simple and may show missing prices as warnings.

Minimal cost item:

```json
{
  "cost_item_id": "generated-id",
  "material_id": "MAT_PAINT_WALLS",
  "material_name": "Wall paint",
  "package_count": 2,
  "unit_price": null,
  "currency": "USD",
  "total_price": null,
  "price_status": "MISSING_PRICE"
}
```

Missing price is a warning, not a blocking material calculation error.

---

## 16. GET /api/v1/rooms/{room_id}/procurement-summary

Returns purchase list.

Minimal procurement item:

```json
{
  "procurement_item_id": "generated-id",
  "material_id": "MAT_PAINT_WALLS",
  "material_name": "Wall paint",
  "required_quantity": 12.47,
  "unit": "LITER",
  "package_id": "PKG_PAINT_WALLS_10L",
  "package_size": 10,
  "package_count": 2,
  "purchase_quantity": 20,
  "source_operation_ids": ["OPR_WALL_PAINT"],
  "estimated_total_price": null,
  "price_status": "MISSING_PRICE"
}
```

---

## 17. GET /api/v1/health

### Success — 200

```json
{
  "success": true,
  "data": {
    "status": "ok",
    "service": "buildx-repair-platform-api",
    "version": "prototype_v0.1"
  },
  "warnings": [],
  "meta": {}
}
```

---

## 18. Dependency Rules

```text
Core Summary uses Room + RoomGeometry.
Execution Summary uses Room + RoomGeometry + operations/coatings artifacts.
Material Consumption Summary uses ExecutionSummary + material artifacts + Material Engine.
Cost Summary uses MaterialConsumptionSummary and must not recalculate quantities.
Procurement Summary uses MaterialConsumptionSummary and must not recalculate formulas.
```

---

## 19. Frontend Contract Rules

Frontend may:

```text
create project
create room
show summaries
show warnings/errors
```

Frontend must not:

```text
calculate material quantities
calculate package counts
hide backend errors
invent missing rules
```

---

## 20. Required API Tests

```text
POST /projects success
POST /projects missing project_name
GET /projects/{project_id} not found
POST room success
POST room invalid dimensions
POST room invalid covering
GET core-summary returns expected geometry
GET execution-summary returns operations
GET material-consumption-summary returns package_count
GET material-consumption-summary returns missing rule error
GET cost-summary handles missing price as warning
GET procurement-summary returns purchase_quantity
GET health returns ok
```

---

## 21. Acceptance Criteria

This document is accepted if:

```text
1. It defines all required prototype endpoints.
2. It defines request/response envelopes.
3. It defines error envelope.
4. It defines HTTP status policy.
5. It maps API to Domain Model and Engine outputs.
6. It prevents frontend business logic.
7. It supports writing FastAPI routes and Pydantic schemas.
8. It supports writing API tests.
```

---

## 22. Freeze Criteria

This document can be frozen when:

```text
1. Domain Model is accepted.
2. JSON Artifacts spec is accepted.
3. Material Engine spec is accepted.
4. Required endpoints are approved.
5. Error envelope is approved.
6. Frontend can be built from this contract.
```

---

## 23. Change Rules

After freeze:

```text
Any endpoint change requires Change Request.
Any response shape change requires Change Request.
Any error envelope change requires Change Request.
Any new required field requires Domain Model review.
Any new calculation field requires Engine spec review.
```
