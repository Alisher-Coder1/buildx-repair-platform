# 08 — Material Consumption Engine Specification

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_08 |
| File Name | `08_material_consumption_engine_spec.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 3 — Calculation Truth |
| Implementation Block | Material Consumption Engine, formulas, packages, calculation errors |
| Criticality | CRITICAL |
| Source of Truth Responsibility | Defines how material quantities and package counts are calculated for Prototype v0.1 |
| Directly Related Documents | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md`, `07_execution_engine_spec.md`, `09_cost_and_procurement_spec.md`, `10_api_contract.md`, `12_testing_and_release_spec.md`, `26_validation_and_error_handling_spec.md`, `29_calculation_versioning_and_traceability_spec.md` |
| Upstream Dependencies | `02_mvp_scope.md`, `05_domain_model.md`, `06_json_artifacts_spec.md` |
| Downstream Dependencies | Cost Engine, Procurement Summary, API summaries, frontend results, tests |
| Duplication Check | This document defines calculation logic only. It must not redefine API response format, DB schema, UI layout, supplier logic, or full cost engine. |
| Conflict Check | Cost and Procurement must consume this engine output and must not recalculate material quantities independently. |

---

## 1. Purpose

This document defines the Material Consumption Engine for Prototype v0.1.

This is the core engine of the platform.

The engine must answer:

```text
How much material is required?
In what unit?
Which operation caused the requirement?
Which rule and norm were used?
How many packages must be purchased?
What errors block the calculation?
```

The result of this engine is later used by:

```text
Cost Summary
Procurement Summary
Reports
UI Results Dashboard
Tests
```

---

## 2. Engine Scope

### 2.1 In Scope for Prototype v0.1

The engine must support:

```text
AREA_BASED calculation
LAYER_BASED calculation
THICKNESS_BASED calculation
LINEAR_BASED calculation
PACKAGE_COUNT calculation
loss_factor
operation-to-material rules
missing rule errors
missing norm errors
missing package errors
room-level summary
```

### 2.2 Out of Scope for Prototype v0.1

The engine must not implement:

```text
supplier selection
real-time prices
rental calculation
warehouse stock
delivery optimization
taxes
discounts
complex recipe mode
manufacturer-specific advanced rules
multi-country norms
AI-based guessing of missing norms
```

### 2.3 Future-Ready But Not Implemented

Reserved for future:

```text
RECIPE_BASED formulas
partial wall height formulas
door/window area deductions
opening deductions
multi-layer wall systems
supplier-specific package variants
regional norms
manufacturer catalog import
```

---

## 3. Inputs

The engine receives:

```text
Room
RoomGeometry
ExecutionSummary.operations[]
JSON artifacts:
- materials_v1.json
- packages_v1.json
- material_norms_v1.json
- operation_material_rules_v1.json
```

Minimum required input objects:

```text
Room:
- room_id
- zone
- selected floor/wall/ceiling coverings

RoomGeometry:
- floor_area_m2
- ceiling_area_m2
- perimeter_m
- wall_area_m2

Operation:
- operation_id
- surface_type
- quantity
- unit
- stage
- source_rule_id
```

---

## 4. Outputs

The engine returns `MaterialConsumptionSummary`.

### 4.1 MaterialConsumptionSummary

Required fields:

```text
room_id
items[]
errors[]
warnings[]
calculated_at
artifact_version
```

### 4.2 MaterialConsumptionItem

Required fields:

```text
item_id
room_id
source_operation_id
rule_id
material_id
material_name
formula_type
base_quantity
calculated_quantity
unit
loss_factor
layer_count
thickness_mm
package_id
package_size
package_count
warnings[]
```

---

## 5. Rule Matching

### 5.1 Rule Key

The engine must match material rules by this context:

```text
operation_id
surface_type
coating_id
zone
```

This is required.

Weak matching by only:

```text
operation_id + surface_type
```

is forbidden.

### 5.2 Matching Priority

Because `ANY` is allowed in starter artifacts, matching priority must be deterministic:

```text
1. Exact operation_id + surface_type + exact coating_id + exact zone
2. Exact operation_id + surface_type + exact coating_id + ANY zone
3. Exact operation_id + surface_type + ANY coating_id + exact zone
4. Exact operation_id + surface_type + ANY coating_id + ANY zone
```

### 5.3 No Rule Found

If no rule is found for an operation that should produce material consumption:

```text
ERR_MATERIAL_RULE_MISSING
```

The engine must not silently skip required material consumption.

---

## 6. Norm Resolution

After matching an `OperationMaterialRule`, the engine must resolve:

```text
material_id
norm_id
package_id if package calculation is required
```

### 6.1 Missing Material

If `material_id` does not exist:

```text
ERR_ARTIFACT_REFERENCE_INVALID
```

### 6.2 Missing Norm

If `norm_id` does not exist:

```text
ERR_MATERIAL_NORM_MISSING
```

### 6.3 Missing Package

If package count is required but `package_id` or package size is missing:

```text
ERR_PACKAGE_SIZE_MISSING
```

---

## 7. Base Quantity Selection

The operation already carries quantity from Execution Engine.

However, for clarity, operation quantities must trace to one of:

```text
floor_area_m2
ceiling_area_m2
wall_area_m2
perimeter_m
constant quantity
```

The Material Engine must use operation quantity as `base_quantity`.

It must not recalculate geometry independently.

---

## 8. Formula Types

### 8.1 AREA_BASED

Used when material quantity is proportional to area.

Formula:

```text
material_quantity = base_quantity * consumption_norm * loss_factor
```

If `layer_count` is provided and formula is treated as layered:

```text
material_quantity = base_quantity * consumption_norm * layer_count * loss_factor
```

Required fields:

```text
base_quantity
consumption_norm
loss_factor
```

Optional:

```text
layer_count
```

---

### 8.2 LAYER_BASED

Used for paint, primer layers, waterproofing layers.

Formula:

```text
material_quantity = base_quantity * consumption_norm * layer_count * loss_factor
```

Required fields:

```text
base_quantity
consumption_norm
layer_count
loss_factor
```

---

### 8.3 THICKNESS_BASED

Used for plaster, putty, self-leveling mix and similar materials.

Formula:

```text
material_quantity = base_quantity * q_per_mm * thickness_mm * loss_factor
```

Required fields:

```text
base_quantity
q_per_mm
thickness_mm
loss_factor
```

---

### 8.4 LINEAR_BASED

Used for skirting boards and other linear materials.

Formula:

```text
material_quantity = base_quantity * consumption_norm * loss_factor
```

Required fields:

```text
base_quantity
consumption_norm
loss_factor
```

Here `base_quantity` is usually `perimeter_m`.

---

### 8.5 PACKAGE_COUNT

Package count must be calculated for purchasable materials.

Formula:

```text
package_count = ceil(material_quantity / package_size)
```

Rules:

```text
package_count must be integer
package_count must never be less than 1 if material_quantity > 0
package_size must be greater than 0
```

---

## 9. Rounding Rules

### 9.1 Internal Precision

Internal calculations may keep high precision.

### 9.2 Display Precision

Displayed quantities:

```text
calculated_quantity: 2 decimals
base_quantity: 2 decimals
package_count: integer
```

### 9.3 Procurement Quantity

For procurement:

```text
purchase_quantity = package_count * package_size
```

Procurement rounding belongs to Procurement Summary, but the package count comes from this engine.

---

## 10. Loss Factor Rules

`loss_factor` is mandatory.

Examples:

```text
1.05 = 5% reserve
1.10 = 10% reserve
```

Priority:

```text
1. rule.loss_factor
2. norm.default_loss_factor
3. error if neither exists
```

No implicit default is allowed.

If missing:

```text
ERR_REQUIRED_FIELD_MISSING
```

---

## 11. Calculation Algorithm

The engine must execute this deterministic algorithm:

```text
1. Receive Room + RoomGeometry + ExecutionSummary.
2. Load artifact set.
3. Validate artifacts.
4. For each operation:
   4.1 Determine selected coating for operation surface.
   4.2 Match OperationMaterialRule using matching priority.
   4.3 If rule missing, return ERR_MATERIAL_RULE_MISSING.
   4.4 Resolve material.
   4.5 Resolve norm.
   4.6 Resolve package if required.
   4.7 Select formula_type.
   4.8 Compute material_quantity.
   4.9 Compute package_count.
   4.10 Create MaterialConsumptionItem.
5. Aggregate items into MaterialConsumptionSummary.
6. Return summary with errors/warnings.
```

---

## 12. Multi-Material Operations

Some operations produce more than one material.

Example:

```text
floor tile installation
→ porcelain tile
→ tile adhesive
→ grout
```

