# Document Cards v0.1
## Document Control Metadata
| Field | Value |
|---|---|
| Document ID | DOC_CARDS_001 |
| File Name | `document_cards_v0.1.md` |
| Project Path | `docs/cards/document_cards_v0.1.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Hierarchy Level | Level 0 — Documentation Architecture / Document Planning |
| Implementation Block | Document cards, document ownership, audit preparation |
| Source of Truth Responsibility | Initial planning cards for documents `00–60` |

## 1. Purpose

This file provides a planning card for each numbered document in the Buildx Repair Platform documentation pack.

Each card defines:

- purpose;
- hierarchy level;
- implementation block;
- criticality;
- key questions;
- direct relations;
- duplication guard;
- acceptance criteria.

These cards are not a replacement for the full documents. They are the preparation layer before writing full specifications.

## 2. Summary Table

| Doc | File | Layer | Criticality | Implementation Block |
|---|---|---|---|---|
| 00 | `00_documentation_index.md` | Level 0 — Documentation Control | CRITICAL | Documentation navigation and source-of-truth map |
| 01 | `01_product_brief.md` | Level 1 — Product Truth | HIGH | Product vision and business value |
| 02 | `02_mvp_scope.md` | Level 1 — Product / MVP Truth | CRITICAL | MVP boundary and anti-chaos control |
| 03 | `03_user_flow_and_modules.md` | Level 1 — Product Workflow | HIGH | Guided user flow and workspace/module map |
| 04 | `04_system_architecture.md` | Level 2 — System Truth | CRITICAL | Backend/frontend/data/artifact architecture |
| 05 | `05_domain_model.md` | Level 2 — Domain Truth | CRITICAL | Core entities, relationships, schemas |
| 06 | `06_json_artifacts_spec.md` | Level 2 — Artifact Truth | CRITICAL | Machine-readable catalogs, rules and norms |
| 07 | `07_execution_engine_spec.md` | Level 3 — Engine Truth | CRITICAL | Work/stage/operation generation |
| 08 | `08_material_consumption_engine_spec.md` | Level 3 — Calculation Truth | CRITICAL | Material formulas, consumption, packages, recipe mode |
| 09 | `09_cost_and_procurement_spec.md` | Level 3 — Cost / Procurement Truth | CRITICAL | Cost summaries and procurement lists |
| 10 | `10_api_contract.md` | Level 4 — Interface Truth | CRITICAL | Internal API contract |
| 11 | `11_ui_ux_spec.md` | Level 4 — UX Truth | HIGH | Guided UX, screens, states, role views |
| 12 | `12_testing_and_release_spec.md` | Level 5 — Verification Truth | CRITICAL | Testing, release criteria, manifest/changelog |
| 13 | `13_document_acceptance_and_governance.md` | Level 0 — Documentation Governance | CRITICAL | Acceptance, freeze, CR process |
| 14 | `14_tooling_equipment_and_robotics_spec.md` | Level 6 — Domain Expansion | MEDIUM | Tools, equipment, robotics, economics |
| 15 | `15_engineering_layer_spec.md` | Level 6 — Engineering Domain | HIGH | Electrical, plumbing, control devices, engineering dependencies |
| 16 | `16_openings_doors_windows_spec.md` | Level 6 — Envelope Domain | HIGH | Openings, doors, windows, geometry deductions, economics |
| 17 | `17_construction_technology_and_sequencing_spec.md` | Level 3 — Technology Truth | CRITICAL | Dependencies, allowed/blocked work, quality gates |
| 18 | `18_fixtures_furniture_and_equipment_spec.md` | Level 6 — Domain Expansion | HIGH | Fixtures, furniture, appliances, guided filling order |
| 19 | `19_recommendation_and_constraint_engine_spec.md` | Level 3 — Constraint Truth | HIGH | Compatibility rules, warnings, recommendations |
| 20 | `20_hvac_ventilation_and_air_quality_spec.md` | Level 6 — Engineering Domain | MEDIUM | Ventilation, AC, air quality, equipment selection |
| 21 | `21_acoustic_thermal_and_building_physics_spec.md` | Level 6 — Building Physics Domain | MEDIUM | Soundproofing, insulation, vapor barriers |
| 22 | `22_heating_systems_spec.md` | Level 6 — Engineering Domain | MEDIUM | Heating systems, radiators, warm floors, controls |
| 23 | `23_smart_home_and_automation_spec.md` | Level 6 — Smart Engineering Domain | MEDIUM | Smart home devices, protocols, scenarios |
| 24 | `24_auxiliary_spaces_balconies_loggias_storage_spec.md` | Level 6 — Space Domain | MEDIUM | Balconies, loggias, storage, utility spaces |
| 25 | `25_accessories_hardware_and_finishing_components_spec.md` | Level 6 — Catalog Domain | MEDIUM | Skirting, thresholds, hardware, intercoms, accessories |
| 26 | `26_validation_and_error_handling_spec.md` | Level 5 — Validation Truth | CRITICAL | Validation layer, errors, warnings, no silent fallback |
| 27 | `27_development_methodology_and_coding_standards.md` | Level 5 — Implementation Discipline | CRITICAL | Programming approach, modular monolith, coding standards |
| 28 | `28_roadmap_to_mvp_and_production.md` | Level 6 — Planning / Delivery | HIGH | Roadmap, phases, production path |
| 29 | `29_calculation_versioning_and_traceability_spec.md` | Level 7 — Traceability | HIGH | Calculation versions, traces, recalculation history |
| 30 | `30_users_roles_permissions_and_access_control_spec.md` | Level 7 — Access Control | HIGH | Users, roles, permissions, RBAC |
| 31 | `31_information_security_privacy_backup_and_cyber_protection_spec.md` | Level 7 — Security / Resilience | HIGH | Security, privacy, backup, restore, cyber protection |
| 32 | `32_files_media_and_project_evidence_spec.md` | Level 7 — Data / Evidence | MEDIUM | Files, photos, media, evidence, attachment metadata |
| 33 | `33_catalog_and_rules_governance_spec.md` | Level 7 — Data Governance | HIGH | Catalog/rule updates, approval and versioning |
| 34 | `34_deployment_environments_and_operations_spec.md` | Level 7 — Operations | MEDIUM | Environments, CI/CD, deployment, rollback |
| 35 | `35_observability_logging_and_diagnostics_spec.md` | Level 7 — Operations | MEDIUM | Logs, monitoring, diagnostics, traces |
| 36 | `36_regulatory_safety_and_liability_boundaries_spec.md` | Level 7 — Safety / Liability | MEDIUM | Safety boundaries, regulatory warnings, liability limits |
| 37 | `37_units_currency_localization_and_market_adaptation_spec.md` | Level 7 — Localization | MEDIUM | Units, currencies, language, market adaptation |
| 38 | `38_change_impact_and_recalculation_spec.md` | Level 7 — Change Impact | HIGH | Change impact, outdated states, recalculation rules |
| 39 | `39_project_room_status_lifecycle_spec.md` | Level 4 — Workflow State | HIGH | Project/room lifecycle statuses |
| 40 | `40_reports_exports_and_printable_outputs_spec.md` | Level 4 — Outputs | MEDIUM | PDF/XLSX/CSV/JSON reports and print outputs |
| 41 | `41_ai_usage_boundaries_and_human_approval_spec.md` | Level 7 — AI Governance | MEDIUM | AI boundaries, human approval, deterministic rules |
| 42 | `42_performance_limits_and_scalability_spec.md` | Level 7 — Scalability | MEDIUM | Performance, limits, caching, scalability |
| 43 | `43_pricing_suppliers_and_market_data_spec.md` | Level 7 — Market Data | MEDIUM | Pricing, supplier price data, market data |
| 44 | `44_maintenance_updates_and_support_spec.md` | Level 7 — Support / Lifecycle | MEDIUM | Maintenance, updates, technical support |
| 45 | `45_documentation_writing_methodology_and_style_guide.md` | Level 0 — Documentation Writing Standard | CRITICAL | How documentation files must be written |
| 46 | `46_customer_workflow_and_client_management_spec.md` | Level 7 — Business Process | MEDIUM | Customer workflow, approvals, handover |
| 47 | `47_contractor_workflow_and_subcontractor_management_spec.md` | Level 7 — Business Process | MEDIUM | Contractor workflow, assignment, acceptance |
| 48 | `48_bugfix_improvement_and_regression_policy.md` | Level 7 — Maintenance / Quality | MEDIUM | Bugfix process, RCA, regression tests |
| 49 | `49_suppliers_procurement_and_rental_ecosystem_spec.md` | Level 7 — Supplier Ecosystem | MEDIUM | Suppliers, offers, procurement, rental |
| 50 | `50_knowledge_base_and_documentation_rag_spec.md` | Level 0 — Documentation Infrastructure | HIGH | Documentation KB, RAG, AI context packs |
| 51 | `51_multi_client_mobile_and_role_based_access_spec.md` | Level 4 — Multi-Client Access | HIGH | Web, mobile, portals, role-based reduced interfaces |
| 52 | `52_design_system_and_visual_language_spec.md` | Level 4 — Design System | MEDIUM | Visual style, UI components, design language |
| 53 | `53_external_integrations_and_api_interoperability_spec.md` | Level 7 — Integrations | MEDIUM | 1C, Bitrix24, CRM, ERP, supplier APIs, webhooks |
| 54 | `54_commercial_models_partnerships_and_monetization_spec.md` | Level 7 — Commercial Strategy | MEDIUM | Subscriptions, pricing plans, partnerships, monetization |
| 55 | `55_database_schema_migrations_and_data_integrity_spec.md` | Level 2 — Data Persistence | HIGH | DB schema, migrations, integrity, SQLite to PostgreSQL |
| 56 | `56_notifications_communications_and_activity_feed_spec.md` | Level 4 — Communication | MEDIUM | Notifications, activity feed, comments, alerts |
| 57 | `57_approvals_change_orders_and_decision_log_spec.md` | Level 7 — Approval Workflow | MEDIUM | Approvals, change orders, decision history |
| 58 | `58_product_analytics_kpi_and_usage_metrics_spec.md` | Level 7 — Product Analytics | LOW | Product metrics, KPIs, usage tracking |
| 59 | `59_user_onboarding_help_center_and_training_spec.md` | Level 4 — User Enablement | MEDIUM | Onboarding, help center, user training |
| 60 | `60_legal_contracts_financial_documents_and_e_signatures_spec.md` | Level 7 — Legal / Financial Documents | LOW | Contracts, acts, invoices, e-signatures |

---

## 3. Document Cards

## DOC_00 — `00_documentation_index.md`

### Title

Documentation Index

### Purpose

This document defines: **Documentation navigation and source-of-truth map**.

### Hierarchy Level

Level 0 — Documentation Control

### Implementation Block

Documentation navigation and source-of-truth map

### Criticality

CRITICAL

### Tags

`registry`, `navigation`, `documentation-control`

### Key Questions

- What exact responsibility does `Documentation Index` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `13`
- `45`
- `50`
- `documentation_registry_v0.1.yaml`
- `documentation_audit_question_matrix_v0.1.md`
- `documentation_dependency_map_v0.1.md`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Documentation navigation and source-of-truth map.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_01 — `01_product_brief.md`

### Title

Product Brief

### Purpose

This document defines: **Product vision and business value**.

### Hierarchy Level

Level 1 — Product Truth

### Implementation Block

Product vision and business value

### Criticality

HIGH

### Tags

`product`, `vision`, `value`

### Key Questions

- What exact responsibility does `Product Brief` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `02`
- `03`
- `28`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Product vision and business value.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_02 — `02_mvp_scope.md`

### Title

MVP Scope

### Purpose

This document defines: **MVP boundary and anti-chaos control**.

### Hierarchy Level

Level 1 — Product / MVP Truth

### Implementation Block

MVP boundary and anti-chaos control

### Criticality

CRITICAL

### Tags

`mvp`, `scope`, `anti-chaos`

### Key Questions

- What exact responsibility does `MVP Scope` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `01`
- `03`
- `04`
- `05`
- `06`
- `08`
- `12`
- `26`
- `27`
- `28`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: MVP boundary and anti-chaos control.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_03 — `03_user_flow_and_modules.md`

### Title

User Flow and Modules

### Purpose

This document defines: **Guided user flow and workspace/module map**.

### Hierarchy Level

Level 1 — Product Workflow

### Implementation Block

Guided user flow and workspace/module map

### Criticality

HIGH

### Tags

`user-flow`, `modules`, `workspace`

### Key Questions

- What exact responsibility does `User Flow and Modules` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `01`
- `02`
- `10`
- `11`
- `39`
- `51`
- `52`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Guided user flow and workspace/module map.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_04 — `04_system_architecture.md`

### Title

System Architecture

### Purpose

This document defines: **Backend/frontend/data/artifact architecture**.

### Hierarchy Level

Level 2 — System Truth

### Implementation Block

Backend/frontend/data/artifact architecture

### Criticality

CRITICAL

### Tags

`architecture`, `layers`, `modular-monolith`

### Key Questions

- What exact responsibility does `System Architecture` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `02`
- `05`
- `06`
- `10`
- `27`
- `55`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Backend/frontend/data/artifact architecture.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_05 — `05_domain_model.md`

### Title

Domain Model

### Purpose

This document defines: **Core entities, relationships, schemas**.

### Hierarchy Level

Level 2 — Domain Truth

### Implementation Block

Core entities, relationships, schemas

### Criticality

CRITICAL

### Tags

`domain-model`, `entities`, `schemas`

### Key Questions

- What exact responsibility does `Domain Model` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `04`
- `06`
- `10`
- `26`
- `55`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Core entities, relationships, schemas.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_06 — `06_json_artifacts_spec.md`

### Title

JSON Artifacts Specification

### Purpose

This document defines: **Machine-readable catalogs, rules and norms**.

### Hierarchy Level

Level 2 — Artifact Truth

### Implementation Block

Machine-readable catalogs, rules and norms

### Criticality

CRITICAL

### Tags

`json-artifacts`, `rules`, `catalogs`

### Key Questions

- What exact responsibility does `JSON Artifacts Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `07`
- `08`
- `09`
- `17`
- `26`
- `33`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Machine-readable catalogs, rules and norms.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_07 — `07_execution_engine_spec.md`

