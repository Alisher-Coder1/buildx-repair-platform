# 05 — Domain Model

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_05 |
| File Name | `05_domain_model.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 2 — Domain Truth |
| Implementation Block | Domain entities, fields, enums, relationships, backend schemas |
| Criticality | CRITICAL |
| Source of Truth Responsibility | Defines Prototype v0.1 domain entities and their responsibilities |
| Directly Related Documents | `02_mvp_scope.md`, `04_system_architecture.md`, `06_json_artifacts_spec.md`, `07_execution_engine_spec.md`, `08_material_consumption_engine_spec.md`, `09_cost_and_procurement_spec.md`, `10_api_contract.md`, `26_validation_and_error_handling_spec.md`, `55_database_schema_migrations_and_data_integrity_spec.md` |
| Upstream Dependencies | `02_mvp_scope.md`, `04_system_architecture.md` |
| Downstream Dependencies | API schemas, database schema, validation layer, engines, tests, frontend types |
| Duplication Check | This document must not define full API payload examples, detailed database migrations, full JSON artifact schemas, or formula algorithms |
| Conflict Check | API, DB, JSON artifacts and engines must not introduce entities or fields that contradict this document |

---

## 1. Purpose

This document fixes the domain model for Prototype v0.1 of the Buildx Repair Platform.

It turns the MVP scope into concrete entities, fields, enums and relationships so that the next implementation layers can be built without guessing:

```text
Pydantic schemas
SQLAlchemy models
FastAPI endpoints
JSON artifacts
validation rules
calculation engines
frontend TypeScript types
tests
```

This is not a complete model of the future production platform. It is the minimum domain model needed for the first working vertical slice.

---

## 2. Scope

### 2.1 In Scope for Prototype v0.1

```text
Project
Room
RoomGeometry
RoomZone
SurfaceType
Covering selection
Operation
ExecutionSummary
Material
MaterialNorm
OperationMaterialRule
PackageSpec
MaterialConsumptionItem
MaterialConsumptionSummary
CostItem
CostSummary
ProcurementItem
ProcurementSummary
ValidationError
ErrorResponse
```

### 2.2 Out of Scope for Prototype v0.1

```text
Client
Contractor
Supplier
Rental
Mobile App User
Payment
Subscription
Legal Contract
Detailed Engineering System
HVAC Design
Smart Home Scenario
Door/Window Installation Logic
Calendar Scheduling
```

### 2.3 Reserved for Future

These names are reserved and must not be implemented deeply in Prototype v0.1:

```text
Client
Contractor
Supplier
Opening
Door
Window
EngineeringPoint
Fixture
FurnitureItem
Equipment
Tool
RentalOffer
SmartDevice
HVACDevice
HeatingSystem
Approval
ChangeOrder
FileEvidence
```

---

## 3. Modeling Principles

```text
1. Room is the primary calculation unit.
2. Geometry is derived from room dimensions.
3. Surface types are fixed: FLOOR, WALLS, CEILING.
4. Coverings are selected from controlled enums/artifacts.
5. Operations are generated deterministically.
6. Material consumption is rule-driven.
7. Cost must not recalculate quantities.
8. Procurement must aggregate calculated material/package needs.
9. Missing rule, norm or package must return structured error.
10. UI must not contain business calculation logic.
```

---

## 4. Core Entity Map

```text
Project
└── Room
    ├── RoomGeometry
    ├── Surface/Covering Selection
    ├── ExecutionSummary
    │   └── Operation[]
    ├── MaterialConsumptionSummary
    │   └── MaterialConsumptionItem[]
    ├── CostSummary
    │   └── CostItem[]
    ├── ProcurementSummary
    │   └── ProcurementItem[]
    └── ValidationError[]
