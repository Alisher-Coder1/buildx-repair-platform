from app.db.models import Room
from app.domain.geometry import calculate_room_geometry


def build_core_summary(room: Room) -> dict:
    geometry = calculate_room_geometry(room.length_m, room.width_m, room.height_m)
    return {
        "room_id": room.room_id,
        "room_name": room.room_name,
        "zone": room.zone,
        "geometry": geometry.model_dump(),
        "coverings": {
            "floor_covering": room.floor_covering,
            "wall_covering": room.wall_covering,
            "ceiling_covering": room.ceiling_covering,
        },
    }