### Title

Execution Engine Specification

### Purpose

This document defines: **Work/stage/operation generation**.

### Hierarchy Level

Level 3 — Engine Truth

### Implementation Block

Work/stage/operation generation

### Criticality

CRITICAL

### Tags

`execution-engine`, `operations`, `stages`

### Key Questions

- What exact responsibility does `Execution Engine Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `06`
- `08`
- `17`
- `18`
- `26`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Work/stage/operation generation.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_08 — `08_material_consumption_engine_spec.md`

### Title

Material Consumption Engine Specification

### Purpose

This document defines: **Material formulas, consumption, packages, recipe mode**.

### Hierarchy Level

Level 3 — Calculation Truth

### Implementation Block

Material formulas, consumption, packages, recipe mode

### Criticality

CRITICAL

### Tags

`material-engine`, `formulas`, `packages`

### Key Questions

- What exact responsibility does `Material Consumption Engine Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `06`
- `07`
- `09`
- `12`
- `26`
- `29`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Material formulas, consumption, packages, recipe mode.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_09 — `09_cost_and_procurement_spec.md`

### Title

Cost and Procurement Specification

### Purpose

This document defines: **Cost summaries and procurement lists**.

### Hierarchy Level

Level 3 — Cost / Procurement Truth

### Implementation Block