```

External rule/catalog references:

```text
Coating
Material
MaterialNorm
PackageSpec
OperationDefinition
OperationMaterialRule
```

These references come from JSON artifacts and must not be hardcoded as business logic in code.

---

## 5. Entity: Project

### Responsibility

`Project` groups one or more rooms and project-level summaries.

Prototype v0.1 may support the structure for multiple rooms, but project-level aggregation is optional until explicitly implemented.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `project_id` | UUID/string | yes | System-generated unique identifier |
| `project_name` | string | yes | User-visible name |
| `status` | `ProjectStatus` | yes | Default: `DRAFT` |
| `created_at` | datetime | yes | System-generated |
| `updated_at` | datetime | yes | System-generated |
| `rooms` | `Room[]` | optional | May be returned only by detail endpoint |

### Enum: ProjectStatus

```text
DRAFT
IN_PROGRESS
CALCULATED
ARCHIVED
```

Prototype v0.1 minimally uses:

```text
DRAFT
CALCULATED
```

### Validation Rules

```text
project_name is required
project_name must not be empty
project_id must be unique
```

### Not Included

```text
client_id
contract_id
billing_plan
company_id
multi-tenant ownership
```

---

## 6. Entity: Room

### Responsibility

`Room` is the main calculation unit for Prototype v0.1.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `room_id` | UUID/string | yes | System-generated |
| `project_id` | UUID/string | yes | Parent project |
| `room_name` | string | yes | User-visible name |
| `length_m` | decimal | yes | Room length in meters |
| `width_m` | decimal | yes | Room width in meters |
| `height_m` | decimal | yes | Room height in meters |
| `zone` | `RoomZone` | yes | `DRY`, `WET`, `KITCHEN` |
| `floor_covering` | `FloorCovering` | yes | Selected floor covering |
| `wall_covering` | `WallCovering` | yes | Selected wall covering |
| `ceiling_covering` | `CeilingCovering` | yes | Selected ceiling covering |
| `status` | `RoomStatus` | yes | Derived or stored |
| `created_at` | datetime | yes | System-generated |
| `updated_at` | datetime | yes | System-generated |

### Enum: RoomZone

```text
DRY
WET
KITCHEN
```

### Enum: RoomStatus

```text
DRAFT
MISSING_REQUIRED_DATA
READY_FOR_CALCULATION
CALCULATED
BLOCKED_BY_VALIDATION
```

### Dimension Validation

```text
0.5 <= length_m <= 100.0
0.5 <= width_m <= 100.0
0.5 <= height_m <= 10.0
```

### Required Validation

```text
length_m is required
width_m is required
height_m is required
zone is required
floor_covering is required
wall_covering is required
ceiling_covering is required
coverings must match allowed enum values
```

---

## 7. Value Object: RoomGeometry

### Responsibility

`RoomGeometry` provides calculated geometry values for engines.

### Fields

| Field | Type | Required | Formula |
|---|---|---:|---|
| `floor_area_m2` | decimal | yes | `length_m * width_m` |
| `ceiling_area_m2` | decimal | yes | `length_m * width_m` |
| `perimeter_m` | decimal | yes | `2 * (length_m + width_m)` |
| `wall_area_m2` | decimal | yes | `perimeter_m * height_m` |

### Rounding

```text
Display rounding: 2 decimals
Internal calculation: may keep higher precision
```

### Ownership

`RoomGeometry` belongs to Room and must not exist independently.

---

## 8. Surface and Covering Model

### Enum: SurfaceType

```text
FLOOR
WALLS
CEILING
```

### Enum: FloorCovering

```text
LAMINATE
PORCELAIN_TILE
LINOLEUM
SELF_LEVELING_FLOOR
```

### Enum: WallCovering

```text
VINYL_WALLPAPER
NON_WOVEN_WALLPAPER
WATER_BASED_PAINT
CERAMIC_TILE
DECORATIVE_PLASTER
```

### Enum: CeilingCovering

```text
WHITEWASH
WATER_BASED_PAINT
STRETCH_CEILING
```

### Coating Reference

`Coating` metadata belongs to JSON artifacts.

Minimum referenced fields:

| Field | Type | Required | Notes |
|---|---|---:|---|
| `coating_id` | string | yes | Enum-compatible ID |
| `surface_type` | `SurfaceType` | yes | Floor/walls/ceiling |
| `display_name` | string | yes | User-facing name |
| `is_active` | bool | yes | Whether selectable |
| `prototype_enabled` | bool | yes | Whether enabled for Prototype v0.1 |

Full artifact schema belongs to `06_json_artifacts_spec.md`.

---

## 9. Entity: Operation

### Responsibility

`Operation` represents a generated repair work item.

Operations are generated by Execution Engine based on room, zone, surface and selected covering.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `operation_id` | string | yes | Stable operation identifier |
| `operation_name` | string | yes | User-facing name |
| `stage` | `StageCode` | yes | Repair stage |
| `surface_type` | `SurfaceType` | yes | Related surface |
| `quantity` | decimal | yes | Operation quantity |
| `unit` | `QuantityUnit` | yes | `M2`, `M_LINEAR`, `PCS` |
| `source_rule_id` | string | yes | Rule that generated operation |
| `sort_order` | integer | yes | Deterministic order |
| `is_required` | bool | yes | Required or optional |
| `warnings` | string[] | optional | Optional warnings |

### Enum: StageCode

```text
STG_PREP
STG_WATERPROOF
STG_ROUGH
STG_FINISH
```

### Enum: QuantityUnit

```text
M2
M_LINEAR
PCS
KG
LITER
PACKAGE
```

Prototype operations mostly use:

```text
M2
M_LINEAR
PCS
```

### Operation Quantity Source

Operation quantity must come from one of:

```text
floor_area_m2
ceiling_area_m2
wall_area_m2
perimeter_m
constant quantity
```

Detailed operation generation belongs to `07_execution_engine_spec.md`.

---

## 10. Entity: ExecutionSummary

### Responsibility

`ExecutionSummary` is the deterministic result of operation generation for a room.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `room_id` | UUID/string | yes | Related room |
| `operations` | `Operation[]` | yes | Generated operations |
| `validation_errors` | `ValidationError[]` | optional | Blocking errors |
| `warnings` | string[] | optional | Non-blocking warnings |
| `generated_at` | datetime | yes | Generation timestamp |
| `artifact_version` | string | yes | Rule artifact version |

### Rule

If blocking validation errors exist, dependent material/cost/procurement summaries must not silently generate incomplete results.

---

## 11. Entity: Material

### Responsibility

`Material` is a catalog reference used for material consumption.

Material metadata belongs primarily to JSON artifacts.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `material_id` | string | yes | Stable material ID |
| `material_name` | string | yes | User-facing name |
| `default_unit` | `MaterialUnit` | yes | Base calculation unit |
| `is_active` | bool | yes | Active material |
| `prototype_enabled` | bool | yes | Included in Prototype v0.1 |

### Enum: MaterialUnit

```text
KG
LITER
M2
M_LINEAR
PCS
ROLL
PACKAGE
```

### Prototype Material IDs

Required:

```text
PRIMER
PAINT_WALLS
PAINT_CEILING
PUTTY
PLASTER_MIX
WATERPROOFING
TILE_ADHESIVE
GROUT
LAMINATE
LINOLEUM
PORCELAIN_TILE
CERAMIC_TILE
WALLPAPER
SKIRTING
SELF_LEVELING_MIX
```

Optional:

```text
CEMENT
ALABASTER
```

---

## 12. Entity: MaterialNorm

### Responsibility

`MaterialNorm` defines consumption norm for a material.

The detailed JSON structure belongs to `06_json_artifacts_spec.md`.  
The formula behavior belongs to `08_material_consumption_engine_spec.md`.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `norm_id` | string | yes | Stable norm ID |
| `material_id` | string | yes | Referenced material |
| `formula_type` | `FormulaType` | yes | Calculation mode |
| `consumption_norm` | decimal | conditional | Used for area/layer formulas |
| `q_per_mm` | decimal | conditional | Used for thickness formulas |
| `default_layer_count` | integer | conditional | Default layers |
| `default_loss_factor` | decimal | yes | Example: `1.10` |
| `unit` | `MaterialUnit` | yes | Output unit |
| `is_active` | bool | yes | Active norm |

### Enum: FormulaType

```text
AREA_BASED
LAYER_BASED
THICKNESS_BASED
LINEAR_BASED
PACKAGE_COUNT
RECIPE_BASED
```

Prototype v0.1 must support:

```text
AREA_BASED
LAYER_BASED
THICKNESS_BASED
LINEAR_BASED
PACKAGE_COUNT
```

`RECIPE_BASED` is reserved unless cement/alabaster recipe mode is implemented.

---

## 13. Entity: OperationMaterialRule

### Responsibility

`OperationMaterialRule` links operation context to required material.

A weak rule like:

```text
operation + surface
```

is not enough.

Minimum rule key must support:

```text
operation_id
surface_type
coating_id
zone
```

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `rule_id` | string | yes | Stable rule ID |
| `operation_id` | string | yes | Source operation |
| `surface_type` | `SurfaceType` | yes | Floor/walls/ceiling |
| `coating_id` | string | yes | Selected covering |
| `zone` | `RoomZone` | yes | DRY/WET/KITCHEN |
| `material_id` | string | yes | Required material |
| `norm_id` | string | yes | Consumption norm |
| `formula_type` | `FormulaType` | yes | Formula to use |
| `layer_count` | integer | conditional | Formula-dependent |
| `thickness_mm` | decimal | conditional | Formula-dependent |
| `loss_factor` | decimal | yes | Waste coefficient |
| `package_id` | string | conditional | Required if package count is expected |
| `is_required` | bool | yes | Required or optional |
| `is_active` | bool | yes | Active rule |

### Missing Rule Behavior

If operation requires material consumption and matching rule does not exist:

```text
ERR_MATERIAL_RULE_MISSING
```

The system must not return empty material summary.

---

## 14. Entity: PackageSpec

### Responsibility

`PackageSpec` defines purchasable package size for material.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `package_id` | string | yes | Stable package ID |
| `material_id` | string | yes | Related material |
| `package_size` | decimal | yes | Size of one package |
| `package_unit` | `MaterialUnit` | yes | Unit of package size |
| `display_name` | string | yes | Example: `25 kg bag` |
| `is_default` | bool | yes | Default package |
| `is_active` | bool | yes | Active package |

### Missing Package Behavior

If package count is required but package size is missing:

```text
ERR_PACKAGE_SIZE_MISSING
```

---

## 15. Entity: MaterialConsumptionItem

### Responsibility

Represents calculated material quantity for one operation/material pair.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `item_id` | string | yes | Generated item ID |
| `room_id` | UUID/string | yes | Related room |
| `source_operation_id` | string | yes | Operation that caused material need |
| `rule_id` | string | yes | Material rule used |
| `material_id` | string | yes | Material |
| `material_name` | string | yes | User-facing name |
| `formula_type` | `FormulaType` | yes | Formula used |
| `base_quantity` | decimal | yes | Area/linear/base input |
| `calculated_quantity` | decimal | yes | Quantity before package rounding |
| `unit` | `MaterialUnit` | yes | Quantity unit |
| `loss_factor` | decimal | yes | Applied loss factor |
| `layer_count` | integer | conditional | If applicable |
| `thickness_mm` | decimal | conditional | If applicable |
| `package_id` | string | conditional | If package exists |
| `package_size` | decimal | conditional | If package exists |
| `package_count` | integer | conditional | Calculated via ceil |
| `warnings` | string[] | optional | Non-blocking warnings |

### Rule

`calculated_quantity` must not be zero unless calculation genuinely results in zero and is allowed by rule.

---

## 16. Entity: MaterialConsumptionSummary

### Responsibility

Aggregates material consumption items for a room.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `room_id` | UUID/string | yes | Related room |
| `items` | `MaterialConsumptionItem[]` | yes | Calculated items |
| `errors` | `ValidationError[]` | optional | Blocking calculation errors |
| `warnings` | string[] | optional | Warnings |
| `calculated_at` | datetime | yes | Calculation timestamp |
| `artifact_version` | string | yes | Artifact version used |

### Blocking Rule

If blocking errors exist, cost and procurement summaries must not pretend to be complete.

---

## 17. Entity: CostItem

### Responsibility

Represents calculated cost for a material/procurement line.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `cost_item_id` | string | yes | Generated ID |
| `room_id` | UUID/string | yes | Related room |
| `material_id` | string | yes | Related material |
| `package_count` | integer | conditional | If packaged |
| `unit_price` | decimal | conditional | Manual/basic price |
| `currency` | string | yes | Prototype default may be configured |
| `total_price` | decimal | conditional | Calculated |
| `price_status` | `PriceStatus` | yes | Known/missing/manual |

### Enum: PriceStatus

```text
MISSING_PRICE
MANUAL_PRICE
CATALOG_PRICE
```

Prototype v0.1 uses:

```text
MISSING_PRICE
MANUAL_PRICE
```

---

## 18. Entity: CostSummary

### Responsibility

Aggregates room/project cost.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `room_id` | UUID/string | yes | Related room |
| `items` | `CostItem[]` | yes | Cost items |
| `material_total` | decimal | conditional | Sum of known material prices |
| `labor_total` | decimal | optional | Placeholder in Prototype v0.1 |
| `grand_total` | decimal | conditional | Sum of known totals |
| `currency` | string | yes | Default currency |
| `errors` | `ValidationError[]` | optional | Blocking errors |
| `warnings` | string[] | optional | Missing prices etc. |

### Rule

Missing price is not a calculation failure, but must be visible as warning/status.

---

## 19. Entity: ProcurementItem

### Responsibility

Represents what the user needs to buy.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `procurement_item_id` | string | yes | Generated ID |
| `room_id` | UUID/string | yes | Related room |
| `material_id` | string | yes | Material |
| `material_name` | string | yes | User-facing name |
| `required_quantity` | decimal | yes | Calculated quantity |
| `unit` | `MaterialUnit` | yes | Base unit |
| `package_id` | string | conditional | Package |
| `package_size` | decimal | conditional | Package size |
| `package_count` | integer | conditional | Packages to buy |
| `purchase_quantity` | decimal | yes | Usually `package_count * package_size` |
| `source_operation_ids` | string[] | yes | Operations requiring this material |
| `estimated_total_price` | decimal | optional | If prices exist |
| `price_status` | `PriceStatus` | yes | Missing/manual/catalog |

### Aggregation Rule

Procurement items should aggregate same material/package combinations where possible.

---

## 20. Entity: ProcurementSummary

### Responsibility

Aggregates procurement items for room/project.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `room_id` | UUID/string | yes | Related room |
| `items` | `ProcurementItem[]` | yes | Purchase list |
| `estimated_total` | decimal | optional | If prices exist |
| `currency` | string | yes | Default currency |
| `errors` | `ValidationError[]` | optional | Blocking errors |
| `warnings` | string[] | optional | Missing price/package warnings |

---

## 21. Entity: ValidationError

### Responsibility

Represents structured error returned by validation layer or engine.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `error_code` | `ErrorCode` | yes | Stable machine code |
| `message` | string | yes | Human-readable message |
| `field` | string | optional | Related input field |
| `entity` | string | optional | Related entity |
| `severity` | `ErrorSeverity` | yes | Blocking/warning |
| `details` | object | optional | Structured details |
| `source_document` | string | optional | Spec source if useful |

### Enum: ErrorSeverity

```text
BLOCKING
WARNING
INFO
```

### Enum: ErrorCode

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
ERR_INTERNAL_CALCULATION_ERROR
```

