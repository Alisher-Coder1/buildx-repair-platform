# Documentation Dependency Map v0.1

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | AUDIT_DEP_MAP_001 |
| File Name | `documentation_dependency_map_v0.1.md` |
| Project Path | `docs/audit/documentation_dependency_map_v0.1.md` |
| Version | v0.1 |
| Status | DRAFT |
| Owner | Documentation Architect |
| Hierarchy Level | Level 0 — Documentation Audit / Dependency Control |
| Implementation Block | Documentation dependency audit, cross-document consistency, AI reading packs |
| Source of Truth Responsibility | Human-readable map of dependencies between documentation files |

---

## 1. Purpose

This document shows how the Buildx Repair Platform documentation files are connected.

It is used to answer:

- Which documents are directly connected?
- Which documents are upstream sources of truth?
- Which documents depend on a given document?
- Which documents must be updated together?
- Which documents may duplicate or conflict with each other?
- Which documents should be provided to a developer or AI coding agent for a specific implementation task?

This file complements:

- `docs/documentation_registry_v0.1.yaml`
- `docs/audit/documentation_audit_question_matrix_v0.1.md`
- `docs/00_documentation_index.md`

---

## 2. Relationship Types

| Relationship Type | Meaning |
|---|---|
| Primary Source of Truth | Main document responsible for a topic |
| Upstream Dependency | Higher-level document that constrains this document |
| Directly Related | Documents that must stay consistent with this document |
| Downstream Dependency | Documents/modules affected by this document |
| Conflict Risk | Documents where contradictions are likely |
| Duplication Risk | Documents where the same responsibility may be repeated incorrectly |
| AI Reading Pack | Minimal document set required for implementation/review of a module |

---

## 3. Global Hierarchy Rule

If documents conflict, use this order:

```text
Level 0 — Documentation Control
Level 1 — Product / MVP Truth
Level 2 — System / Domain / Artifact Truth
Level 3 — Engine / Calculation / Technology Truth
Level 4 — API / UI / Interface Truth
Level 5 — Validation / Testing / Development Discipline
Level 6 — Domain Expansion / Business / Operations
Level 7 — Production / Security / Integration / Commercial Strategy
```

Rule:

```text
A lower-level document must not override a higher-level document.
If a lower-level document requires a change to a higher-level decision, a Change Request is required.
```

---

## 4. Documentation Control Pack

| Document | Primary Responsibility | Directly Related | Downstream |
|---|---|---|---|
| `00_documentation_index.md` | Navigation and document structure | Registry, audit matrix, dependency map | All documents |
| `13_document_acceptance_and_governance.md` | Acceptance, freeze, change rules | `45`, audit matrix, dependency map | All documents |
| `45_documentation_writing_methodology_and_style_guide.md` | How documents must be written | Template, governance, audit matrix | All documents |
| `50_knowledge_base_and_documentation_rag_spec.md` | Documentation KB / RAG readiness | Registry, audit matrix, dependency map | AI/RAG workflows |
| `docs/audit/documentation_audit_question_matrix_v0.1.md` | Audit questions and criteria | `13`, `45`, dependency map | All audits |
| `docs/audit/documentation_dependency_map_v0.1.md` | Human-readable dependency map | `00`, `13`, registry | Cross-document audits |
| `docs/documentation_registry_v0.1.yaml` | Machine-readable document registry | Index, dependency map | AI reading packs, traceability |
| `docs/templates/document_template.md` | Standard document template | `45`, `13` | All docs |

---

## 5. Product / MVP / Roadmap Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `01_product_brief.md` | Product vision and value | `00` | `02`, `03`, `28` | Architecture, UI, roadmap |
| `02_mvp_scope.md` | MVP boundary and anti-chaos control | `01` | `04`, `05`, `06`, `08`, `12`, `26`, `27`, `28` | All MVP docs |
| `03_user_flow_and_modules.md` | User journey and workspaces | `01`, `02` | `10`, `11`, `39`, `51`, `52` | UI, API, lifecycle |
| `28_roadmap_to_mvp_and_production.md` | Roadmap to MVP and production | `01`, `02`, `04`, `12`, `27` | `44`, `48`, `50` | Delivery planning |

Conflict risks:

- `02_mvp_scope.md` must not be overridden by domain expansion documents.
- `03_user_flow_and_modules.md` must not define UI components in detail; that belongs to `11` and `52`.
- `28_roadmap_to_mvp_and_production.md` must not redefine MVP scope.

---