Cost summaries and procurement lists

### Criticality

CRITICAL

### Tags

`cost`, `procurement`, `purchase-list`

### Key Questions

- What exact responsibility does `Cost and Procurement Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `08`
- `40`
- `43`
- `49`
- `54`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Cost summaries and procurement lists.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_10 — `10_api_contract.md`

### Title

API Contract

### Purpose

This document defines: **Internal API contract**.

### Hierarchy Level

Level 4 — Interface Truth

### Implementation Block

Internal API contract

### Criticality

CRITICAL

### Tags

`api`, `contract`, `backend-frontend`

### Key Questions

- What exact responsibility does `API Contract` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `11`
- `26`
- `30`
- `31`
- `51`
- `53`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Internal API contract.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_11 — `11_ui_ux_spec.md`

### Title

UI/UX Specification

### Purpose

This document defines: **Guided UX, screens, states, role views**.

### Hierarchy Level

Level 4 — UX Truth

### Implementation Block

Guided UX, screens, states, role views

### Criticality

HIGH

### Tags

`ui`, `ux`, `workflow`

### Key Questions

- What exact responsibility does `UI/UX Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `03`
- `10`
- `19`
- `26`
- `39`
- `51`
- `52`
- `56`
- `59`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Guided UX, screens, states, role views.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_12 — `12_testing_and_release_spec.md`

### Title

Testing and Release Specification

### Purpose

This document defines: **Testing, release criteria, manifest/changelog**.

### Hierarchy Level

Level 5 — Verification Truth

### Implementation Block

Testing, release criteria, manifest/changelog

### Criticality

CRITICAL

### Tags

`testing`, `release`, `qa`

### Key Questions

- What exact responsibility does `Testing and Release Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `02`
- `08`
- `10`
- `26`
- `27`
- `34`
- `35`
- `48`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Testing, release criteria, manifest/changelog.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_13 — `13_document_acceptance_and_governance.md`

### Title

Document Acceptance and Governance

### Purpose

This document defines: **Acceptance, freeze, CR process**.

### Hierarchy Level

Level 0 — Documentation Governance

### Implementation Block

Acceptance, freeze, CR process

### Criticality

CRITICAL

### Tags

`governance`, `freeze`, `change-request`

### Key Questions

- What exact responsibility does `Document Acceptance and Governance` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `00`
- `45`
- `documentation_audit_question_matrix_v0.1.md`
- `documentation_dependency_map_v0.1.md`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Acceptance, freeze, CR process.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_14 — `14_tooling_equipment_and_robotics_spec.md`

### Title

Tooling, Equipment and Robotics Specification

### Purpose

This document defines: **Tools, equipment, robotics, economics**.

### Hierarchy Level

Level 6 — Domain Expansion

### Implementation Block

Tools, equipment, robotics, economics

### Criticality

MEDIUM

### Tags

`tools`, `equipment`, `robotics`

### Key Questions

- What exact responsibility does `Tooling, Equipment and Robotics Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `07`
- `09`
- `17`
- `49`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Tools, equipment, robotics, economics.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_15 — `15_engineering_layer_spec.md`

