from app.artifacts.loader import load_artifact_set
from app.domain.material_engine import build_material_consumption_summary


class WetTileRoom:
    room_id = "room-1"
    length_m = 4.0
    width_m = 3.0
    height_m = 2.7
    zone = "WET"
    floor_covering = "COATING_FLOOR_PORCELAIN_TILE"
    wall_covering = "COATING_WALL_CERAMIC_TILE"
    ceiling_covering = "COATING_CEILING_WATER_BASED_PAINT"


def test_material_explanation_links_material_to_operation_surface_coating_and_zone():
    summary = build_material_consumption_summary(WetTileRoom(), load_artifact_set())

    floor_tile = next(
        item
        for item in summary["items"]
        if item["source_operation_id"] == "OPR_FLOOR_TILE_INSTALL"
        and item["material_id"] == "MAT_PORCELAIN_TILE"
    )

    explanation = floor_tile["explanation"]

    assert explanation["operation"]["operation_id"] == "OPR_FLOOR_TILE_INSTALL"
    assert explanation["operation"]["operation_name"] == "Floor tile installation"
    assert explanation["operation"]["surface_type"] == "FLOOR"
    assert explanation["operation"]["stage"] == "STG_FINISH"

    assert explanation["selection_context"]["zone"] == "WET"
    assert explanation["selection_context"]["coating_id"] == "COATING_FLOOR_PORCELAIN_TILE"
    assert explanation["selection_context"]["surface_type"] == "FLOOR"

    assert explanation["calculation"]["formula_type"] == "AREA_BASED"
    assert explanation["calculation"]["formula"] == "base_quantity * consumption_norm * loss_factor"
    assert explanation["calculation"]["base_quantity"] == 12.0
    assert explanation["calculation"]["calculated_quantity"] == 13.2

    assert explanation["packaging"]["package_size"] == 1.44
    assert explanation["packaging"]["package_count"] == 10
    assert explanation["packaging"]["rounding_rule"] == "ceil(calculated_quantity / package_size)"