Detailed validation behavior belongs to `26_validation_and_error_handling_spec.md`.

---

## 22. Entity: ErrorResponse

### Responsibility

Standard API-level error response.

### Fields

| Field | Type | Required | Notes |
|---|---|---:|---|
| `success` | bool | yes | Must be `false` |
| `errors` | `ValidationError[]` | yes | One or more errors |
| `warnings` | `ValidationError[]` | optional | Non-blocking warnings |
| `trace_id` | string | optional | For diagnostics |

Full API format belongs to `10_api_contract.md`.

---

## 23. Relationship Rules

```text
Project has many Rooms.
Room belongs to one Project.
Room has one derived RoomGeometry.
Room may have one generated ExecutionSummary.
ExecutionSummary contains many Operations.
Operation may generate zero or more MaterialConsumptionItems.
MaterialConsumptionSummary depends on ExecutionSummary.
CostSummary depends on MaterialConsumptionSummary.
ProcurementSummary depends on MaterialConsumptionSummary.
ValidationError can be attached to any summary or response.
```

---

## 24. Prototype Data Flow

```text
Input:
Project + Room + Dimensions + Zone + Coverings

Derived:
RoomGeometry

Generated:
ExecutionSummary

Calculated:
MaterialConsumptionSummary

Calculated/aggregated:
CostSummary
ProcurementSummary

Validated:
ValidationError[]
```