### Title

Engineering Layer Specification

### Purpose

This document defines: **Electrical, plumbing, control devices, engineering dependencies**.

### Hierarchy Level

Level 6 — Engineering Domain

### Implementation Block

Electrical, plumbing, control devices, engineering dependencies

### Criticality

HIGH

### Tags

`engineering`, `electrical`, `plumbing`

### Key Questions

- What exact responsibility does `Engineering Layer Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `17`
- `20`
- `22`
- `23`
- `26`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Electrical, plumbing, control devices, engineering dependencies.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_16 — `16_openings_doors_windows_spec.md`

### Title

Openings, Doors and Windows Specification

### Purpose

This document defines: **Openings, doors, windows, geometry deductions, economics**.

### Hierarchy Level

Level 6 — Envelope Domain

### Implementation Block

Openings, doors, windows, geometry deductions, economics

### Criticality

HIGH

### Tags

`doors`, `windows`, `openings`

### Key Questions

- What exact responsibility does `Openings, Doors and Windows Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `08`
- `09`
- `23`
- `25`
- `36`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Openings, doors, windows, geometry deductions, economics.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_17 — `17_construction_technology_and_sequencing_spec.md`

### Title

Construction Technology and Sequencing Specification

### Purpose

This document defines: **Dependencies, allowed/blocked work, quality gates**.

### Hierarchy Level

Level 3 — Technology Truth

### Implementation Block

Dependencies, allowed/blocked work, quality gates

### Criticality

CRITICAL

### Tags

`sequencing`, `technology`, `quality-gates`

### Key Questions

- What exact responsibility does `Construction Technology and Sequencing Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `07`
- `15`
- `18`
- `20`
- `21`
- `22`
- `23`
- `26`
- `39`
- `47`
- `57`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Dependencies, allowed/blocked work, quality gates.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_18 — `18_fixtures_furniture_and_equipment_spec.md`

### Title

Fixtures, Furniture and Equipment Specification

### Purpose

This document defines: **Fixtures, furniture, appliances, guided filling order**.

### Hierarchy Level

Level 6 — Domain Expansion

### Implementation Block

Fixtures, furniture, appliances, guided filling order

### Criticality

HIGH

### Tags

`fixtures`, `furniture`, `appliances`

### Key Questions

- What exact responsibility does `Fixtures, Furniture and Equipment Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `15`
- `17`
- `20`
- `22`
- `23`
- `49`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Fixtures, furniture, appliances, guided filling order.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_19 — `19_recommendation_and_constraint_engine_spec.md`

### Title

Recommendation and Constraint Engine Specification

### Purpose

This document defines: **Compatibility rules, warnings, recommendations**.

### Hierarchy Level

Level 3 — Constraint Truth

### Implementation Block

Compatibility rules, warnings, recommendations

### Criticality

HIGH

### Tags

`recommendations`, `constraints`, `compatibility`

### Key Questions

- What exact responsibility does `Recommendation and Constraint Engine Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `11`
- `15`
- `16`
- `18`
- `20`
- `22`
- `23`
- `26`
- `52`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Compatibility rules, warnings, recommendations.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_20 — `20_hvac_ventilation_and_air_quality_spec.md`

### Title

HVAC, Ventilation and Air Quality Specification

### Purpose

This document defines: **Ventilation, AC, air quality, equipment selection**.

### Hierarchy Level

Level 6 — Engineering Domain

### Implementation Block

Ventilation, AC, air quality, equipment selection

### Criticality

MEDIUM

### Tags

`hvac`, `ventilation`, `air-quality`

### Key Questions

- What exact responsibility does `HVAC, Ventilation and Air Quality Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `15`
- `17`
- `19`
- `21`
- `22`
- `23`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Ventilation, AC, air quality, equipment selection.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_21 — `21_acoustic_thermal_and_building_physics_spec.md`

### Title

Acoustic, Thermal and Building Physics Specification

### Purpose

This document defines: **Soundproofing, insulation, vapor barriers**.

### Hierarchy Level

Level 6 — Building Physics Domain

### Implementation Block

Soundproofing, insulation, vapor barriers

### Criticality

MEDIUM

### Tags

`acoustics`, `insulation`, `building-physics`

### Key Questions

- What exact responsibility does `Acoustic, Thermal and Building Physics Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `08`
- `17`
- `19`
- `20`
- `22`
- `24`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Soundproofing, insulation, vapor barriers.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_22 — `22_heating_systems_spec.md`

### Title

Heating Systems Specification

### Purpose

This document defines: **Heating systems, radiators, warm floors, controls**.

### Hierarchy Level

Level 6 — Engineering Domain

### Implementation Block

Heating systems, radiators, warm floors, controls

### Criticality

MEDIUM

### Tags

`heating`, `radiators`, `warm-floor`

### Key Questions

- What exact responsibility does `Heating Systems Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `15`
- `17`
- `19`
- `20`
- `21`
- `23`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Heating systems, radiators, warm floors, controls.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_23 — `23_smart_home_and_automation_spec.md`

### Title

Smart Home and Automation Specification

### Purpose

This document defines: **Smart home devices, protocols, scenarios**.

### Hierarchy Level

Level 6 — Smart Engineering Domain

### Implementation Block

Smart home devices, protocols, scenarios

### Criticality

MEDIUM

### Tags

`smart-home`, `automation`, `protocols`

### Key Questions