The engine must support multiple rules for the same operation.

It must create one `MaterialConsumptionItem` per matched material rule.

---

## 13. Error Handling

### 13.1 Blocking Errors

Blocking errors:

```text
ERR_MATERIAL_RULE_MISSING
ERR_MATERIAL_NORM_MISSING
ERR_PACKAGE_SIZE_MISSING
ERR_ARTIFACT_REFERENCE_INVALID
ERR_REQUIRED_FIELD_MISSING
ERR_INVALID_QUANTITY
ERR_INTERNAL_CALCULATION_ERROR
```

If blocking errors exist, the summary must include errors and should not be treated as complete.

### 13.2 Warnings

Warnings may include:

```text
MISSING_PRICE
OPTIONAL_MATERIAL_SKIPPED
FUTURE_RULE_NOT_IMPLEMENTED
```

Warnings do not block material quantity calculation.

---

## 14. No Silent Fallback Policy

The engine must never:

```text
assume a default norm
assume a default package size
return zero if rule is missing
skip unknown material silently
guess formula type
guess thickness
guess layer count
```

If data is missing, return structured error.

---

## 15. Required Prototype Materials

The engine must support these material IDs from artifacts:

```text
MAT_PRIMER
MAT_PAINT_WALLS
MAT_PAINT_CEILING
MAT_PUTTY
MAT_PLASTER_MIX
MAT_WATERPROOFING
MAT_TILE_ADHESIVE
MAT_GROUT
MAT_LAMINATE
MAT_LINOLEUM
MAT_PORCELAIN_TILE
MAT_CERAMIC_TILE
MAT_WALLPAPER
MAT_SKIRTING
MAT_SELF_LEVELING_MIX
```

Optional/future:

```text
MAT_CEMENT
MAT_ALABASTER
```

---

## 16. Required Numerical Test Scenarios

These scenarios must be used in backend tests.

Base test room:

```text
length_m = 4.0
width_m = 3.0
height_m = 2.7

floor_area_m2 = 12.00
ceiling_area_m2 = 12.00
perimeter_m = 14.00
wall_area_m2 = 37.80
```

### 16.1 Wall Primer

Input:

```text
base_quantity = wall_area_m2 = 37.80
consumption_norm = 0.12 L/m2
loss_factor = 1.10
package_size = 10 L
```

Expected:

```text
calculated_quantity = 37.80 * 0.12 * 1.10 = 4.9896 L
display_quantity = 4.99 L or 5.00 L depending rounding policy
package_count = ceil(4.9896 / 10) = 1
```

Acceptance:

```text
package_count must equal 1
```

### 16.2 Wall Paint

Input:

```text
base_quantity = wall_area_m2 = 37.80
consumption_norm = 0.15 L/m2
layer_count = 2
loss_factor = 1.10
package_size = 10 L
```

Expected:

```text
calculated_quantity = 37.80 * 0.15 * 2 * 1.10 = 12.474 L
display_quantity = 12.47 L
package_count = ceil(12.474 / 10) = 2
```

### 16.3 Wall Putty

Input:

```text
base_quantity = wall_area_m2 = 37.80
q_per_mm = 1.0 kg/m2/mm
thickness_mm = 2
loss_factor = 1.10
package_size = 25 kg
```

Expected:

```text
calculated_quantity = 37.80 * 1.0 * 2 * 1.10 = 83.16 kg
package_count = ceil(83.16 / 25) = 4
```

### 16.4 Laminate

Input:

```text
base_quantity = floor_area_m2 = 12.00
consumption_norm = 1.0
loss_factor = 1.08
package_size = 2.0 m2
```

Expected:

```text
calculated_quantity = 12.00 * 1.0 * 1.08 = 12.96 m2
package_count = ceil(12.96 / 2.0) = 7
purchase_quantity = 7 * 2.0 = 14.00 m2
```

### 16.5 Skirting Board

Input:

```text
base_quantity = perimeter_m = 14.00
consumption_norm = 1.0
loss_factor = 1.05
package_size = 2.5 m
```

Expected:

```text
calculated_quantity = 14.00 * 1.0 * 1.05 = 14.70 m
package_count = ceil(14.70 / 2.5) = 6
purchase_quantity = 15.00 m
```

### 16.6 Wet Floor Waterproofing

Input:

