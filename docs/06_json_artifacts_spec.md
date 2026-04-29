# 06 — JSON Artifacts Specification

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_06 |
| File Name | `06_json_artifacts_spec.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 2 — Artifact Truth |
| Implementation Block | JSON artifacts, rule catalogs, material norms, operation-material rules |
| Criticality | CRITICAL |
| Source of Truth Responsibility | Defines machine-readable artifact files used by prototype engines |
| Directly Related Documents | `02_mvp_scope.md`, `05_domain_model.md`, `07_execution_engine_spec.md`, `08_material_consumption_engine_spec.md`, `09_cost_and_procurement_spec.md`, `10_api_contract.md`, `12_testing_and_release_spec.md`, `26_validation_and_error_handling_spec.md`, `33_catalog_and_rules_governance_spec.md` |
| Upstream Dependencies | `02_mvp_scope.md`, `05_domain_model.md` |
| Downstream Dependencies | Execution Engine, Material Consumption Engine, Cost/Procurement summaries, validation tests |
| Duplication Check | This document defines artifact structure and reference integrity, not engine algorithms or API responses |
| Conflict Check | Engine specs must use these artifacts instead of hardcoding rules |

---

## 1. Purpose

This document defines the JSON artifacts required for Prototype v0.1.

The goal is to make the platform rule-driven instead of hardcoding repair logic into backend code.

The first prototype must load rules, materials, coverings, norms, operations and package data from JSON artifacts.

---

## 2. Why JSON Artifacts Exist

The platform must not calculate repair logic from scattered `if/else` statements.

Instead, the code should work as deterministic engines that read:

```text
coatings
materials
packages
operations
material norms
operation-material rules
```

This gives us:

```text
faster prototype implementation
easier testing
clearer debugging
future catalog expansion
better AI/developer readability
less hardcoded business logic
```

---

## 3. Required Artifact Files for Prototype v0.1

Minimum required files:

```text
data/artifacts/artifact_manifest_v1.json
data/artifacts/coatings_v1.json
data/artifacts/materials_v1.json
data/artifacts/packages_v1.json
data/artifacts/operations_v1.json
data/artifacts/material_norms_v1.json
data/artifacts/operation_material_rules_v1.json
```

Optional / future:

```text
data/artifacts/recipes_v1.json
```

---

## 4. Global Artifact Rules

### 4.1 ID Rules

All IDs must be stable, uppercase where practical, and machine-readable.

Examples:

```text
COATING_FLOOR_LAMINATE
MAT_PRIMER
OPR_FLOOR_LAMINATE_INSTALL
NORM_PRIMER_DEFAULT
RULE_PRIMER_WALL_PAINT_DRY
PKG_PRIMER_10L
```

### 4.2 Version Rules

Every artifact file must include:

```json
{
  "artifact_name": "example",
  "artifact_version": "v1",
  "prototype_version": "prototype_v0.1"
}
```

### 4.3 No Silent Fallback Rule

If an artifact reference is missing, the system must return structured error.

Examples:

```text
missing material_id → ERR_MATERIAL_NORM_MISSING or artifact validation error
missing rule_id → ERR_MATERIAL_RULE_MISSING
missing package_id where package is required → ERR_PACKAGE_SIZE_MISSING
```

### 4.4 Reference Integrity

Artifact loader must validate:

```text
operation_material_rules.material_id exists in materials_v1.json
operation_material_rules.norm_id exists in material_norms_v1.json
operation_material_rules.package_id exists in packages_v1.json when present
operation_material_rules.coating_id exists in coatings_v1.json
operation_material_rules.operation_id exists in operations_v1.json
```

---

## 5. Artifact: artifact_manifest_v1.json

### 5.1 Responsibility

Tracks artifact versions and required files.

### 5.2 Required Fields

```json
{
  "artifact_set_id": "BUILDX_ARTIFACTS_PROTO_V01",
  "artifact_set_version": "v1",
  "prototype_version": "prototype_v0.1",
  "required_files": [],
  "created_at": "YYYY-MM-DD",
  "status": "DRAFT"
}
```

### 5.3 Acceptance Criteria

```text
all required artifact files are listed
artifact versions are explicit
prototype version is explicit
```

---

## 6. Artifact: coatings_v1.json

### 6.1 Responsibility

Defines selectable coverings by surface.

### 6.2 Required Fields per Coating

| Field | Type | Required | Notes |
|---|---|---:|---|
| `coating_id` | string | yes | Stable ID |
| `surface_type` | enum | yes | FLOOR/WALLS/CEILING |
| `display_name` | string | yes | User-facing name |
| `prototype_enabled` | bool | yes | Selectable in Prototype v0.1 |
| `is_active` | bool | yes | Active in catalog |

### 6.3 Required Prototype Coverings

Floor:

```text
LAMINATE
PORCELAIN_TILE
LINOLEUM
SELF_LEVELING_FLOOR
```

Walls:

```text
VINYL_WALLPAPER
NON_WOVEN_WALLPAPER
WATER_BASED_PAINT
CERAMIC_TILE
DECORATIVE_PLASTER
```

Ceiling:

```text
WHITEWASH
WATER_BASED_PAINT
STRETCH_CEILING
```

---

## 7. Artifact: materials_v1.json

### 7.1 Responsibility

Defines material catalog references used by material rules and norms.

### 7.2 Required Fields per Material

| Field | Type | Required | Notes |
|---|---|---:|---|
| `material_id` | string | yes | Stable material ID |
| `material_name` | string | yes | User-facing name |
| `default_unit` | enum | yes | KG/LITER/M2/M_LINEAR/ROLL |
| `prototype_enabled` | bool | yes | Used in Prototype v0.1 |
| `is_active` | bool | yes | Active material |

---

## 8. Artifact: packages_v1.json

### 8.1 Responsibility

Defines package sizes used for purchase/package count.

### 8.2 Required Fields per Package

| Field | Type | Required | Notes |
|---|---|---:|---|
| `package_id` | string | yes | Stable package ID |
| `material_id` | string | yes | Related material |
| `package_size` | decimal | yes | Package amount |
| `package_unit` | enum | yes | Unit of package size |
| `display_name` | string | yes | User-facing package |
| `is_default` | bool | yes | Default package |
| `is_active` | bool | yes | Active package |

---

## 9. Artifact: operations_v1.json

### 9.1 Responsibility

Defines operation definitions that Execution Engine may generate.

### 9.2 Required Fields per Operation

| Field | Type | Required | Notes |
|---|---|---:|---|
| `operation_id` | string | yes | Stable operation ID |
| `operation_name` | string | yes | User-facing name |
| `stage` | enum | yes | STG_PREP/STG_WATERPROOF/STG_ROUGH/STG_FINISH |
| `surface_type` | enum | yes | FLOOR/WALLS/CEILING |
| `quantity_source` | enum | yes | floor_area_m2/wall_area_m2/ceiling_area_m2/perimeter_m |
| `default_unit` | enum | yes | M2/M_LINEAR/PCS |
| `sort_order` | integer | yes | Deterministic order |
| `is_active` | bool | yes | Active operation |

---

## 10. Artifact: material_norms_v1.json

### 10.1 Responsibility

Defines consumption norms used by Material Consumption Engine.

### 10.2 Required Fields per Norm

| Field | Type | Required | Notes |
|---|---|---:|---|
| `norm_id` | string | yes | Stable norm ID |
| `material_id` | string | yes | Related material |
| `formula_type` | enum | yes | AREA_BASED/LAYER_BASED/THICKNESS_BASED/LINEAR_BASED |
| `consumption_norm` | decimal | conditional | Area/layer formula |
| `q_per_mm` | decimal | conditional | Thickness formula |
| `default_layer_count` | integer | conditional | Layer-based |
| `default_loss_factor` | decimal | yes | Waste coefficient |
| `unit` | enum | yes | Output unit |
| `is_active` | bool | yes | Active norm |

---

## 11. Artifact: operation_material_rules_v1.json

### 11.1 Responsibility

Maps operation context to material consumption.

This is the most important rule artifact.

A weak rule using only operation + surface is forbidden.

Minimum key:

```text
operation_id + surface_type + coating_id + zone
```

### 11.2 Required Fields per Rule

| Field | Type | Required | Notes |
|---|---|---:|---|
| `rule_id` | string | yes | Stable rule ID |
| `operation_id` | string | yes | Operation requiring material |
| `surface_type` | enum | yes | FLOOR/WALLS/CEILING |
| `coating_id` | string | yes | Selected coating |
| `zone` | enum | yes | DRY/WET/KITCHEN/ANY |
| `material_id` | string | yes | Required material |
| `norm_id` | string | yes | Material norm |
| `formula_type` | enum | yes | Formula to apply |
| `layer_count` | integer | conditional | If formula uses layers |
| `thickness_mm` | decimal | conditional | If formula uses thickness |
| `loss_factor` | decimal | yes | Applied loss factor |
| `package_id` | string | conditional | For purchase packaging |
| `is_required` | bool | yes | Required material |
| `is_active` | bool | yes | Active rule |

### 11.3 Missing Rule Behavior

If an operation should produce material consumption but no matching rule exists:

```text
ERR_MATERIAL_RULE_MISSING
```

---

## 12. Artifact Loader Requirements

The backend artifact loader must:

```text
load all required files
validate JSON syntax
validate required top-level keys
validate unique IDs
validate reference integrity
validate formula-specific required fields
return structured errors
never silently ignore invalid artifacts
```

---

## 13. Formula-Specific Validation

### 13.1 AREA_BASED / LAYER_BASED

Required:

```text
consumption_norm
default_loss_factor or rule loss_factor
unit
```

### 13.2 THICKNESS_BASED

Required:

```text
q_per_mm
thickness_mm
loss_factor
unit
```

### 13.3 LINEAR_BASED

Required:

```text
consumption_norm or direct linear coefficient
loss_factor
unit
```

### 13.4 PACKAGE_COUNT

Required:

```text
package_id
package_size
package_unit
```

---

## 14. Artifact Validation Errors

Required errors:

```text
ERR_ARTIFACT_FILE_MISSING
ERR_ARTIFACT_JSON_INVALID
ERR_ARTIFACT_DUPLICATE_ID
ERR_ARTIFACT_REFERENCE_INVALID
ERR_ARTIFACT_REQUIRED_FIELD_MISSING
ERR_ARTIFACT_INVALID_ENUM_VALUE
ERR_MATERIAL_RULE_MISSING
ERR_MATERIAL_NORM_MISSING
ERR_PACKAGE_SIZE_MISSING
```

These should be mapped into the validation/error handling layer.

---

## 15. MVP vs Future Boundary

### Prototype v0.1

Required:

```text
coatings
materials
packages
operations
material norms
operation-material rules
```

### Future

```text
recipes
supplier offers
rental offers
pricing catalogs
regional market data
engineering catalogs
smart-home device catalogs
HVAC equipment catalogs
```

Future artifacts must not be required for Prototype v0.1.

---

## 16. Starter Artifact Files

This phase includes starter JSON files under:

```text
data/artifacts/
```

These files are not final production catalogs.  
They are prototype seeds to accelerate backend implementation and testing.

Included starter files:

```text
artifact_manifest_v1.json
coatings_v1.json
materials_v1.json
packages_v1.json
operations_v1.json
material_norms_v1.json
operation_material_rules_v1.json
```

---

## 17. Testability Notes

Required artifact tests:

```text
all files exist
all JSON files parse
all IDs are unique
all operation_material_rules references are valid
all material rules have material_id
all material rules have norm_id
all material rules that need package count have package_id
missing rule returns ERR_MATERIAL_RULE_MISSING
missing norm returns ERR_MATERIAL_NORM_MISSING
missing package returns ERR_PACKAGE_SIZE_MISSING
```

---

## 18. Acceptance Criteria

This document is accepted if:

```text
1. It defines all required Prototype v0.1 artifact files.
2. It defines required fields for each artifact type.
3. It defines reference integrity rules.
4. It defines artifact validation errors.
5. It forbids silent fallback.
6. It separates Prototype artifacts from Future artifacts.
7. It provides starter artifact files for backend acceleration.
8. It supports writing artifact loader tests.
```

---

## 19. Freeze Criteria

This document can be frozen when:

```text
1. Domain model is accepted.
2. Starter artifacts parse correctly.
3. Reference integrity can be checked.
4. Material Engine spec can use these artifacts.
5. API contract can expose outputs based on these artifacts.
```

---

## 20. Change Rules

After freeze:

```text
Any new artifact file requires Change Request.
Any new required field requires Change Request.
Any change to rule key structure requires Change Request.
Any deletion of prototype material/coating/operation requires review.
```

---

## 21. Open Questions

```text
1. Should starter artifacts include CEMENT and ALABASTER now?
2. Should recipe mode be added to starter artifacts or delayed?
3. Should project-level material aggregation be supported in Prototype v0.1?
```

Current recommendation:

```text
Delay recipe mode.
Keep CEMENT and ALABASTER optional.
Implement room-level summaries first.
```