- What exact responsibility does `Smart Home and Automation Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `15`
- `19`
- `20`
- `22`
- `30`
- `31`
- `51`
- `53`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Smart home devices, protocols, scenarios.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_24 — `24_auxiliary_spaces_balconies_loggias_storage_spec.md`

### Title

Auxiliary Spaces, Balconies, Loggias and Storage Specification

### Purpose

This document defines: **Balconies, loggias, storage, utility spaces**.

### Hierarchy Level

Level 6 — Space Domain

### Implementation Block

Balconies, loggias, storage, utility spaces

### Criticality

MEDIUM

### Tags

`balcony`, `loggia`, `storage`

### Key Questions

- What exact responsibility does `Auxiliary Spaces, Balconies, Loggias and Storage Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `16`
- `19`
- `21`
- `36`
- `49`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Balconies, loggias, storage, utility spaces.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_25 — `25_accessories_hardware_and_finishing_components_spec.md`

### Title

Accessories, Hardware and Finishing Components Specification

### Purpose

This document defines: **Skirting, thresholds, hardware, intercoms, accessories**.

### Hierarchy Level

Level 6 — Catalog Domain

### Implementation Block

Skirting, thresholds, hardware, intercoms, accessories

### Criticality

MEDIUM

### Tags

`accessories`, `hardware`, `finishing`

### Key Questions

- What exact responsibility does `Accessories, Hardware and Finishing Components Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `09`
- `16`
- `23`
- `49`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Skirting, thresholds, hardware, intercoms, accessories.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_26 — `26_validation_and_error_handling_spec.md`

### Title

Validation and Error Handling Specification

### Purpose

This document defines: **Validation layer, errors, warnings, no silent fallback**.

### Hierarchy Level

Level 5 — Validation Truth

### Implementation Block

Validation layer, errors, warnings, no silent fallback

### Criticality

CRITICAL

### Tags

`validation`, `errors`, `no-silent-fallback`

### Key Questions

- What exact responsibility does `Validation and Error Handling Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `06`
- `10`
- `12`
- `17`
- `19`
- `27`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Validation layer, errors, warnings, no silent fallback.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_27 — `27_development_methodology_and_coding_standards.md`

### Title

Development Methodology and Coding Standards

### Purpose

This document defines: **Programming approach, modular monolith, coding standards**.

### Hierarchy Level

Level 5 — Implementation Discipline

### Implementation Block

Programming approach, modular monolith, coding standards

### Criticality

CRITICAL

### Tags

`development`, `coding-standards`, `modular-monolith`

### Key Questions

- What exact responsibility does `Development Methodology and Coding Standards` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `04`
- `05`
- `06`
- `10`
- `12`
- `26`
- `55`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Programming approach, modular monolith, coding standards.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_28 — `28_roadmap_to_mvp_and_production.md`

### Title

Roadmap to MVP and Production

### Purpose

This document defines: **Roadmap, phases, production path**.

### Hierarchy Level

Level 6 — Planning / Delivery

### Implementation Block

Roadmap, phases, production path

### Criticality

HIGH

### Tags

`roadmap`, `mvp`, `production`

### Key Questions

- What exact responsibility does `Roadmap to MVP and Production` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `01`
- `02`
- `04`
- `12`
- `27`
- `44`
- `48`
- `50`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Roadmap, phases, production path.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_29 — `29_calculation_versioning_and_traceability_spec.md`

### Title

Calculation Versioning and Traceability Specification

### Purpose

This document defines: **Calculation versions, traces, recalculation history**.

### Hierarchy Level

Level 7 — Traceability

### Implementation Block

Calculation versions, traces, recalculation history

### Criticality

HIGH

### Tags

`traceability`, `versioning`, `calculation`

### Key Questions

- What exact responsibility does `Calculation Versioning and Traceability Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `06`
- `08`
- `09`
- `33`
- `38`
- `44`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Calculation versions, traces, recalculation history.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_30 — `30_users_roles_permissions_and_access_control_spec.md`

### Title

Users, Roles, Permissions and Access Control Specification

### Purpose

This document defines: **Users, roles, permissions, RBAC**.

### Hierarchy Level

Level 7 — Access Control

### Implementation Block

Users, roles, permissions, RBAC

### Criticality

HIGH

### Tags

`rbac`, `roles`, `permissions`

### Key Questions

- What exact responsibility does `Users, Roles, Permissions and Access Control Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `10`
- `11`
- `31`
- `46`
- `47`
- `51`
- `54`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Users, roles, permissions, RBAC.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_31 — `31_information_security_privacy_backup_and_cyber_protection_spec.md`

### Title

Information Security, Privacy, Backup and Cyber Protection Specification

### Purpose

This document defines: **Security, privacy, backup, restore, cyber protection**.

### Hierarchy Level

Level 7 — Security / Resilience

### Implementation Block

Security, privacy, backup, restore, cyber protection

### Criticality

HIGH

### Tags

`security`, `backup`, `privacy`

### Key Questions

- What exact responsibility does `Information Security, Privacy, Backup and Cyber Protection Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `30`
- `32`
- `34`
- `35`
- `53`
- `56`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Security, privacy, backup, restore, cyber protection.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_32 — `32_files_media_and_project_evidence_spec.md`

### Title

Files, Media and Project Evidence Specification

### Purpose

This document defines: **Files, photos, media, evidence, attachment metadata**.

### Hierarchy Level

Level 7 — Data / Evidence

### Implementation Block

Files, photos, media, evidence, attachment metadata

### Criticality

MEDIUM

### Tags

`files`, `media`, `evidence`

### Key Questions

- What exact responsibility does `Files, Media and Project Evidence Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `31`
- `46`
- `47`
- `56`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Files, photos, media, evidence, attachment metadata.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_33 — `33_catalog_and_rules_governance_spec.md`

### Title

Catalog and Rules Governance Specification

### Purpose

This document defines: **Catalog/rule updates, approval and versioning**.

### Hierarchy Level

Level 7 — Data Governance

### Implementation Block

Catalog/rule updates, approval and versioning

### Criticality

HIGH

### Tags

`catalog-governance`, `rules`, `versioning`

### Key Questions

