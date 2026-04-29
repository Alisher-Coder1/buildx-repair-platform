from typing import Any

from app.artifacts.exceptions import ArtifactValidationError


ARTIFACT_ITEM_ID_FIELDS = {
    "coatings_v1.json": "coating_id",
    "materials_v1.json": "material_id",
    "packages_v1.json": "package_id",
    "operations_v1.json": "operation_id",
    "material_norms_v1.json": "norm_id",
    "operation_material_rules_v1.json": "rule_id",
}

REQUIRED_ITEM_FIELDS = {
    "coatings_v1.json": ["coating_id", "surface_type", "display_name", "prototype_enabled", "is_active"],
    "materials_v1.json": ["material_id", "material_name", "default_unit", "prototype_enabled", "is_active"],
    "packages_v1.json": ["package_id", "material_id", "package_size", "package_unit", "display_name", "is_default", "is_active"],
    "operations_v1.json": ["operation_id", "operation_name", "stage", "surface_type", "quantity_source", "default_unit", "sort_order", "is_active"],
    "material_norms_v1.json": ["norm_id", "material_id", "formula_type", "default_loss_factor", "unit", "is_active"],
    "operation_material_rules_v1.json": ["rule_id", "operation_id", "surface_type", "coating_id", "zone", "material_id", "norm_id", "formula_type", "loss_factor", "package_id", "is_required", "is_active"],
}

ALLOWED_SURFACE_TYPES = {"FLOOR", "WALLS", "CEILING"}
ALLOWED_ZONES = {"DRY", "WET", "KITCHEN", "ANY"}
ALLOWED_STAGES = {"STG_PREP", "STG_WATERPROOF", "STG_ROUGH", "STG_FINISH"}
ALLOWED_UNITS = {"KG", "LITER", "M2", "M_LINEAR", "PCS", "ROLL", "PACKAGE"}
ALLOWED_FORMULA_TYPES = {"AREA_BASED", "LAYER_BASED", "THICKNESS_BASED", "LINEAR_BASED", "PACKAGE_COUNT", "RECIPE_BASED"}


def _items(artifacts: dict[str, dict[str, Any]], filename: str) -> list[dict[str, Any]]:
    artifact = artifacts.get(filename)
    if artifact is None:
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_FILE_MISSING",
            message="Artifact is missing from loaded artifact set.",
            artifact_file=filename,
        )

    if filename == "artifact_manifest_v1.json":
        return []

    items = artifact.get("items")
    if not isinstance(items, list):
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_REQUIRED_FIELD_MISSING",
            message="Artifact must contain items array.",
            artifact_file=filename,
            field="items",
        )

    return items


def _validate_required_fields(filename: str, item: dict[str, Any]) -> None:
    for field in REQUIRED_ITEM_FIELDS.get(filename, []):
        if field not in item:
            raise ArtifactValidationError(
                error_code="ERR_ARTIFACT_REQUIRED_FIELD_MISSING",
                message="Required artifact field is missing.",
                artifact_file=filename,
                field=field,
                details={"item": item},
            )


def _validate_unique_ids(filename: str, items: list[dict[str, Any]]) -> None:
    id_field = ARTIFACT_ITEM_ID_FIELDS[filename]
    seen: set[str] = set()

    for item in items:
        item_id = item.get(id_field)
        if not item_id:
            raise ArtifactValidationError(
                error_code="ERR_ARTIFACT_REQUIRED_FIELD_MISSING",
                message="Artifact ID field is missing.",
                artifact_file=filename,
                field=id_field,
                details={"item": item},
            )

        if item_id in seen:
            raise ArtifactValidationError(
                error_code="ERR_ARTIFACT_DUPLICATE_ID",
                message="Duplicate artifact ID found.",
                artifact_file=filename,
                field=id_field,
                details={"duplicate_id": item_id},
            )

        seen.add(item_id)


def _validate_invalid_enum(filename: str, field: str, item: dict[str, Any]) -> None:
    raise ArtifactValidationError(
        error_code="ERR_ARTIFACT_INVALID_ENUM_VALUE",
        message="Artifact enum value is invalid.",
        artifact_file=filename,
        field=field,
        details={"item": item},
    )


