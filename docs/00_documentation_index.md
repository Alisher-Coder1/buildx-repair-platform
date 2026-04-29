# 00 Documentation Index

## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_00 |
| File Name | 00_documentation_index.md |
| Version | v0.1 |
| Status | DRAFT |
| Owner | Documentation Architect |
| Hierarchy Level | Level 0 — Documentation Control |
| Implementation Block | Documentation Navigation / Source Map |
| Source of Truth Responsibility | Documentation structure, reading order, document map |
| Directly Related Documents | 13_document_acceptance_and_governance.md, 45_documentation_writing_methodology_and_style_guide.md, documentation_registry_v0.1.yaml, docs/audit/documentation_audit_question_matrix_v0.1.md, docs/audit/documentation_dependency_map_v0.1.md |
| Upstream Dependencies | None |
| Downstream Dependencies | All documentation files |
| Duplication Check | Must not duplicate full content of individual documents |
| Conflict Check | Must align with documentation_registry_v0.1.yaml |
| Requires Expert Review | No |

## Purpose

This document is the human-readable map of the Buildx Repair Platform documentation system.

It explains:

- which documents exist;
- how documents are grouped;
- which documents are critical;
- which order to read them in;
- how humans and AI coding agents should navigate the documentation.

## Current Documentation Count

Current planned numbered documents:

```text
00–60 = 61 numbered documents
```

Additional documentation control files:

```text
docs/documentation_registry_v0.1.yaml
docs/audit/documentation_audit_question_matrix_v0.1.md
docs/audit/documentation_dependency_map_v0.1.md
```

## Core Principle

The documentation package must be treated as a structured knowledge system, not as a random folder of Markdown files.

## Reading Order — Phase 1

1. `README.md`
2. `docs/00_documentation_index.md`
3. `docs/documentation_registry_v0.1.yaml`
4. `docs/templates/document_template.md`
5. `docs/45_documentation_writing_methodology_and_style_guide.md`
6. `docs/13_document_acceptance_and_governance.md`
7. `docs/audit/documentation_audit_question_matrix_v0.1.md`
8. `docs/audit/documentation_dependency_map_v0.1.md`

## Documentation Layers

### Level 0 — Documentation Control

- `00_documentation_index.md`
- `13_document_acceptance_and_governance.md`
- `45_documentation_writing_methodology_and_style_guide.md`
- `documentation_registry_v0.1.yaml`
- `documentation_audit_question_matrix_v0.1.md`
- `documentation_dependency_map_v0.1.md`
- `50_knowledge_base_and_documentation_rag_spec.md`

### Level 1 — Product Layer

- `01_product_brief.md`
- `02_mvp_scope.md`
- `03_user_flow_and_modules.md`
- `28_roadmap_to_mvp_and_production.md`

### Level 2 — System Layer

- `04_system_architecture.md`
- `05_domain_model.md`
- `06_json_artifacts_spec.md`
- `55_database_schema_migrations_and_data_integrity_spec.md`

### Level 3 — Core Engines

- `07_execution_engine_spec.md`
- `08_material_consumption_engine_spec.md`
- `09_cost_and_procurement_spec.md`
- `17_construction_technology_and_sequencing_spec.md`
- `19_recommendation_and_constraint_engine_spec.md`
- `26_validation_and_error_handling_spec.md`

### Level 4 — Interfaces

- `10_api_contract.md`
- `11_ui_ux_spec.md`
- `40_reports_exports_and_printable_outputs_spec.md`
- `51_multi_client_mobile_and_role_based_access_spec.md`
- `52_design_system_and_visual_language_spec.md`
- `53_external_integrations_and_api_interoperability_spec.md`

### Level 5 — QA / Development / Release

- `12_testing_and_release_spec.md`
- `27_development_methodology_and_coding_standards.md`
- `34_deployment_environments_and_operations_spec.md`
- `35_observability_logging_and_diagnostics_spec.md`
- `48_bugfix_improvement_and_regression_policy.md`

### Level 6 — Domain Expansion Layers

- `14_tooling_equipment_and_robotics_spec.md`
- `15_engineering_layer_spec.md`
- `16_openings_doors_windows_spec.md`
- `18_fixtures_furniture_and_equipment_spec.md`
- `20_hvac_ventilation_and_air_quality_spec.md`
- `21_acoustic_thermal_and_building_physics_spec.md`
- `22_heating_systems_spec.md`
- `23_smart_home_and_automation_spec.md`
- `24_auxiliary_spaces_balconies_loggias_storage_spec.md`
- `25_accessories_hardware_and_finishing_components_spec.md`