```text
base_quantity = floor_area_m2 = 12.00
consumption_norm = 1.2 kg/m2
layer_count = 1
loss_factor = 1.10
package_size = 20 kg
```

Expected:

```text
calculated_quantity = 12.00 * 1.2 * 1 * 1.10 = 15.84 kg
package_count = ceil(15.84 / 20) = 1
```

### 16.7 Floor Tile Adhesive

Input:

```text
base_quantity = floor_area_m2 = 12.00
consumption_norm = 4.5 kg/m2
loss_factor = 1.10
package_size = 25 kg
```

Expected:

```text
calculated_quantity = 12.00 * 4.5 * 1.10 = 59.40 kg
package_count = ceil(59.40 / 25) = 3
```

### 16.8 Self-Leveling Mix

Input:

```text
base_quantity = floor_area_m2 = 12.00
q_per_mm = 1.6 kg/m2/mm
thickness_mm = 5
loss_factor = 1.10
package_size = 25 kg
```

Expected:

```text
calculated_quantity = 12.00 * 1.6 * 5 * 1.10 = 105.60 kg
package_count = ceil(105.60 / 25) = 5
```

---

## 17. Required Negative Test Scenarios

### 17.1 Missing Rule

Condition:

```text
operation exists
no matching operation_material_rule exists
```

Expected:

```text
ERR_MATERIAL_RULE_MISSING
```

### 17.2 Missing Norm

Condition:

```text
rule.norm_id does not exist
```

Expected:

```text
ERR_MATERIAL_NORM_MISSING
```

### 17.3 Missing Package

Condition:

```text
package count required
package_id missing or package_size <= 0
```

Expected:

```text
ERR_PACKAGE_SIZE_MISSING
```

### 17.4 Invalid Quantity

Condition:

```text
base_quantity <= 0
```

Expected:

```text
ERR_INVALID_QUANTITY
```

### 17.5 Missing Thickness

Condition:

```text
formula_type = THICKNESS_BASED
thickness_mm missing
```

Expected:

```text
ERR_REQUIRED_FIELD_MISSING
```

---

## 18. Output Completeness Rules

A complete material summary must contain:

```text
all generated material items
all package counts
all blocking errors if any
artifact version
calculation timestamp
source operation IDs
source material rule IDs
```

If errors exist:

```text
summary.status = BLOCKED or equivalent API-level status
```

The final status naming belongs to API contract, but this engine must expose error presence.

---

## 19. Relationship With Cost Engine

Cost Engine must use:

```text
material_id
package_count
package_id
purchase_quantity
```

Cost Engine must not recalculate material quantity.

---

## 20. Relationship With Procurement Engine

Procurement Engine must aggregate:

```text
material_id
package_id
package_count
purchase_quantity
source_operation_ids
```

Procurement Engine must not recalculate formulas.

---

## 21. Relationship With UI

UI must display:

```text
material name
calculated quantity
unit
package size
package count
source operation
errors/warnings
```

UI must not calculate material quantities.

---

## 22. Implementation Notes

Recommended module name:

```text
app/domain/material_engine.py
```

Recommended pure functions:

```text
calculate_area_based(...)
calculate_layer_based(...)
calculate_thickness_based(...)
calculate_linear_based(...)
calculate_package_count(...)
calculate_room_material_consumption(...)
```

Recommended tests:

```text
tests/test_material_engine_formulas.py
tests/test_material_engine_rules.py
tests/test_material_engine_errors.py
tests/test_material_summary.py
```

---

## 23. Acceptance Criteria

This document is accepted if:

```text
1. It defines all required formula types for Prototype v0.1.
2. It defines rule matching priority.
3. It defines norm/package resolution.
4. It defines no silent fallback behavior.
5. It defines error behavior.
6. It defines numerical test scenarios.
7. It defines relationship to cost/procurement without duplicating them.
8. It is sufficient for backend implementation of Material Consumption Engine.
```

---

## 24. Freeze Criteria

This document can be frozen when:

```text
1. `02_mvp_scope.md` is accepted.
2. `05_domain_model.md` is accepted.
3. `06_json_artifacts_spec.md` is accepted.
4. Starter artifact rules support required calculations.
5. All numerical examples are approved.
6. Required negative tests are approved.
```

---

## 25. Change Rules

After freeze:

```text
Any new formula type requires Change Request.
Any change in package_count formula requires Change Request.
Any change in rule matching priority requires Change Request.
Any new required material requires update to artifacts and tests.
```