def _validate_enums(filename: str, item: dict[str, Any]) -> None:
    if "surface_type" in item and item["surface_type"] not in ALLOWED_SURFACE_TYPES:
        _validate_invalid_enum(filename, "surface_type", item)

    if "zone" in item and item["zone"] not in ALLOWED_ZONES:
        _validate_invalid_enum(filename, "zone", item)

    if "stage" in item and item["stage"] not in ALLOWED_STAGES:
        _validate_invalid_enum(filename, "stage", item)

    for unit_field in ("default_unit", "unit", "package_unit"):
        if unit_field in item and item[unit_field] not in ALLOWED_UNITS:
            _validate_invalid_enum(filename, unit_field, item)

    if "formula_type" in item and item["formula_type"] not in ALLOWED_FORMULA_TYPES:
        _validate_invalid_enum(filename, "formula_type", item)


def _validate_positive_number(filename: str, field: str, item: dict[str, Any]) -> None:
    value = item.get(field)
    if value is None or not isinstance(value, (int, float)) or value <= 0:
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_REQUIRED_FIELD_MISSING",
            message="Artifact numeric field must exist and be greater than zero.",
            artifact_file=filename,
            field=field,
            details={"item": item},
        )


def _validate_formula_specific_fields(filename: str, item: dict[str, Any]) -> None:
    formula_type = item.get("formula_type")

    if filename == "material_norms_v1.json":
        if formula_type in {"AREA_BASED", "LAYER_BASED", "LINEAR_BASED"}:
            _validate_positive_number(filename, "consumption_norm", item)

        if formula_type == "THICKNESS_BASED":
            _validate_positive_number(filename, "q_per_mm", item)

        _validate_positive_number(filename, "default_loss_factor", item)

    if filename == "operation_material_rules_v1.json":
        _validate_positive_number(filename, "loss_factor", item)

        if formula_type == "THICKNESS_BASED":
            _validate_positive_number(filename, "thickness_mm", item)

        if formula_type == "LAYER_BASED":
            _validate_positive_number(filename, "layer_count", item)


def _build_id_set(artifacts: dict[str, dict[str, Any]], filename: str, id_field: str) -> set[str]:
    return {item[id_field] for item in _items(artifacts, filename)}


def _validate_reference(value: str, allowed: set[str], filename: str, field: str, item: dict[str, Any]) -> None:
    if value == "ANY":
        return

    if value not in allowed:
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_REFERENCE_INVALID",
            message="Artifact reference is invalid.",
            artifact_file=filename,
            field=field,
            details={"value": value, "item": item},
        )


def _validate_references(artifacts: dict[str, dict[str, Any]]) -> None:
    material_ids = _build_id_set(artifacts, "materials_v1.json", "material_id")
    package_ids = _build_id_set(artifacts, "packages_v1.json", "package_id")
    operation_ids = _build_id_set(artifacts, "operations_v1.json", "operation_id")
    norm_ids = _build_id_set(artifacts, "material_norms_v1.json", "norm_id")
    coating_ids = _build_id_set(artifacts, "coatings_v1.json", "coating_id")

    for package in _items(artifacts, "packages_v1.json"):
        _validate_reference(package["material_id"], material_ids, "packages_v1.json", "material_id", package)
        _validate_positive_number("packages_v1.json", "package_size", package)

    for norm in _items(artifacts, "material_norms_v1.json"):
        _validate_reference(norm["material_id"], material_ids, "material_norms_v1.json", "material_id", norm)

    for rule in _items(artifacts, "operation_material_rules_v1.json"):
        _validate_reference(rule["operation_id"], operation_ids, "operation_material_rules_v1.json", "operation_id", rule)
        _validate_reference(rule["material_id"], material_ids, "operation_material_rules_v1.json", "material_id", rule)
        _validate_reference(rule["norm_id"], norm_ids, "operation_material_rules_v1.json", "norm_id", rule)
        _validate_reference(rule["package_id"], package_ids, "operation_material_rules_v1.json", "package_id", rule)
        _validate_reference(rule["coating_id"], coating_ids, "operation_material_rules_v1.json", "coating_id", rule)


def validate_artifact_set(artifacts: dict[str, dict[str, Any]]) -> None:
    for filename in ARTIFACT_ITEM_ID_FIELDS:
        items = _items(artifacts, filename)
        _validate_unique_ids(filename, items)

        for item in items:
            if not isinstance(item, dict):
                raise ArtifactValidationError(
                    error_code="ERR_ARTIFACT_JSON_INVALID",
                    message="Artifact item must be a JSON object.",
                    artifact_file=filename,
                )

            _validate_required_fields(filename, item)
            _validate_enums(filename, item)
            _validate_formula_specific_fields(filename, item)

    _validate_references(artifacts)