- What exact responsibility does `Catalog and Rules Governance Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `06`
- `08`
- `09`
- `29`
- `43`
- `49`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Catalog/rule updates, approval and versioning.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_34 — `34_deployment_environments_and_operations_spec.md`

### Title

Deployment, Environments and Operations Specification

### Purpose

This document defines: **Environments, CI/CD, deployment, rollback**.

### Hierarchy Level

Level 7 — Operations

### Implementation Block

Environments, CI/CD, deployment, rollback

### Criticality

MEDIUM

### Tags

`deployment`, `environments`, `ops`

### Key Questions

- What exact responsibility does `Deployment, Environments and Operations Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `27`
- `31`
- `35`
- `44`
- `48`
- `55`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Environments, CI/CD, deployment, rollback.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_35 — `35_observability_logging_and_diagnostics_spec.md`

### Title

Observability, Logging and Diagnostics Specification

### Purpose

This document defines: **Logs, monitoring, diagnostics, traces**.

### Hierarchy Level

Level 7 — Operations

### Implementation Block

Logs, monitoring, diagnostics, traces

### Criticality

MEDIUM

### Tags

`observability`, `logging`, `diagnostics`

### Key Questions

- What exact responsibility does `Observability, Logging and Diagnostics Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `26`
- `29`
- `31`
- `34`
- `44`
- `48`
- `56`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Logs, monitoring, diagnostics, traces.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_36 — `36_regulatory_safety_and_liability_boundaries_spec.md`

### Title

Regulatory, Safety and Liability Boundaries Specification

### Purpose

This document defines: **Safety boundaries, regulatory warnings, liability limits**.

### Hierarchy Level

Level 7 — Safety / Liability

### Implementation Block

Safety boundaries, regulatory warnings, liability limits

### Criticality

MEDIUM

### Tags

`safety`, `regulatory`, `liability`

### Key Questions

- What exact responsibility does `Regulatory, Safety and Liability Boundaries Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `15`
- `16`
- `20`
- `22`
- `23`
- `24`
- `41`
- `46`
- `47`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Safety boundaries, regulatory warnings, liability limits.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_37 — `37_units_currency_localization_and_market_adaptation_spec.md`

### Title

Units, Currency, Localization and Market Adaptation Specification

### Purpose

This document defines: **Units, currencies, language, market adaptation**.

### Hierarchy Level

Level 7 — Localization

### Implementation Block

Units, currencies, language, market adaptation

### Criticality

MEDIUM

### Tags

`units`, `currency`, `localization`

### Key Questions

- What exact responsibility does `Units, Currency, Localization and Market Adaptation Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `08`
- `09`
- `43`
- `49`
- `54`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Units, currencies, language, market adaptation.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_38 — `38_change_impact_and_recalculation_spec.md`

### Title

Change Impact and Recalculation Specification

### Purpose

This document defines: **Change impact, outdated states, recalculation rules**.

### Hierarchy Level

Level 7 — Change Impact

### Implementation Block

Change impact, outdated states, recalculation rules

### Criticality

HIGH

### Tags

`change-impact`, `recalculation`, `outdated`

### Key Questions

- What exact responsibility does `Change Impact and Recalculation Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `05`
- `07`
- `08`
- `09`
- `17`
- `29`
- `39`
- `57`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Change impact, outdated states, recalculation rules.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_39 — `39_project_room_status_lifecycle_spec.md`

### Title

Project and Room Status Lifecycle Specification

### Purpose

This document defines: **Project/room lifecycle statuses**.

### Hierarchy Level

Level 4 — Workflow State

### Implementation Block

Project/room lifecycle statuses

### Criticality

HIGH

### Tags

`statuses`, `lifecycle`, `workflow`

### Key Questions

- What exact responsibility does `Project and Room Status Lifecycle Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `03`
- `07`
- `17`
- `26`
- `38`
- `11`
- `46`
- `47`
- `57`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Project/room lifecycle statuses.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_40 — `40_reports_exports_and_printable_outputs_spec.md`

### Title

Reports, Exports and Printable Outputs Specification

### Purpose

This document defines: **PDF/XLSX/CSV/JSON reports and print outputs**.

### Hierarchy Level

Level 4 — Outputs

### Implementation Block

PDF/XLSX/CSV/JSON reports and print outputs

### Criticality

MEDIUM

### Tags

`reports`, `exports`, `print`

### Key Questions

- What exact responsibility does `Reports, Exports and Printable Outputs Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `08`
- `09`
- `10`
- `29`
- `46`
- `49`
- `53`
- `60`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: PDF/XLSX/CSV/JSON reports and print outputs.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_41 — `41_ai_usage_boundaries_and_human_approval_spec.md`

### Title

AI Usage Boundaries and Human Approval Specification

### Purpose

This document defines: **AI boundaries, human approval, deterministic rules**.

### Hierarchy Level

Level 7 — AI Governance

### Implementation Block

AI boundaries, human approval, deterministic rules

### Criticality

MEDIUM

### Tags

`ai`, `human-approval`, `deterministic`

### Key Questions

- What exact responsibility does `AI Usage Boundaries and Human Approval Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `13`
- `26`
- `27`
- `36`
- `50`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: AI boundaries, human approval, deterministic rules.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_42 — `42_performance_limits_and_scalability_spec.md`

### Title

Performance Limits and Scalability Specification

### Purpose

This document defines: **Performance, limits, caching, scalability**.

### Hierarchy Level

Level 7 — Scalability

### Implementation Block

Performance, limits, caching, scalability

### Criticality

MEDIUM

### Tags

`performance`, `limits`, `scalability`

### Key Questions

- What exact responsibility does `Performance Limits and Scalability Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `04`
- `10`
- `27`
- `34`
- `35`
- `55`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Performance, limits, caching, scalability.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_43 — `43_pricing_suppliers_and_market_data_spec.md`

### Title

Pricing, Suppliers and Market Data Specification

### Purpose

This document defines: **Pricing, supplier price data, market data**.

### Hierarchy Level

Level 7 — Market Data

### Implementation Block

Pricing, supplier price data, market data

### Criticality

MEDIUM

### Tags

`pricing`, `market-data`, `suppliers`

### Key Questions

