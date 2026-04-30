from typing import Any

from app.core.errors import ErrorCode, ErrorSeverity
from app.core.responses import error_item
from app.domain.procurement_engine import build_procurement_summary


def build_cost_summary(room, artifact_set: dict[str, dict[str, Any]]) -> dict[str, Any]:
    procurement_summary = build_procurement_summary(room, artifact_set)

    items: list[dict[str, Any]] = []
    for procurement_item in procurement_summary["items"]:
        items.append(
            {
                "cost_item_id": f"COST:{procurement_item['procurement_item_id']}",
                "material_id": procurement_item["material_id"],
                "material_name": procurement_item["material_name"],
                "package_count": procurement_item["package_count"],
                "unit_price": None,
                "currency": "USD",
                "total_price": None,
                "price_status": "MISSING_PRICE",
            }
        )

    return {
        "room_id": room.room_id,
        "items": items,
        "material_total": None,
        "labor_total": None,
        "grand_total": None,
        "currency": "USD",
    }


def build_missing_price_warning() -> dict[str, Any]:
    return error_item(
        ErrorCode.MISSING_PRICE.value,
        "Some material prices are missing.",
        field="unit_price",
        entity="CostSummary",
        severity=ErrorSeverity.WARNING,
        details={},
    )