## 6. System Foundation Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `04_system_architecture.md` | System layers and module boundaries | `01`, `02` | `05`, `06`, `10`, `27`, `55` | All implementation docs |
| `05_domain_model.md` | Logical entities and relationships | `02`, `04` | `06`, `10`, `26`, `55` | API, DB, engines, UI |
| `06_json_artifacts_spec.md` | Machine-readable rules and catalogs | `02`, `04`, `05` | `07`, `08`, `09`, `17`, `26`, `33` | Engines and validation |
| `55_database_schema_migrations_and_data_integrity_spec.md` | DB schema, migrations, integrity | `04`, `05`, `27` | `29`, `31`, `34`, `38` | Persistence layer |

Conflict risks:

- `10_api_contract.md` must not introduce fields absent from `05_domain_model.md`.
- `06_json_artifacts_spec.md` must not contain detailed engine formulas that belong in `08`.
- `55_database_schema_migrations_and_data_integrity_spec.md` must implement the domain model, not redefine it.

---

## 7. Core Engine Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `07_execution_engine_spec.md` | Generate stages and operations | `02`, `05`, `06` | `08`, `17`, `18`, `26` | Materials, sequencing, API |
| `08_material_consumption_engine_spec.md` | Material quantities, formulas, packages | `02`, `05`, `06`, `07` | `09`, `12`, `26`, `29` | Cost, procurement, reports |
| `09_cost_and_procurement_spec.md` | Cost and procurement summaries | `05`, `08` | `40`, `43`, `49` | UI, reports, suppliers |
| `17_construction_technology_and_sequencing_spec.md` | Dependencies, parallel rules, wait times, quality gates | `07`, `15`, `26` | `18`, `20`, `21`, `22`, `23` | Allowed/blocked states |
| `19_recommendation_and_constraint_engine_spec.md` | Recommendations, warnings, compatibility constraints | `05`, `15`, `16`, `18`, `20`, `22`, `23` | `11`, `26`, `52` | UI warnings and blocks |
| `26_validation_and_error_handling_spec.md` | Validation, errors, warnings, no silent fallback | `02`, `05`, `06`, `10` | `12`, `17`, `19`, `27` | API, UI, tests |
| `29_calculation_versioning_and_traceability_spec.md` | Versioned calculation trace | `06`, `08`, `09` | `33`, `38`, `44` | Audit, recalculation, support |
| `38_change_impact_and_recalculation_spec.md` | Impact analysis after changes | `05`, `07`, `08`, `09`, `17`, `29` | `39`, `57` | Recalculation UI/workflow |

Conflict risks:

- `09` must not recalculate material quantities independently of `08`.
- `17` must not generate operations; operation generation belongs to `07`.
- `26` must not redefine formulas; it validates inputs, outputs and error behavior.
- `19` must not override deterministic blocking rules from `17`.

---

## 8. Interface and Experience Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `10_api_contract.md` | Internal platform API | `05`, `06`, `07`, `08`, `09`, `26` | `11`, `30`, `31`, `53` | Frontend, mobile, integrations |
| `11_ui_ux_spec.md` | Guided workflow and UX states | `03`, `10`, `19`, `26`, `39` | `51`, `52`, `56`, `59` | Frontend |
| `39_project_room_status_lifecycle_spec.md` | Project/room statuses | `03`, `07`, `17`, `26`, `38` | `11`, `46`, `47`, `57` | UI progress, approvals |
| `40_reports_exports_and_printable_outputs_spec.md` | Reports, exports, printable output | `08`, `09`, `10`, `29` | `46`, `49`, `53`, `60` | PDF/XLSX/export |
| `51_multi_client_mobile_and_role_based_access_spec.md` | Web/mobile/portal role-based interfaces | `10`, `11`, `30`, `31` | `46`, `47`, `52`, `56` | Mobile/portals |
| `52_design_system_and_visual_language_spec.md` | Visual language and UI components | `03`, `11`, `39`, `51` | `59` | Design system |
| `56_notifications_communications_and_activity_feed_spec.md` | Notifications, communication, activity feed | `30`, `39`, `46`, `47`, `57` | `31`, `35`, `51` | Notifications service |
| `59_user_onboarding_help_center_and_training_spec.md` | Onboarding, help center, training | `01`, `03`, `11`, `52` | `46`, `47`, `44` | Training/help UX |

Conflict risks:

- `11` must not define API responses; API belongs to `10`.
- `52` must not define workflows; workflow belongs to `11`.
- `51` must not redefine permissions; permissions belong to `30`.
- `40` must not redefine calculations; it only presents/exports results.