- What exact responsibility does `Pricing, Suppliers and Market Data Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `09`
- `33`
- `37`
- `49`
- `54`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Pricing, supplier price data, market data.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_44 — `44_maintenance_updates_and_support_spec.md`

### Title

Maintenance, Updates and Support Specification

### Purpose

This document defines: **Maintenance, updates, technical support**.

### Hierarchy Level

Level 7 — Support / Lifecycle

### Implementation Block

Maintenance, updates, technical support

### Criticality

MEDIUM

### Tags

`maintenance`, `support`, `updates`

### Key Questions

- What exact responsibility does `Maintenance, Updates and Support Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `12`
- `29`
- `33`
- `34`
- `35`
- `48`
- `59`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Maintenance, updates, technical support.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_45 — `45_documentation_writing_methodology_and_style_guide.md`

### Title

Documentation Writing Methodology and Style Guide

### Purpose

This document defines: **How documentation files must be written**.

### Hierarchy Level

Level 0 — Documentation Writing Standard

### Implementation Block

How documentation files must be written

### Criticality

CRITICAL

### Tags

`style-guide`, `documentation`, `writing`

### Key Questions

- What exact responsibility does `Documentation Writing Methodology and Style Guide` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `00`
- `13`
- `documentation_audit_question_matrix_v0.1.md`
- `documentation_dependency_map_v0.1.md`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: How documentation files must be written.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_46 — `46_customer_workflow_and_client_management_spec.md`

### Title

Customer Workflow and Client Management Specification

### Purpose

This document defines: **Customer workflow, approvals, handover**.

### Hierarchy Level

Level 7 — Business Process

### Implementation Block

Customer workflow, approvals, handover

### Criticality

MEDIUM

### Tags

`customer`, `workflow`, `client`

### Key Questions

- What exact responsibility does `Customer Workflow and Client Management Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `03`
- `09`
- `39`
- `40`
- `56`
- `57`
- `60`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Customer workflow, approvals, handover.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_47 — `47_contractor_workflow_and_subcontractor_management_spec.md`

### Title

Contractor Workflow and Subcontractor Management Specification

### Purpose

This document defines: **Contractor workflow, assignment, acceptance**.

### Hierarchy Level

Level 7 — Business Process

### Implementation Block

Contractor workflow, assignment, acceptance

### Criticality

MEDIUM

### Tags

`contractor`, `subcontractor`, `work-assignment`

### Key Questions

- What exact responsibility does `Contractor Workflow and Subcontractor Management Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `07`
- `17`
- `39`
- `56`
- `57`
- `60`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Contractor workflow, assignment, acceptance.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_48 — `48_bugfix_improvement_and_regression_policy.md`

### Title

Bugfix, Improvement and Regression Policy

### Purpose

This document defines: **Bugfix process, RCA, regression tests**.

### Hierarchy Level

Level 7 — Maintenance / Quality

### Implementation Block

Bugfix process, RCA, regression tests

### Criticality

MEDIUM

### Tags

`bugfix`, `regression`, `improvement`

### Key Questions

- What exact responsibility does `Bugfix, Improvement and Regression Policy` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `12`
- `26`
- `27`
- `35`
- `44`
- `45`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Bugfix process, RCA, regression tests.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_49 — `49_suppliers_procurement_and_rental_ecosystem_spec.md`

### Title

Suppliers, Procurement and Rental Ecosystem Specification

### Purpose

This document defines: **Suppliers, offers, procurement, rental**.

### Hierarchy Level

Level 7 — Supplier Ecosystem

### Implementation Block

Suppliers, offers, procurement, rental

### Criticality

MEDIUM

### Tags

`suppliers`, `procurement`, `rental`

### Key Questions

- What exact responsibility does `Suppliers, Procurement and Rental Ecosystem Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `09`
- `14`
- `33`
- `43`
- `53`
- `54`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Suppliers, offers, procurement, rental.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_50 — `50_knowledge_base_and_documentation_rag_spec.md`

### Title

Knowledge Base and Documentation RAG Specification

### Purpose

This document defines: **Documentation KB, RAG, AI context packs**.

### Hierarchy Level

Level 0 — Documentation Infrastructure

### Implementation Block

Documentation KB, RAG, AI context packs

### Criticality

HIGH

### Tags

`knowledge-base`, `rag`, `documentation`

### Key Questions

- What exact responsibility does `Knowledge Base and Documentation RAG Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `00`
- `13`
- `45`
- `documentation_registry_v0.1.yaml`
- `documentation_audit_question_matrix_v0.1.md`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Documentation KB, RAG, AI context packs.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_51 — `51_multi_client_mobile_and_role_based_access_spec.md`

### Title

Multi-Client, Mobile and Role-Based Access Specification

### Purpose

This document defines: **Web, mobile, portals, role-based reduced interfaces**.

### Hierarchy Level

Level 4 — Multi-Client Access

### Implementation Block

Web, mobile, portals, role-based reduced interfaces

### Criticality

HIGH

### Tags

`mobile`, `role-based-ui`, `multi-client`

### Key Questions

- What exact responsibility does `Multi-Client, Mobile and Role-Based Access Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `10`
- `11`
- `30`
- `31`
- `46`
- `47`
- `52`
- `56`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Web, mobile, portals, role-based reduced interfaces.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_52 — `52_design_system_and_visual_language_spec.md`

### Title

Design System and Visual Language Specification

### Purpose

This document defines: **Visual style, UI components, design language**.

### Hierarchy Level

Level 4 — Design System

### Implementation Block

Visual style, UI components, design language

### Criticality

MEDIUM

### Tags

`design-system`, `visual-language`, `ui-components`

### Key Questions

- What exact responsibility does `Design System and Visual Language Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `03`
- `11`
- `39`
- `51`
- `59`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Visual style, UI components, design language.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_53 — `53_external_integrations_and_api_interoperability_spec.md`

### Title

External Integrations and API Interoperability Specification

### Purpose

This document defines: **1C, Bitrix24, CRM, ERP, supplier APIs, webhooks**.

### Hierarchy Level

Level 7 — Integrations

### Implementation Block

1C, Bitrix24, CRM, ERP, supplier APIs, webhooks

### Criticality

MEDIUM

