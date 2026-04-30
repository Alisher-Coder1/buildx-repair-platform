from app.artifacts.loader import load_artifact_set
from app.domain.execution_engine import generate_execution_operations


class FakeRoom:
    room_id = "room-1"
    length_m = 4.0
    width_m = 3.0
    height_m = 2.7
    zone = "WET"
    floor_covering = "COATING_FLOOR_PORCELAIN_TILE"
    wall_covering = "COATING_WALL_CERAMIC_TILE"
    ceiling_covering = "COATING_CEILING_WATER_BASED_PAINT"


def test_generate_execution_operations_for_wet_tile_room():
    operations = generate_execution_operations(FakeRoom(), load_artifact_set())
    operation_ids = [item["operation_id"] for item in operations]

    assert "OPR_FLOOR_PREP" in operation_ids
    assert "OPR_WALL_PREP" in operation_ids
    assert "OPR_CEILING_PREP" in operation_ids
    assert "OPR_FLOOR_WATERPROOFING" in operation_ids
    assert "OPR_WALL_WATERPROOFING" in operation_ids
    assert "OPR_WALL_TILE_INSTALL" in operation_ids
    assert "OPR_FLOOR_TILE_INSTALL" in operation_ids
    assert "OPR_CEILING_PAINT" in operation_ids


def test_execution_operation_quantities_are_from_geometry():
    operations = generate_execution_operations(FakeRoom(), load_artifact_set())

    wall_tile = next(item for item in operations if item["operation_id"] == "OPR_WALL_TILE_INSTALL")
    floor_tile = next(item for item in operations if item["operation_id"] == "OPR_FLOOR_TILE_INSTALL")

    assert wall_tile["quantity"] == 37.8
    assert floor_tile["quantity"] == 12.0


def test_execution_operations_are_sorted_by_sort_order():
    operations = generate_execution_operations(FakeRoom(), load_artifact_set())
    sort_orders = [item["sort_order"] for item in operations]

    assert sort_orders == sorted(sort_orders)
