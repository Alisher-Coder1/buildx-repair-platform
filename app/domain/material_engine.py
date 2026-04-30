import math
from datetime import datetime, timezone
from typing import Any

from app.artifacts.exceptions import ArtifactValidationError
from app.domain.execution_engine import generate_execution_operations


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def calculate_package_count(material_quantity: float, package_size: float) -> int:
    if material_quantity <= 0:
        raise ArtifactValidationError(
            error_code="ERR_INVALID_QUANTITY",
            message="Material quantity must be greater than zero.",
            field="material_quantity",
            details={"material_quantity": material_quantity},
        )

    if package_size <= 0:
        raise ArtifactValidationError(
            error_code="ERR_PACKAGE_SIZE_MISSING",
            message="Package size must be greater than zero.",
            field="package_size",
            details={"package_size": package_size},
        )

    return max(1, math.ceil(material_quantity / package_size))


def raise_required(field: str, rule: dict[str, Any], norm: dict[str, Any]) -> None:
    raise ArtifactValidationError(
        error_code="ERR_REQUIRED_FIELD_MISSING",
        message="Required calculation field is missing.",
        field=field,
        details={"rule_id": rule.get("rule_id"), "norm_id": norm.get("norm_id")},
    )


def calculate_material_quantity(
    *,
    formula_type: str,
    base_quantity: float,
    norm: dict[str, Any],
    rule: dict[str, Any],
) -> float:
    if base_quantity <= 0:
        raise ArtifactValidationError(
            error_code="ERR_INVALID_QUANTITY",
            message="Base quantity must be greater than zero.",
            field="base_quantity",
            details={"base_quantity": base_quantity},
        )

    loss_factor = rule.get("loss_factor") or norm.get("default_loss_factor")
    if not loss_factor or loss_factor <= 0:
        raise_required("loss_factor", rule, norm)

    if formula_type == "AREA_BASED":
        consumption_norm = norm.get("consumption_norm")
        if not consumption_norm or consumption_norm <= 0:
            raise_required("consumption_norm", rule, norm)
        layer_count = rule.get("layer_count")
        if layer_count:
            return base_quantity * consumption_norm * layer_count * loss_factor
        return base_quantity * consumption_norm * loss_factor

    if formula_type == "LAYER_BASED":
        consumption_norm = norm.get("consumption_norm")
        layer_count = rule.get("layer_count") or norm.get("default_layer_count")
        if not consumption_norm or consumption_norm <= 0:
            raise_required("consumption_norm", rule, norm)
        if not layer_count or layer_count <= 0:
            raise_required("layer_count", rule, norm)
        return base_quantity * consumption_norm * layer_count * loss_factor

    if formula_type == "THICKNESS_BASED":
        q_per_mm = norm.get("q_per_mm")
        thickness_mm = rule.get("thickness_mm")
        if not q_per_mm or q_per_mm <= 0:
            raise_required("q_per_mm", rule, norm)
        if not thickness_mm or thickness_mm <= 0:
            raise_required("thickness_mm", rule, norm)
        return base_quantity * q_per_mm * thickness_mm * loss_factor

    if formula_type == "LINEAR_BASED":
        consumption_norm = norm.get("consumption_norm")
        if not consumption_norm or consumption_norm <= 0:
            raise_required("consumption_norm", rule, norm)
        return base_quantity * consumption_norm * loss_factor

    raise ArtifactValidationError(
        error_code="ERR_REQUIRED_FIELD_MISSING",
        message="Unsupported formula type for Prototype v0.1.",
        field="formula_type",
        details={"formula_type": formula_type, "rule_id": rule.get("rule_id")},
    )


def _index_by(items: list[dict[str, Any]], id_field: str) -> dict[str, dict[str, Any]]:
    return {item[id_field]: item for item in items}


def _selected_coating_for_surface(room, surface_type: str) -> str:
    if surface_type == "FLOOR":
        return room.floor_covering
    if surface_type == "WALLS":
        return room.wall_covering
    if surface_type == "CEILING":
        return room.ceiling_covering
    raise ArtifactValidationError(
        error_code="ERR_INVALID_ENUM_VALUE",
        message="Unsupported surface type.",
        field="surface_type",
        details={"surface_type": surface_type},
    )


def _rule_priority(rule: dict[str, Any], coating_id: str, zone: str) -> int | None:
    rule_coating = rule["coating_id"]
    rule_zone = rule["zone"]

    if rule_coating == coating_id and rule_zone == zone:
        return 0
    if rule_coating == coating_id and rule_zone == "ANY":
        return 1
    if rule_coating == "ANY" and rule_zone == zone:
        return 2
    if rule_coating == "ANY" and rule_zone == "ANY":
        return 3
    return None


