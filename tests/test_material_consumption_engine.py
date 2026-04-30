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


def test_material_consumption_summary_for_wet_tile_room():
    summary = build_material_consumption_summary(WetTileRoom(), load_artifact_set())
    material_ids = [item["material_id"] for item in summary["items"]]

    assert "MAT_PRIMER" in material_ids
    assert "MAT_WATERPROOFING" in material_ids
    assert "MAT_TILE_ADHESIVE" in material_ids
    assert "MAT_GROUT" in material_ids
    assert "MAT_PORCELAIN_TILE" in material_ids
    assert "MAT_PAINT_CEILING" in material_ids


def test_floor_tile_package_count():
    summary = build_material_consumption_summary(WetTileRoom(), load_artifact_set())

    floor_tile = next(
        item for item in summary["items"]
        if item["source_operation_id"] == "OPR_FLOOR_TILE_INSTALL"
        and item["material_id"] == "MAT_PORCELAIN_TILE"
    )

    assert floor_tile["calculated_quantity"] == 13.2
    assert floor_tile["package_count"] == 10


def test_floor_tile_adhesive_package_count():
    summary = build_material_consumption_summary(WetTileRoom(), load_artifact_set())

    adhesive = next(
        item for item in summary["items"]
        if item["source_operation_id"] == "OPR_FLOOR_TILE_INSTALL"
        and item["material_id"] == "MAT_TILE_ADHESIVE"
    )

    assert adhesive["calculated_quantity"] == 59.4
    assert adhesive["package_count"] == 3


def test_wall_waterproofing_package_count():
    summary = build_material_consumption_summary(WetTileRoom(), load_artifact_set())

    waterproofing = next(
        item for item in summary["items"]
        if item["source_operation_id"] == "OPR_WALL_WATERPROOFING"
        and item["material_id"] == "MAT_WATERPROOFING"
    )

    assert waterproofing["calculated_quantity"] == 49.9
    assert waterproofing["package_count"] == 3
