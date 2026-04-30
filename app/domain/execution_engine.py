from datetime import datetime, timezone
from typing import Any

from app.artifacts.exceptions import ArtifactValidationError
from app.domain.geometry import calculate_room_geometry


FLOOR_INSTALL_OPERATION_BY_COVERING = {
    "COATING_FLOOR_LAMINATE": ["OPR_FLOOR_LAMINATE_INSTALL", "OPR_SKIRTING_INSTALL"],
    "COATING_FLOOR_LINOLEUM": ["OPR_FLOOR_LINOLEUM_INSTALL", "OPR_SKIRTING_INSTALL"],
    "COATING_FLOOR_PORCELAIN_TILE": ["OPR_FLOOR_TILE_INSTALL"],
    "COATING_FLOOR_SELF_LEVELING": ["OPR_FLOOR_SELF_LEVELING"],
}

WALL_OPERATIONS_BY_COVERING = {
    "COATING_WALL_WATER_BASED_PAINT": ["OPR_WALL_PLASTER", "OPR_WALL_PUTTY", "OPR_WALL_PAINT"],
    "COATING_WALL_VINYL_WALLPAPER": ["OPR_WALL_PLASTER", "OPR_WALL_PUTTY", "OPR_WALL_WALLPAPER"],
    "COATING_WALL_NON_WOVEN_WALLPAPER": ["OPR_WALL_PLASTER", "OPR_WALL_PUTTY", "OPR_WALL_WALLPAPER"],
    "COATING_WALL_CERAMIC_TILE": ["OPR_WALL_PLASTER", "OPR_WALL_TILE_INSTALL"],
    "COATING_WALL_DECORATIVE_PLASTER": ["OPR_WALL_PLASTER"],
}

CEILING_OPERATIONS_BY_COVERING = {
    "COATING_CEILING_WATER_BASED_PAINT": ["OPR_CEILING_PAINT"],
    "COATING_CEILING_WHITEWASH": [],
    "COATING_CEILING_STRETCH": [],
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _operation_index(artifact_set: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    operations = artifact_set["operations_v1.json"]["items"]
    return {operation["operation_id"]: operation for operation in operations}


def _quantity_from_source(quantity_source: str, geometry: dict[str, float]) -> float:
    if quantity_source not in geometry:
        raise ArtifactValidationError(
            error_code="ERR_ARTIFACT_REFERENCE_INVALID",
            message="Operation quantity source is not supported by geometry.",
            artifact_file="operations_v1.json",
            field="quantity_source",
            details={"quantity_source": quantity_source},
        )

    return geometry[quantity_source]


def _operation_to_output(operation: dict[str, Any], geometry: dict[str, float]) -> dict[str, Any]:
    quantity = _quantity_from_source(operation["quantity_source"], geometry)

    return {
        "operation_id": operation["operation_id"],
        "operation_name": operation["operation_name"],
        "stage": operation["stage"],
        "surface_type": operation["surface_type"],
        "quantity": round(quantity, 2),
        "unit": operation["default_unit"],
        "source_rule_id": f"execution_rule:{operation['operation_id']}",
        "sort_order": operation["sort_order"],
        "is_required": True,
        "warnings": [],
    }


def _append_operation_ids_for_room(room) -> list[str]:
    operation_ids: list[str] = [
        "OPR_FLOOR_PREP",
        "OPR_WALL_PREP",
        "OPR_CEILING_PREP",
    ]

    if room.zone == "WET":
        operation_ids.append("OPR_FLOOR_WATERPROOFING")
        if room.wall_covering == "COATING_WALL_CERAMIC_TILE":
            operation_ids.append("OPR_WALL_WATERPROOFING")

    operation_ids.extend(WALL_OPERATIONS_BY_COVERING.get(room.wall_covering, []))
    operation_ids.extend(CEILING_OPERATIONS_BY_COVERING.get(room.ceiling_covering, []))
    operation_ids.extend(FLOOR_INSTALL_OPERATION_BY_COVERING.get(room.floor_covering, []))

    return operation_ids


def generate_execution_operations(room, artifact_set: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    operation_by_id = _operation_index(artifact_set)
    geometry = calculate_room_geometry(room.length_m, room.width_m, room.height_m).model_dump()
    operation_ids = _append_operation_ids_for_room(room)

    output: list[dict[str, Any]] = []
    for operation_id in operation_ids:
        operation = operation_by_id.get(operation_id)
        if operation is None:
            raise ArtifactValidationError(
                error_code="ERR_ARTIFACT_REFERENCE_INVALID",
                message="Required operation definition is missing.",
                artifact_file="operations_v1.json",
                field="operation_id",
                details={"operation_id": operation_id},
            )

        output.append(_operation_to_output(operation, geometry))

    return sorted(output, key=lambda item: item["sort_order"])


def build_execution_summary(room, artifact_set: dict[str, dict[str, Any]]) -> dict[str, Any]:
    manifest = artifact_set.get("artifact_manifest_v1.json", {})
    return {
        "room_id": room.room_id,
        "operations": generate_execution_operations(room, artifact_set),
        "generated_at": utc_now_iso(),
        "artifact_version": manifest.get("artifact_set_version", "v1"),
    }