---

## 25. Mapping to JSON Artifacts

| Domain Concept | JSON Artifact |
|---|---|
| `Coating` | `coatings_v1.json` |
| `Material` | `materials_v1.json` |
| `PackageSpec` | `packages_v1.json` |
| `OperationDefinition` | `operations_v1.json` |
| `MaterialNorm` | `material_norms_v1.json` |
| `OperationMaterialRule` | `operation_material_rules_v1.json` |
| `Recipe` | `recipes_v1.json` optional/future |

This document defines concepts and required references.  
JSON structure belongs to `06_json_artifacts_spec.md`.

---

## 26. Mapping to API

| Domain Entity | Expected API Use |
|---|---|
| `Project` | `POST /projects`, `GET /projects/{project_id}` |
| `Room` | `POST /projects/{project_id}/rooms`, `GET /rooms/{room_id}` |
| `RoomGeometry` | `GET /rooms/{room_id}/core-summary` |
| `ExecutionSummary` | `GET /rooms/{room_id}/execution-summary` |
| `MaterialConsumptionSummary` | `GET /rooms/{room_id}/material-consumption-summary` |
| `CostSummary` | `GET /rooms/{room_id}/cost-summary` |
| `ProcurementSummary` | `GET /rooms/{room_id}/procurement-summary` |
| `ErrorResponse` | All endpoints |

