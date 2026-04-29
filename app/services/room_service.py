from sqlalchemy.orm import Session

from app.db.models import Project, Room
from app.schemas.room import RoomCreate


def create_room(db: Session, project_id: str, payload: RoomCreate) -> Room | None:
    project = db.get(Project, project_id)
    if project is None:
        return None

    room = Room(
        project_id=project_id,
        room_name=payload.room_name,
        length_m=payload.length_m,
        width_m=payload.width_m,
        height_m=payload.height_m,
        zone=payload.zone.value,
        floor_covering=payload.floor_covering,
        wall_covering=payload.wall_covering,
        ceiling_covering=payload.ceiling_covering,
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


def get_room(db: Session, room_id: str) -> Room | None:
    return db.get(Room, room_id)
