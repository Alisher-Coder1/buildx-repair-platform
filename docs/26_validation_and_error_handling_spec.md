# 26 — Validation and Error Handling Specification

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_26 |
| File Name | `26_validation_and_error_handling_spec.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 5 — Validation Truth |
| Implementation Block | Input validation, artifact validation, engine validation, structured errors |
| Criticality | CRITICAL |
| Source of Truth Responsibility | Defines validation rules, error behavior, no silent fallback policy and error response structure |
| Directly Related Documents | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md`, `08_material_consumption_engine_spec.md`, `10_api_contract.md`, `12_testing_and_release_spec.md`, `27_development_methodology_and_coding_standards.md` |
| Upstream Dependencies | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md`, `08_material_consumption_engine_spec.md`, `10_api_contract.md` |
| Downstream Dependencies | FastAPI schemas, Pydantic validation, artifact loader, calculation engines, API tests, frontend error display |
| Duplication Check | This document defines validation and error behavior only. It must not redefine formulas, endpoint contracts, JSON artifact schemas, or UI layout. |
| Conflict Check | API and engine implementations must use these error codes and must not invent silent fallback behavior. |

---

## 1. Purpose

This document defines validation and error handling for Prototype v0.1.

Its purpose is to prevent hidden mistakes during implementation.

The system must reject invalid data, expose missing rules, expose missing norms, and never silently return incomplete or fake results.

---

## 2. Core Policy

The platform must follow this rule:

```text
No silent fallback.
```

This means the system must never:

```text
guess missing norms
guess missing package sizes
guess missing rule context
ignore invalid artifacts
return zero instead of error
return empty result instead of error
hide blocking calculation errors
let frontend invent missing backend data
```

---

## 3. Validation Layers

Prototype v0.1 has five validation layers:

```text
1. API request validation
2. Domain validation
3. JSON artifact validation
4. Engine calculation validation
5. Summary/output validation
```

Each layer must produce structured errors.

---

## 4. Error Object

All structured errors must follow this shape:

```json
{
  "error_code": "ERR_REQUIRED_FIELD_MISSING",
  "message": "Required field is missing.",
  "field": "length_m",
  "entity": "Room",
  "severity": "BLOCKING",
  "details": {}
}
```

## 4.1 Required Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `error_code` | string | yes | Stable machine-readable code |
| `message` | string | yes | Human-readable message |
| `field` | string/null | optional | Input field or artifact field |
| `entity` | string/null | optional | Entity/module name |
| `severity` | enum | yes | `BLOCKING`, `WARNING`, `INFO` |
| `details` | object | optional | Structured debug context |

---

## 5. Error Severity

### 5.1 BLOCKING

Calculation or request cannot continue.

Examples:

```text
missing required field
invalid enum
missing material rule
missing material norm
missing package size
invalid JSON artifact
```

### 5.2 WARNING

Operation can continue, but user must be informed.

Examples:

```text
missing price
optional material skipped
future rule not implemented
```

### 5.3 INFO

Non-critical informational message.

Prototype v0.1 may not use `INFO` heavily.

---

## 6. API Error Envelope

API error response must follow `10_api_contract.md`:

```json
{
  "success": false,
  "errors": [],
  "warnings": [],
  "meta": {
    "trace_id": "optional"
  }
}
```

Rule:

```text
If any BLOCKING error exists, success must be false.
```

---

## 7. Warning Envelope

Successful response with warning:

```json
{
  "success": true,
  "data": {},
  "warnings": [
    {
      "error_code": "MISSING_PRICE",
      "message": "Some material prices are missing.",
      "field": "unit_price",
      "entity": "CostSummary",
      "severity": "WARNING",
      "details": {}
    }
  ],
  "meta": {}
}
```

---

## 8. HTTP Status Policy

| Situation | HTTP Status | Severity |
|---|---:|---|
| Successful create | 201 | none |
| Successful read | 200 | none |
| Request validation error | 422 | BLOCKING |
| Domain validation error | 422 | BLOCKING |
| Artifact validation error | 422 | BLOCKING |
| Engine calculation blocked | 422 | BLOCKING |
| Not found | 404 | BLOCKING |
| Internal unexpected error | 500 | BLOCKING |

---

## 9. Required Error Codes

### 9.1 Request / Domain Errors

```text
ERR_REQUIRED_FIELD_MISSING
ERR_OUT_OF_RANGE
ERR_INVALID_ENUM_VALUE
ERR_EXTRA_FIELD_FORBIDDEN
ERR_UNSUPPORTED_COVERING
ERR_INVALID_QUANTITY
ERR_NOT_FOUND
```

### 9.2 Artifact Errors

```text
ERR_ARTIFACT_FILE_MISSING
ERR_ARTIFACT_JSON_INVALID
ERR_ARTIFACT_DUPLICATE_ID
ERR_ARTIFACT_REFERENCE_INVALID
ERR_ARTIFACT_REQUIRED_FIELD_MISSING
ERR_ARTIFACT_INVALID_ENUM_VALUE
```

### 9.3 Engine Errors

```text
ERR_MATERIAL_RULE_MISSING
ERR_MATERIAL_NORM_MISSING
ERR_PACKAGE_SIZE_MISSING
ERR_INTERNAL_CALCULATION_ERROR
```

### 9.4 Warning Codes

```text
MISSING_PRICE
OPTIONAL_MATERIAL_SKIPPED
FUTURE_RULE_NOT_IMPLEMENTED
```

---

## 10. API Request Validation

### 10.1 Project Create

Validation rules:

```text
project_name required
project_name must not be empty
extra fields forbidden
```

Errors:

```text
ERR_REQUIRED_FIELD_MISSING
ERR_EXTRA_FIELD_FORBIDDEN
```

---

## 11. Room Create Validation

Required fields:

```text
room_name
length_m
width_m
height_m
zone
floor_covering
wall_covering
ceiling_covering
```

Dimension ranges:

```text
0.5 <= length_m <= 100.0
0.5 <= width_m <= 100.0
0.5 <= height_m <= 10.0
```

Allowed zone values:

```text
DRY
WET
KITCHEN
```

Errors:

```text
ERR_REQUIRED_FIELD_MISSING
ERR_OUT_OF_RANGE
ERR_INVALID_ENUM_VALUE
ERR_UNSUPPORTED_COVERING
ERR_EXTRA_FIELD_FORBIDDEN
```

---

## 12. Covering Validation

Covering must be valid for its surface.

Examples:

```text
floor_covering must reference FLOOR coating
wall_covering must reference WALLS coating
ceiling_covering must reference CEILING coating
```

Invalid surface/coating combination:

```text
ERR_UNSUPPORTED_COVERING
```

---

## 13. Geometry Validation

Geometry must not produce invalid quantities.

Invalid cases:

```text
floor_area_m2 <= 0
ceiling_area_m2 <= 0
perimeter_m <= 0
wall_area_m2 <= 0
```

Error:

```text
ERR_INVALID_QUANTITY
```

---

## 14. JSON Artifact Validation

Artifact loader must validate:

```text
required files exist
JSON syntax is valid
top-level structure exists
items array exists
IDs are unique
required fields exist
enum values are valid
references are valid
formula-specific fields are present
package sizes are positive
```

---

## 15. Artifact Reference Validation

Required references:

```text
operation_material_rules.operation_id -> operations_v1.json
operation_material_rules.material_id -> materials_v1.json
operation_material_rules.norm_id -> material_norms_v1.json
operation_material_rules.package_id -> packages_v1.json
operation_material_rules.coating_id -> coatings_v1.json unless ANY
```

Broken reference:

```text
ERR_ARTIFACT_REFERENCE_INVALID
```

---

## 16. Duplicate ID Validation

Duplicate IDs are forbidden in:

```text
coatings
materials
packages
operations
material_norms
operation_material_rules
```

Error:

```text
ERR_ARTIFACT_DUPLICATE_ID
```

---

## 17. Formula-Specific Validation

### 17.1 AREA_BASED

Required:

```text
base_quantity > 0
consumption_norm exists and > 0
loss_factor exists and > 0
```

### 17.2 LAYER_BASED

Required:

```text
base_quantity > 0
consumption_norm exists and > 0
layer_count exists and > 0
loss_factor exists and > 0
```

### 17.3 THICKNESS_BASED

Required:

```text
base_quantity > 0
q_per_mm exists and > 0
thickness_mm exists and > 0
loss_factor exists and > 0
```

### 17.4 LINEAR_BASED

Required:

```text
base_quantity > 0
consumption_norm exists and > 0
loss_factor exists and > 0
```

### 17.5 PACKAGE_COUNT

Required:

```text
material_quantity > 0
package_size exists and > 0
```

---

## 18. Material Engine Validation

Blocking conditions:

```text
no matching operation_material_rule
rule references missing material
rule references missing norm
rule requires package but package missing
formula-specific field missing
base quantity invalid
package size invalid
```

Errors:

```text
ERR_MATERIAL_RULE_MISSING
ERR_ARTIFACT_REFERENCE_INVALID
ERR_MATERIAL_NORM_MISSING
ERR_PACKAGE_SIZE_MISSING
ERR_REQUIRED_FIELD_MISSING
ERR_INVALID_QUANTITY
```

---

## 19. Cost Summary Validation

Missing price is not a blocking error in Prototype v0.1.

Use warning:

```text
MISSING_PRICE
```

Cost Summary must not block material/procurement summary just because price is missing.

---

## 20. Procurement Summary Validation

Procurement Summary depends on package data.

Blocking conditions:

```text
package_count missing when package is required
package_size <= 0
purchase_quantity <= 0
```

Errors:

```text
ERR_PACKAGE_SIZE_MISSING
ERR_INVALID_QUANTITY
```

---

## 21. Error Handling Examples

### 21.1 Missing Room Length

```json
{
  "success": false,
  "errors": [
    {
      "error_code": "ERR_REQUIRED_FIELD_MISSING",
      "message": "Room length is required.",
      "field": "length_m",
      "entity": "Room",
      "severity": "BLOCKING",
      "details": {}
    }
  ],
  "warnings": [],
  "meta": {}
}
```

### 21.2 Invalid Covering

```json
{
  "success": false,
  "errors": [
    {
      "error_code": "ERR_UNSUPPORTED_COVERING",
      "message": "Selected covering is not valid for this surface.",
      "field": "floor_covering",
      "entity": "Room",
      "severity": "BLOCKING",
      "details": {
        "surface_type": "FLOOR",
        "coating_id": "COATING_WALL_CERAMIC_TILE"
      }
    }
  ],
  "warnings": [],
  "meta": {}
}
```

### 21.3 Missing Material Rule

```json
{
  "success": false,
  "errors": [
    {
      "error_code": "ERR_MATERIAL_RULE_MISSING",
      "message": "Material rule is missing for operation and selected context.",
      "field": "operation_material_rules",
      "entity": "MaterialConsumptionEngine",
      "severity": "BLOCKING",
      "details": {
        "operation_id": "OPR_WALL_PAINT",
        "surface_type": "WALLS",
        "coating_id": "COATING_WALL_WATER_BASED_PAINT",
        "zone": "WET"
      }
    }
  ],
  "warnings": [],
  "meta": {}
}
```

### 21.4 Missing Price Warning

```json
{
  "success": true,
  "data": {},
  "warnings": [
    {
      "error_code": "MISSING_PRICE",
      "message": "Some material prices are missing.",
      "field": "unit_price",
      "entity": "CostSummary",
      "severity": "WARNING",
      "details": {
        "material_id": "MAT_PAINT_WALLS"
      }
    }
  ],
  "meta": {}
}
```

---

## 22. Frontend Error Display Rules

Frontend must:

```text
show BLOCKING errors visibly
show WARNING messages visibly but less aggressively
not hide backend errors
not replace backend errors with generic text only
not continue blocked workflow without user understanding why
```

Frontend may translate messages later, but must preserve `error_code`.

---

## 23. Logging and Debug Notes

Prototype v0.1 may use simple logs.

Do not log:

```text
secrets
API keys
future personal data
sensitive file paths
```

Allowed logs:

```text
trace_id
endpoint
error_code
entity
field
artifact file
rule_id
operation_id
```

---

## 24. Required Negative Tests

### 24.1 Project

```text
POST /projects without project_name -> ERR_REQUIRED_FIELD_MISSING
POST /projects with extra field -> ERR_EXTRA_FIELD_FORBIDDEN
```

### 24.2 Room

```text
POST room without length_m -> ERR_REQUIRED_FIELD_MISSING
POST room with length_m < 0.5 -> ERR_OUT_OF_RANGE
POST room with invalid zone -> ERR_INVALID_ENUM_VALUE
POST room with wall coating as floor covering -> ERR_UNSUPPORTED_COVERING
POST room with extra field -> ERR_EXTRA_FIELD_FORBIDDEN
```

### 24.3 Artifacts

```text
missing artifact file -> ERR_ARTIFACT_FILE_MISSING
invalid JSON -> ERR_ARTIFACT_JSON_INVALID
duplicate ID -> ERR_ARTIFACT_DUPLICATE_ID
broken reference -> ERR_ARTIFACT_REFERENCE_INVALID
missing required artifact field -> ERR_ARTIFACT_REQUIRED_FIELD_MISSING
invalid artifact enum -> ERR_ARTIFACT_INVALID_ENUM_VALUE
```

### 24.4 Material Engine

```text
missing material rule -> ERR_MATERIAL_RULE_MISSING
missing norm -> ERR_MATERIAL_NORM_MISSING
missing package -> ERR_PACKAGE_SIZE_MISSING
invalid base quantity -> ERR_INVALID_QUANTITY
missing thickness for THICKNESS_BASED -> ERR_REQUIRED_FIELD_MISSING
```

### 24.5 Cost/Procurement

```text
missing price -> MISSING_PRICE warning
package size <= 0 -> ERR_PACKAGE_SIZE_MISSING or ERR_INVALID_QUANTITY
```

---

## 25. Implementation Notes

Recommended modules:

```text
app/core/errors.py
app/core/validation.py
app/domain/validators.py
app/artifacts/validators.py
app/api/error_handlers.py
```

Recommended tests:

```text
tests/test_request_validation.py
tests/test_artifact_validation.py
tests/test_material_engine_errors.py
tests/test_api_error_envelope.py
```

---

## 26. Acceptance Criteria

This document is accepted if:

```text
1. It defines required error shape.
2. It defines severity levels.
3. It defines HTTP status policy.
4. It defines API/domain/artifact/engine validation.
5. It defines all required Prototype v0.1 error codes.
6. It defines no silent fallback behavior.
7. It provides negative test scenarios.
8. It supports FastAPI/Pydantic implementation.
9. It supports frontend error display.
```

---

## 27. Freeze Criteria

This document can be frozen when:

```text
1. API contract is accepted.
2. Domain model is accepted.
3. JSON artifact spec is accepted.
4. Material engine spec is accepted.
5. Error codes are approved.
6. Negative tests are approved.
```

---

## 28. Change Rules

After freeze:

```text
Any new blocking error code requires Change Request.
Any error envelope change requires API contract review.
Any validation range change requires MVP/domain review.
Any artifact validation change requires JSON artifact spec review.
Any formula validation change requires Material Engine spec review.
```
