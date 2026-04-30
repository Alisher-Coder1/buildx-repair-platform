from app.artifacts.loader import load_artifact_set
from app.domain.cost_engine import build_cost_summary
from app.domain.procurement_engine import build_procurement_summary


class WetTileRoom:
    room_id = "room-1"
    length_m = 4.0
    width_m = 3.0
    height_m = 2.7
    zone = "WET"
    floor_covering = "COATING_FLOOR_PORCELAIN_TILE"
    wall_covering = "COATING_WALL_CERAMIC_TILE"
    ceiling_covering = "COATING_CEILING_WATER_BASED_PAINT"


def test_procurement_summary_groups_material_packages():
    summary = build_procurement_summary(WetTileRoom(), load_artifact_set())

    material_ids = [item["material_id"] for item in summary["items"]]

    assert "MAT_PORCELAIN_TILE" in material_ids
    assert "MAT_TILE_ADHESIVE" in material_ids
    assert "MAT_GROUT" in material_ids
    assert summary["currency"] == "USD"


def test_procurement_purchase_quantity_is_package_count_times_package_size():
    summary = build_procurement_summary(WetTileRoom(), load_artifact_set())

    for item in summary["items"]:
        assert item["purchase_quantity"] == round(item["package_count"] * item["package_size"], 2)
        assert item["package_count"] >= 1


def test_cost_summary_has_missing_price_status():
    summary = build_cost_summary(WetTileRoom(), load_artifact_set())

    assert summary["currency"] == "USD"
    assert summary["material_total"] is None
    assert summary["grand_total"] is None

    assert len(summary["items"]) > 0
    for item in summary["items"]:
        assert item["unit_price"] is None
        assert item["total_price"] is None
        assert item["price_status"] == "MISSING_PRICE"