### Tags

`integrations`, `api`, `interoperability`

### Key Questions

- What exact responsibility does `External Integrations and API Interoperability Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `10`
- `30`
- `31`
- `40`
- `49`
- `54`
- `60`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: 1C, Bitrix24, CRM, ERP, supplier APIs, webhooks.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_54 — `54_commercial_models_partnerships_and_monetization_spec.md`

### Title

Commercial Models, Partnerships and Monetization Specification

### Purpose

This document defines: **Subscriptions, pricing plans, partnerships, monetization**.

### Hierarchy Level

Level 7 — Commercial Strategy

### Implementation Block

Subscriptions, pricing plans, partnerships, monetization

### Criticality

MEDIUM

### Tags

`commercial`, `monetization`, `subscriptions`

### Key Questions

- What exact responsibility does `Commercial Models, Partnerships and Monetization Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `30`
- `44`
- `46`
- `47`
- `49`
- `51`
- `53`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Subscriptions, pricing plans, partnerships, monetization.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_55 — `55_database_schema_migrations_and_data_integrity_spec.md`

### Title

Database Schema, Migrations and Data Integrity Specification

### Purpose

This document defines: **DB schema, migrations, integrity, SQLite to PostgreSQL**.

### Hierarchy Level

Level 2 — Data Persistence

### Implementation Block

DB schema, migrations, integrity, SQLite to PostgreSQL

### Criticality

HIGH

### Tags

`database`, `migrations`, `data-integrity`

### Key Questions

- What exact responsibility does `Database Schema, Migrations and Data Integrity Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `04`
- `05`
- `27`
- `29`
- `31`
- `34`
- `38`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: DB schema, migrations, integrity, SQLite to PostgreSQL.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_56 — `56_notifications_communications_and_activity_feed_spec.md`

### Title

Notifications, Communications and Activity Feed Specification

### Purpose

This document defines: **Notifications, activity feed, comments, alerts**.

### Hierarchy Level

Level 4 — Communication

### Implementation Block

Notifications, activity feed, comments, alerts

### Criticality

MEDIUM

### Tags

`notifications`, `activity-feed`, `communications`

### Key Questions

- What exact responsibility does `Notifications, Communications and Activity Feed Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `30`
- `31`
- `35`
- `39`
- `46`
- `47`
- `51`
- `57`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Notifications, activity feed, comments, alerts.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_57 — `57_approvals_change_orders_and_decision_log_spec.md`

### Title

Approvals, Change Orders and Decision Log Specification

### Purpose

This document defines: **Approvals, change orders, decision history**.

### Hierarchy Level

Level 7 — Approval Workflow

### Implementation Block

Approvals, change orders, decision history

### Criticality

MEDIUM

### Tags

`approvals`, `change-orders`, `decision-log`

### Key Questions

- What exact responsibility does `Approvals, Change Orders and Decision Log Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `38`
- `39`
- `46`
- `47`
- `56`
- `60`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Approvals, change orders, decision history.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_58 — `58_product_analytics_kpi_and_usage_metrics_spec.md`

### Title

Product Analytics, KPI and Usage Metrics Specification

### Purpose

This document defines: **Product metrics, KPIs, usage tracking**.

### Hierarchy Level

Level 7 — Product Analytics

### Implementation Block

Product metrics, KPIs, usage tracking

### Criticality

LOW

### Tags

`analytics`, `kpi`, `metrics`

### Key Questions

- What exact responsibility does `Product Analytics, KPI and Usage Metrics Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `11`
- `35`
- `44`
- `54`
- `59`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Product metrics, KPIs, usage tracking.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_59 — `59_user_onboarding_help_center_and_training_spec.md`

### Title

User Onboarding, Help Center and Training Specification

### Purpose

This document defines: **Onboarding, help center, user training**.

### Hierarchy Level

Level 4 — User Enablement

### Implementation Block

Onboarding, help center, user training

### Criticality

MEDIUM

### Tags

`onboarding`, `help-center`, `training`

### Key Questions

- What exact responsibility does `User Onboarding, Help Center and Training Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `01`
- `03`
- `11`
- `44`
- `46`
- `47`
- `52`
- `58`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Onboarding, help center, user training.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## DOC_60 — `60_legal_contracts_financial_documents_and_e_signatures_spec.md`

### Title

Legal, Contracts, Financial Documents and E-Signatures Specification

### Purpose

This document defines: **Contracts, acts, invoices, e-signatures**.

### Hierarchy Level

Level 7 — Legal / Financial Documents

### Implementation Block

Contracts, acts, invoices, e-signatures

### Criticality

LOW

### Tags

`legal`, `contracts`, `financial-docs`

### Key Questions

- What exact responsibility does `Legal, Contracts, Financial Documents and E-Signatures Specification` own?
- What belongs in MVP and what must stay Future/Post-MVP?
- Which documents constrain this document and which documents depend on it?
- What must not be duplicated from other documents?
- What acceptance criteria prove this document is ready for freeze?

### Directly Related Documents

- `31`
- `36`
- `40`
- `46`
- `47`
- `53`
- `54`
- `57`

### Duplication Guard

- Do not duplicate full requirements from upstream documents.
- Do not redefine concepts owned by Domain Model, Architecture, API Contract, or MVP Scope.
- Keep responsibility limited to: Contracts, acts, invoices, e-signatures.

### Initial Acceptance Criteria

- Purpose, scope, metadata, hierarchy level and implementation block are clear.
- Key questions are answered without ambiguity.
- MVP / Future / Out of Scope are separated.
- Direct relations, upstream/downstream dependencies, duplication and conflict checks are filled.
- A developer or AI coding agent can use the document without oral clarification.

### Current Status

```text
DRAFT — card created; full document content still pending.
```

---

## 4. Next Actions

1. Cross-check this file against `docs/documentation_registry_v0.1.yaml`.
2. Cross-check this file against `docs/audit/documentation_dependency_map_v0.1.md`.
3. Fill missing upstream/downstream dependencies in the registry.
4. Promote Tier 1 documents from card-level to full-spec level.
5. Run the audit matrix before marking any document as APPROVED or FROZEN.