---

## 9. Domain Expansion Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `14_tooling_equipment_and_robotics_spec.md` | Tools, equipment, robotics, economics | `05`, `07`, `09` | `17`, `49` | Tool/equipment checklist |
| `15_engineering_layer_spec.md` | Engineering systems and points | `04`, `05`, `06` | `17`, `20`, `22`, `23`, `26` | Engineering operations |
| `16_openings_doors_windows_spec.md` | Openings, doors, windows, economics | `05`, `06`, `08`, `09` | `23`, `25`, `36` | Geometry deductions |
| `18_fixtures_furniture_and_equipment_spec.md` | Fixtures, furniture, appliances | `05`, `15`, `17` | `20`, `22`, `23`, `49` | Engineering dependencies |
| `20_hvac_ventilation_and_air_quality_spec.md` | HVAC, ventilation, air quality | `15`, `17`, `19` | `21`, `22`, `23` | HVAC logic |
| `21_acoustic_thermal_and_building_physics_spec.md` | Insulation, acoustics, vapor barriers | `05`, `08`, `17`, `19` | `20`, `22`, `24` | Material/constraint rules |
| `22_heating_systems_spec.md` | Heating systems and equipment | `15`, `17`, `19` | `20`, `21`, `23` | Heating sublayer |
| `23_smart_home_and_automation_spec.md` | Smart home, protocols, devices, scenarios | `15`, `19`, `30`, `31` | `20`, `22`, `51`, `53` | Automation layer |
| `24_auxiliary_spaces_balconies_loggias_storage_spec.md` | Balconies, loggias, storage spaces | `05`, `16`, `19`, `21` | `36`, `49` | Auxiliary workflows |
| `25_accessories_hardware_and_finishing_components_spec.md` | Accessories, hardware, finishing components | `05`, `09`, `16` | `23`, `49` | Procurement/catalog expansion |

Conflict risks:

- These documents must not move future features into MVP unless `02_mvp_scope.md` changes.
- Engineering-related documents must remain consistent with `15_engineering_layer_spec.md`.
- Cost and procurement references must follow `09_cost_and_procurement_spec.md`.

---

## 10. QA, Development, Release and Maintenance Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `12_testing_and_release_spec.md` | Testing and release criteria | `02`, `05`, `06`, `08`, `10`, `26` | `27`, `34`, `35`, `48` | QA |
| `27_development_methodology_and_coding_standards.md` | Programming approach and coding standards | `04`, `05`, `06`, `10`, `12`, `26` | `55` | Implementation discipline |
| `34_deployment_environments_and_operations_spec.md` | Environments, deployment, rollback | `27`, `31`, `55` | `35`, `44`, `48` | DevOps |
| `35_observability_logging_and_diagnostics_spec.md` | Logs, traces, diagnostics, monitoring | `26`, `29`, `31`, `34` | `44`, `48`, `56` | Support/debug tools |
| `44_maintenance_updates_and_support_spec.md` | Updates, maintenance, support workflows | `12`, `29`, `33`, `34`, `35` | `48`, `59` | Post-release support |
| `48_bugfix_improvement_and_regression_policy.md` | Bugfix, improvements, regression policy | `12`, `26`, `27`, `35`, `44` | `45` | Patch/hotfix workflows |

Conflict risks:

- `48` must not duplicate full support workflows from `44`.
- `35` must not redefine error codes; error behavior belongs to `26`.
- `34` must not redefine architecture; architecture belongs to `04`.

---

## 11. Production, Security, Data and Governance Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `30_users_roles_permissions_and_access_control_spec.md` | Users, roles, permissions, RBAC | `04`, `10`, `11` | `31`, `46`, `47`, `51`, `54` | Auth/API/UI roles |
| `31_information_security_privacy_backup_and_cyber_protection_spec.md` | Security, privacy, backup, cyber protection | `30`, `32`, `34`, `35` | `53`, `56` | Security implementation |
| `32_files_media_and_project_evidence_spec.md` | Files, photos, media, evidence | `05`, `31` | `46`, `47`, `56` | Storage/evidence workflows |
| `33_catalog_and_rules_governance_spec.md` | Rule/catalog update process | `06`, `08`, `09`, `29` | `43`, `49` | Catalog governance |
| `36_regulatory_safety_and_liability_boundaries_spec.md` | Safety, regulatory, liability boundaries | `15`, `16`, `20`, `22`, `23`, `24` | `41`, `46`, `47` | Warnings/approvals |
| `37_units_currency_localization_and_market_adaptation_spec.md` | Units, currency, localization | `08`, `09`, `43` | `49`, `54` | Multi-market readiness |
| `41_ai_usage_boundaries_and_human_approval_spec.md` | AI usage boundaries and human approval | `13`, `26`, `27`, `36` | `50` | AI workflows |
| `42_performance_limits_and_scalability_spec.md` | Performance limits and scalability | `04`, `10`, `27`, `55` | `34`, `35` | Scaling plan |
| `43_pricing_suppliers_and_market_data_spec.md` | Pricing and market data rules | `09`, `33`, `37`, `49` | `54` | Supplier pricing logic |

