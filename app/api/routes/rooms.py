from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.errors import ErrorCode
from app.core.responses import error_item, error_response, success_response
from app.db.session import get_db
from app.schemas.room import RoomCreate, RoomRead
from app.services.room_service import create_room, get_room

router = APIRouter(tags=["rooms"])


@router.post("/projects/{project_id}/rooms")
def create_room_endpoint(project_id: str, payload: RoomCreate, db: Session = Depends(get_db)):
    room = create_room(db, project_id, payload)
    if room is None:
        raise HTTPException(
            status_code=404,
            detail=error_response([
                error_item(
                    ErrorCode.ERR_NOT_FOUND.value,
                    "Project not found.",
                    field="project_id",
                    entity="Project",
                )
            ]),
        )

    return success_response(RoomRead.model_validate(room).model_dump(mode="json"))


@router.get("/rooms/{room_id}")
def get_room_endpoint(room_id: str, db: Session = Depends(get_db)):
    room = get_room(db, room_id)
    if room is None:
        raise HTTPException(
            status_code=404,
            detail=error_response([
                error_item(
                    ErrorCode.ERR_NOT_FOUND.value,
                    "Room not found.",
                    field="room_id",
                    entity="Room",
                )
            ]),
        )

    return success_response(RoomRead.model_validate(room).model_dump(mode="json"))
