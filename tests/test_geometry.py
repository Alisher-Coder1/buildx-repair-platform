from app.domain.geometry import calculate_room_geometry


def test_room_geometry_for_4_by_3_by_2_7():
    geometry = calculate_room_geometry(length_m=4.0, width_m=3.0, height_m=2.7)

    assert geometry.floor_area_m2 == 12.0
    assert geometry.ceiling_area_m2 == 12.0
    assert geometry.perimeter_m == 14.0
    assert geometry.wall_area_m2 == 37.8