Detailed request/response contracts belong to `10_api_contract.md`.

---

## 27. Mapping to Database

This document does not define final physical database schema.

Prototype v0.1 should prefer the simplest reliable implementation:

```text
store Project and Room
load JSON artifacts
calculate summaries on request
```

Generated summaries may be:

```text
calculated on request
cached in future
stored as snapshots in future
```

Detailed tables, migrations and data integrity belong to:

```text
55_database_schema_migrations_and_data_integrity_spec.md
```

---

## 28. MVP vs Future Entity Boundary

| Entity | Prototype v0.1 | Future |
|---|---:|---:|
| Project | yes | expanded |
| Room | yes | expanded |
| RoomGeometry | yes | expanded |
| Surface/Covering | yes | expanded catalogs |
| Operation | yes | expanded sequencing |
| Material | yes | expanded catalog |
| MaterialNorm | yes | expanded governance |
| OperationMaterialRule | yes | expanded rule engine |
| PackageSpec | yes | supplier packages |
| CostItem/Summary | yes | advanced pricing |
| ProcurementItem/Summary | yes | suppliers/orders |
| ValidationError | yes | observability |
| Client | no | yes |
| Contractor | no | yes |
| Supplier | no | yes |
| Opening/Door/Window | no | yes |
| EngineeringPoint | no | yes |
| Fixture/Furniture/Equipment | no | yes |
| SmartDevice/HVAC/Heating | no | yes |