def match_material_rules(
    *,
    operation: dict[str, Any],
    room,
    rules: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    coating_id = _selected_coating_for_surface(room, operation["surface_type"])
    zone = room.zone

    candidates: list[tuple[int, dict[str, Any]]] = []
    for rule in rules:
        if not rule.get("is_active", True):
            continue
        if rule["operation_id"] != operation["operation_id"]:
            continue
        if rule["surface_type"] != operation["surface_type"]:
            continue

        priority = _rule_priority(rule, coating_id, zone)
        if priority is not None:
            candidates.append((priority, rule))

    if not candidates:
        raise ArtifactValidationError(
            error_code="ERR_MATERIAL_RULE_MISSING",
            message="Material rule is missing for operation and selected context.",
            field="operation_material_rules",
            details={
                "operation_id": operation["operation_id"],
                "surface_type": operation["surface_type"],
                "coating_id": coating_id,
                "zone": zone,
            },
        )

    best_priority = min(priority for priority, _ in candidates)
    return [rule for priority, rule in candidates if priority == best_priority]


def _material_formula_description(formula_type: str) -> str:
    if formula_type == "AREA_BASED":
        return "base_quantity * consumption_norm * loss_factor"
    if formula_type == "LAYER_BASED":
        return "base_quantity * consumption_norm * layer_count * loss_factor"
    if formula_type == "THICKNESS_BASED":
        return "base_quantity * q_per_mm * thickness_mm * loss_factor"
    if formula_type == "LINEAR_BASED":
        return "base_quantity * consumption_norm * loss_factor"
    return "unsupported_formula_type"


def build_material_item(
    *,
    room_id: str,
    operation: dict[str, Any],
    rule: dict[str, Any],
    materials_by_id: dict[str, dict[str, Any]],
    norms_by_id: dict[str, dict[str, Any]],
    packages_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    material = materials_by_id.get(rule["material_id"])
    if material is None:
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_REFERENCE_INVALID",
            message="Rule material reference is invalid.",
            field="material_id",
            details={"rule_id": rule["rule_id"], "material_id": rule["material_id"]},
        )

    norm = norms_by_id.get(rule["norm_id"])
    if norm is None:
        raise ArtifactValidationError(
            error_code="ERR_MATERIAL_NORM_MISSING",
            message="Material norm is missing.",
            field="norm_id",
            details={"rule_id": rule["rule_id"], "norm_id": rule["norm_id"]},
        )

    package = packages_by_id.get(rule["package_id"])
    if package is None:
        raise ArtifactValidationError(
            error_code="ERR_PACKAGE_SIZE_MISSING",
            message="Package size is missing.",
            field="package_id",
            details={"rule_id": rule["rule_id"], "package_id": rule["package_id"]},
        )

    formula_type = rule["formula_type"]
    base_quantity = operation["quantity"]
    raw_quantity = calculate_material_quantity(
        formula_type=formula_type,
        base_quantity=base_quantity,
        norm=norm,
        rule=rule,
    )
    package_count = calculate_package_count(raw_quantity, package["package_size"])

    loss_factor = rule.get("loss_factor") or norm.get("default_loss_factor")
    layer_count = rule.get("layer_count") or norm.get("default_layer_count")
    thickness_mm = rule.get("thickness_mm")
    consumption_norm = norm.get("consumption_norm")
    q_per_mm = norm.get("q_per_mm")

    explanation = {
        "formula_type": formula_type,
        "formula": _material_formula_description(formula_type),
        "base_quantity": round(base_quantity, 2),
        "base_unit": operation.get("unit"),
        "norm_id": norm["norm_id"],
        "consumption_norm": consumption_norm,
        "q_per_mm": q_per_mm,
        "loss_factor": loss_factor,
        "layer_count": layer_count,
        "thickness_mm": thickness_mm,
        "calculated_quantity": round(raw_quantity, 2),
        "calculated_unit": norm["unit"],
        "package_size": package["package_size"],
        "package_unit": norm["unit"],
        "package_count": package_count,
        "rounding_rule": "ceil(calculated_quantity / package_size)",
    }

    return {
        "item_id": f"{operation['operation_id']}:{rule['rule_id']}:{material['material_id']}",
        "room_id": room_id,
        "source_operation_id": operation["operation_id"],
        "rule_id": rule["rule_id"],
        "material_id": material["material_id"],
        "material_name": material["material_name"],
        "formula_type": formula_type,
        "base_quantity": round(base_quantity, 2),
        "calculated_quantity": round(raw_quantity, 2),
        "unit": norm["unit"],
        "loss_factor": loss_factor,
        "layer_count": layer_count,
        "thickness_mm": thickness_mm,
        "package_id": package["package_id"],
        "package_size": package["package_size"],
        "package_count": package_count,
        "explanation": explanation,
        "warnings": [],
    }


def build_material_consumption_summary(
    room, artifact_set: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    materials_by_id = _index_by(
        artifact_set["materials_v1.json"]["items"], "material_id"
    )
    norms_by_id = _index_by(artifact_set["material_norms_v1.json"]["items"], "norm_id")
    packages_by_id = _index_by(artifact_set["packages_v1.json"]["items"], "package_id")
    rules = artifact_set["operation_material_rules_v1.json"]["items"]
    operations = generate_execution_operations(room, artifact_set)

    items: list[dict[str, Any]] = []
    for operation in operations:
        matched_rules = match_material_rules(
            operation=operation, room=room, rules=rules
        )
        for rule in matched_rules:
            items.append(
                build_material_item(
                    room_id=room.room_id,
                    operation=operation,
                    rule=rule,
                    materials_by_id=materials_by_id,
                    norms_by_id=norms_by_id,
                    packages_by_id=packages_by_id,
                )
            )

    manifest = artifact_set.get("artifact_manifest_v1.json", {})
    return {
        "room_id": room.room_id,
        "items": items,
        "calculated_at": utc_now_iso(),
        "artifact_version": manifest.get("artifact_set_version", "v1"),
    }
