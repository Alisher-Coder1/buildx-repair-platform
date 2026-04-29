from pydantic import BaseModel


class RoomGeometry(BaseModel):
    length_m: float
    width_m: float
    height_m: float
    floor_area_m2: float
    ceiling_area_m2: float
    perimeter_m: float
    wall_area_m2: float


def round2(value: float) -> float:
    return round(value + 1e-12, 2)


def calculate_room_geometry(length_m: float, width_m: float, height_m: float) -> RoomGeometry:
    floor_area = length_m * width_m
    ceiling_area = length_m * width_m
    perimeter = 2 * (length_m + width_m)
    wall_area = perimeter * height_m

    if floor_area <= 0 or ceiling_area <= 0 or perimeter <= 0 or wall_area <= 0:
        raise ValueError("Invalid geometry quantity")

    return RoomGeometry(
        length_m=round2(length_m),
        width_m=round2(width_m),
        height_m=round2(height_m),
        floor_area_m2=round2(floor_area),
        ceiling_area_m2=round2(ceiling_area),
        perimeter_m=round2(perimeter),
        wall_area_m2=round2(wall_area),
    )