### Level 7 — Production / Business / Operations

- `29_calculation_versioning_and_traceability_spec.md`
- `30_users_roles_permissions_and_access_control_spec.md`
- `31_information_security_privacy_backup_and_cyber_protection_spec.md`
- `32_files_media_and_project_evidence_spec.md`
- `33_catalog_and_rules_governance_spec.md`
- `36_regulatory_safety_and_liability_boundaries_spec.md`
- `37_units_currency_localization_and_market_adaptation_spec.md`
- `38_change_impact_and_recalculation_spec.md`
- `39_project_room_status_lifecycle_spec.md`
- `41_ai_usage_boundaries_and_human_approval_spec.md`
- `42_performance_limits_and_scalability_spec.md`
- `43_pricing_suppliers_and_market_data_spec.md`
- `44_maintenance_updates_and_support_spec.md`
- `46_customer_workflow_and_client_management_spec.md`
- `47_contractor_workflow_and_subcontractor_management_spec.md`
- `49_suppliers_procurement_and_rental_ecosystem_spec.md`
- `54_commercial_models_partnerships_and_monetization_spec.md`
- `56_notifications_communications_and_activity_feed_spec.md`
- `57_approvals_change_orders_and_decision_log_spec.md`
- `58_product_analytics_kpi_and_usage_metrics_spec.md`
- `59_user_onboarding_help_center_and_training_spec.md`
- `60_legal_contracts_financial_documents_and_e_signatures_spec.md`

## Critical MVP Documentation Pack

Before MVP implementation starts, the following documents must be approved or frozen:

- `02_mvp_scope.md`
- `04_system_architecture.md`
- `05_domain_model.md`
- `06_json_artifacts_spec.md`
- `07_execution_engine_spec.md`
- `08_material_consumption_engine_spec.md`
- `09_cost_and_procurement_spec.md`
- `10_api_contract.md`
- `12_testing_and_release_spec.md`
- `13_document_acceptance_and_governance.md`
- `26_validation_and_error_handling_spec.md`
- `27_development_methodology_and_coding_standards.md`

## AI Reading Packs

### Backend Core Pack

- `02_mvp_scope.md`
- `04_system_architecture.md`
- `05_domain_model.md`
- `06_json_artifacts_spec.md`
- `26_validation_and_error_handling_spec.md`
- `27_development_methodology_and_coding_standards.md`

### Material Engine Pack

- `05_domain_model.md`
- `06_json_artifacts_spec.md`
- `07_execution_engine_spec.md`
- `08_material_consumption_engine_spec.md`
- `12_testing_and_release_spec.md`
- `26_validation_and_error_handling_spec.md`
- `29_calculation_versioning_and_traceability_spec.md`

### UI Pack

- `03_user_flow_and_modules.md`
- `10_api_contract.md`
- `11_ui_ux_spec.md`
- `19_recommendation_and_constraint_engine_spec.md`
- `39_project_room_status_lifecycle_spec.md`
- `51_multi_client_mobile_and_role_based_access_spec.md`
- `52_design_system_and_visual_language_spec.md`

### Production Readiness Pack

- `29_calculation_versioning_and_traceability_spec.md`
- `30_users_roles_permissions_and_access_control_spec.md`
- `31_information_security_privacy_backup_and_cyber_protection_spec.md`
- `34_deployment_environments_and_operations_spec.md`
- `35_observability_logging_and_diagnostics_spec.md`
- `44_maintenance_updates_and_support_spec.md`
- `48_bugfix_improvement_and_regression_policy.md`

## Dependency Navigation

Cross-document relationships are controlled by two files:

```text
docs/documentation_registry_v0.1.yaml
docs/audit/documentation_dependency_map_v0.1.md
```

Use `documentation_registry_v0.1.yaml` as the machine-readable registry.

Use `documentation_dependency_map_v0.1.md` as the human-readable dependency map for:

- upstream dependencies;
- directly related documents;
- downstream dependencies;
- likely conflicts;
- documents that must be updated together;
- AI reading packs.

Before approving or freezing any document, the dependency map must be checked together with the audit question matrix.

## Acceptance Criteria

This document is accepted if:

- [ ] It lists the documentation system structure.
- [ ] It explains hierarchy levels.
- [ ] It defines reading order.
- [ ] It references the registry.
- [ ] It references the dependency map.
- [ ] It separates critical MVP documents from future/production documents.
- [ ] It helps humans and AI agents navigate the documentation without confusion.
