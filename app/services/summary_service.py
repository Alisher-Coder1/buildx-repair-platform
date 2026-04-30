from app.artifacts.loader import load_artifact_set
from app.db.models import Room
from app.domain.execution_engine import build_execution_summary
from app.domain.geometry import calculate_room_geometry
from app.domain.material_engine import build_material_consumption_summary


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


def build_room_execution_summary(room: Room) -> dict:
    artifact_set = load_artifact_set()
    return build_execution_summary(room, artifact_set)


def build_room_material_consumption_summary(room: Room) -> dict:
    artifact_set = load_artifact_set()
    return build_material_consumption_summary(room, artifact_set)