Conflict risks:

- `31` must enforce roles from `30`, not redefine them.
- `33` must not redefine formulas; it governs how rules are updated.
- `36` must not act as legal advice; it defines system warnings and boundaries.
- `41` must not allow AI to override deterministic engines.

---

## 12. Business, Commercial and Ecosystem Pack

| Document | Primary Responsibility | Upstream | Directly Related | Downstream |
|---|---|---|---|---|
| `46_customer_workflow_and_client_management_spec.md` | Customer workflow and approvals | `03`, `09`, `39`, `40` | `57`, `60`, `56` | Client portal |
| `47_contractor_workflow_and_subcontractor_management_spec.md` | Contractor workflow and work assignment | `07`, `17`, `39` | `56`, `57`, `60` | Contractor portal |
| `49_suppliers_procurement_and_rental_ecosystem_spec.md` | Suppliers, procurement, rental ecosystem | `09`, `14`, `33`, `43` | `53`, `54` | Supplier/procurement modules |
| `53_external_integrations_and_api_interoperability_spec.md` | External integrations and interoperability | `10`, `30`, `31`, `40`, `49` | `54`, `60` | Integration layer |
| `54_commercial_models_partnerships_and_monetization_spec.md` | Commercial models and monetization | `30`, `49`, `51`, `53` | `44`, `46`, `47` | Billing/feature gating |
| `57_approvals_change_orders_and_decision_log_spec.md` | Approvals, change orders, decisions | `38`, `39`, `46`, `47` | `56`, `60` | Decision log |
| `58_product_analytics_kpi_and_usage_metrics_spec.md` | Product analytics and KPIs | `11`, `35`, `44`, `54` | `59` | Analytics |
| `60_legal_contracts_financial_documents_and_e_signatures_spec.md` | Legal, contracts, financial docs, e-signatures | `40`, `46`, `47`, `53`, `54`, `57` | `31`, `36` | Legal/financial workflows |

Conflict risks:

- `46` and `47` must not redefine roles; roles belong to `30`.
- `49` must not redefine quantities; it uses procurement outputs from `09`.
- `54` must not redefine permissions; it defines commercial access models enforced through `30`.
- `60` must not replace legal counsel; it defines platform workflow requirements.

---

## 13. AI Reading Packs

### Backend Core Pack

```text
02_mvp_scope.md
04_system_architecture.md
05_domain_model.md
06_json_artifacts_spec.md
26_validation_and_error_handling_spec.md
27_development_methodology_and_coding_standards.md
55_database_schema_migrations_and_data_integrity_spec.md
```

### Material Engine Pack

```text
02_mvp_scope.md
05_domain_model.md
06_json_artifacts_spec.md
07_execution_engine_spec.md
08_material_consumption_engine_spec.md
09_cost_and_procurement_spec.md
12_testing_and_release_spec.md
26_validation_and_error_handling_spec.md
29_calculation_versioning_and_traceability_spec.md
```

### Execution and Sequencing Pack

```text
05_domain_model.md
06_json_artifacts_spec.md
07_execution_engine_spec.md
17_construction_technology_and_sequencing_spec.md
26_validation_and_error_handling_spec.md
12_testing_and_release_spec.md
```

### API Pack

```text
05_domain_model.md
06_json_artifacts_spec.md
07_execution_engine_spec.md
08_material_consumption_engine_spec.md
09_cost_and_procurement_spec.md
10_api_contract.md
26_validation_and_error_handling_spec.md
30_users_roles_permissions_and_access_control_spec.md
```

### UI / UX Pack

```text
03_user_flow_and_modules.md
10_api_contract.md
11_ui_ux_spec.md
19_recommendation_and_constraint_engine_spec.md
26_validation_and_error_handling_spec.md
39_project_room_status_lifecycle_spec.md
51_multi_client_mobile_and_role_based_access_spec.md
52_design_system_and_visual_language_spec.md
```

### Security Pack