---

## 29. Testability Notes

This domain model must support tests for:

```text
Project creation
Room creation
Room dimension validation
Room geometry calculation
Allowed zone enums
Allowed covering enums
Execution operation structure
Material consumption item structure
Cost summary structure
Procurement summary structure
Structured validation errors
No silent fallback
```

---

## 30. Acceptance Criteria

This document is accepted if:

```text
1. It defines all Prototype v0.1 entities.
2. It defines required fields for each entity.
3. It separates MVP entities from future entities.
4. It defines required enums.
5. It defines relationships between entities.
6. It explains mapping to JSON artifacts.
7. It explains mapping to API without duplicating API contract.
8. It explains mapping to database without duplicating DB schema spec.
9. It supports writing Pydantic schemas and SQLAlchemy models.
10. It supports writing tests without oral clarification.
```

---

## 31. Freeze Criteria

This document can be frozen when:

```text
1. `02_mvp_scope.md` is accepted.
2. All Prototype v0.1 entities are approved.
3. No required backend entity is missing.
4. No future entity is accidentally required for Prototype v0.1.
5. `06_json_artifacts_spec.md` can be written from this model.
6. `10_api_contract.md` can be written from this model.
```

---

## 32. Change Rules

After freeze:

```text
Any new entity requires Change Request.
Any new enum value requires Change Request.
Any new required field requires Change Request.
Any API field not traceable to this document must be rejected.
Any JSON artifact concept not traceable to this document must be reviewed.
```

---

## 33. Open Questions

```text
1. Should project-level summaries be implemented in Prototype v0.1 or only room-level summaries?
2. Should labor cost remain placeholder or be excluded completely from Prototype v0.1?
3. Should CEMENT and ALABASTER be included in Prototype v0.1 or moved to Prototype v0.2?
```

Current recommendation:

```text
Implement room-level summaries first.
Keep project-level summaries optional.
Keep labor cost as placeholder only.
Move CEMENT and ALABASTER to optional unless recipe mode is implemented.
```
