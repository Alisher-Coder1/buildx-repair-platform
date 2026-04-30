from typing import Any

from app.domain.material_engine import build_material_consumption_summary


def _procurement_key(item: dict[str, Any]) -> tuple[str, str]:
    return item["material_id"], item["package_id"]


def build_procurement_summary(room, artifact_set: dict[str, dict[str, Any]]) -> dict[str, Any]:
    material_summary = build_material_consumption_summary(room, artifact_set)
    grouped: dict[tuple[str, str], dict[str, Any]] = {}

    for item in material_summary["items"]:
        key = _procurement_key(item)

        if key not in grouped:
            grouped[key] = {
                "procurement_item_id": f"{item['material_id']}:{item['package_id']}",
                "material_id": item["material_id"],
                "material_name": item["material_name"],
                "required_quantity": 0.0,
                "unit": item["unit"],
                "package_id": item["package_id"],
                "package_size": item["package_size"],
                "package_count": 0,
                "purchase_quantity": 0.0,
                "source_operation_ids": [],
                "estimated_total_price": None,
                "price_status": "MISSING_PRICE",
            }

        current = grouped[key]
        current["required_quantity"] += item["calculated_quantity"]
        current["package_count"] += item["package_count"]

        if item["source_operation_id"] not in current["source_operation_ids"]:
            current["source_operation_ids"].append(item["source_operation_id"])

    items = []
    for item in grouped.values():
        item["required_quantity"] = round(item["required_quantity"], 2)
        item["purchase_quantity"] = round(item["package_count"] * item["package_size"], 2)
        item["source_operation_ids"] = sorted(item["source_operation_ids"])
        items.append(item)

    items.sort(key=lambda row: row["material_name"])

    return {
        "room_id": room.room_id,
        "items": items,
        "estimated_total": None,
        "currency": "USD",
    }