```text
30_users_roles_permissions_and_access_control_spec.md
31_information_security_privacy_backup_and_cyber_protection_spec.md
32_files_media_and_project_evidence_spec.md
34_deployment_environments_and_operations_spec.md
35_observability_logging_and_diagnostics_spec.md
53_external_integrations_and_api_interoperability_spec.md
```

### Supplier / Procurement Pack

```text
09_cost_and_procurement_spec.md
14_tooling_equipment_and_robotics_spec.md
33_catalog_and_rules_governance_spec.md
40_reports_exports_and_printable_outputs_spec.md
43_pricing_suppliers_and_market_data_spec.md
49_suppliers_procurement_and_rental_ecosystem_spec.md
53_external_integrations_and_api_interoperability_spec.md
```

### Mobile and Role-Based Access Pack

```text
10_api_contract.md
11_ui_ux_spec.md
30_users_roles_permissions_and_access_control_spec.md
31_information_security_privacy_backup_and_cyber_protection_spec.md
39_project_room_status_lifecycle_spec.md
46_customer_workflow_and_client_management_spec.md
47_contractor_workflow_and_subcontractor_management_spec.md
51_multi_client_mobile_and_role_based_access_spec.md
52_design_system_and_visual_language_spec.md
```

### Production Readiness Pack

```text
12_testing_and_release_spec.md
29_calculation_versioning_and_traceability_spec.md
31_information_security_privacy_backup_and_cyber_protection_spec.md
34_deployment_environments_and_operations_spec.md
35_observability_logging_and_diagnostics_spec.md
42_performance_limits_and_scalability_spec.md
44_maintenance_updates_and_support_spec.md
48_bugfix_improvement_and_regression_policy.md
```

---

## 14. Documents That Should Be Updated Together

| If this changes | Also review/update |
|---|---|
| `02_mvp_scope.md` | `00`, `03`, `04`, `12`, `28`, Registry |
| `05_domain_model.md` | `06`, `10`, `26`, `55`, Registry |
| `06_json_artifacts_spec.md` | `07`, `08`, `12`, `26`, `33`, Registry |
| `07_execution_engine_spec.md` | `08`, `17`, `26`, `10`, `12` |
| `08_material_consumption_engine_spec.md` | `09`, `12`, `26`, `29`, `40` |
| `09_cost_and_procurement_spec.md` | `40`, `43`, `49`, `54` |
| `10_api_contract.md` | `11`, `30`, `31`, `51`, `53` |
| `11_ui_ux_spec.md` | `39`, `51`, `52`, `56`, `59` |
| `17_construction_technology_and_sequencing_spec.md` | `07`, `26`, `39`, `47`, `57` |
| `26_validation_and_error_handling_spec.md` | `10`, `11`, `12`, `17`, `19`, `27` |
| `30_users_roles_permissions_and_access_control_spec.md` | `31`, `46`, `47`, `51`, `54` |
| `31_information_security_privacy_backup_and_cyber_protection_spec.md` | `30`, `32`, `34`, `35`, `53` |
| `33_catalog_and_rules_governance_spec.md` | `06`, `08`, `29`, `43`, `49` |
| `38_change_impact_and_recalculation_spec.md` | `29`, `39`, `57` |
| `49_suppliers_procurement_and_rental_ecosystem_spec.md` | `09`, `14`, `43`, `53`, `54` |
| `51_multi_client_mobile_and_role_based_access_spec.md` | `10`, `11`, `30`, `31`, `52` |
| `53_external_integrations_and_api_interoperability_spec.md` | `10`, `30`, `31`, `40`, `49`, `60` |
| `54_commercial_models_partnerships_and_monetization_spec.md` | `30`, `44`, `49`, `51`, `53` |

---

## 15. Dependency Audit Checklist

A document cannot be approved or frozen until these are answered:

```text
1. Does this document have a clear source-of-truth responsibility?
2. Does it duplicate another document?
3. Are upstream dependencies listed?
4. Are downstream dependencies listed?
5. Are directly related documents listed?
6. Are likely conflict risks listed?
7. Are documents that must be updated together identified?
8. Is the document placed at the correct hierarchy level?
9. Is the implementation block clearly defined?
10. Can a developer or AI coding agent identify the required reading pack for this module?
```

---

## 16. Current Status

```text
Status: DRAFT
Purpose: Initial dependency map for Phase 1 documentation architecture.
Next Action: Cross-check this file against documentation_registry_v0.1.yaml.
Freeze Condition: All documents 00–60 are represented in registry and dependency map.
```
