from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.errors import ErrorCode
from app.core.responses import error_item, error_response, success_response
from app.db.session import get_db
from app.services.room_service import get_room
from app.services.summary_service import build_core_summary

router = APIRouter(prefix="/rooms", tags=["summaries"])


@router.get("/{room_id}/core-summary")
def get_room_core_summary(room_id: str, db: Session = Depends(get_db)):
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

    return success_response(build_core_summary(room))
