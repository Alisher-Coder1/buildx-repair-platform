from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.errors import ErrorCode
from app.core.responses import error_item, error_response, success_response
from app.db.session import get_db
from app.domain.cost_engine import build_missing_price_warning
from app.services.room_service import get_room
from app.services.summary_service import (
    build_core_summary,
    build_room_cost_summary,
    build_room_execution_summary,
    build_room_material_consumption_summary,
    build_room_procurement_summary,
)

router = APIRouter(prefix="/rooms", tags=["summaries"])


def _get_room_or_404(room_id: str, db: Session):
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

    return room


@router.get("/{room_id}/core-summary")
def get_room_core_summary(room_id: str, db: Session = Depends(get_db)):
    room = _get_room_or_404(room_id, db)
    return success_response(build_core_summary(room))


@router.get("/{room_id}/execution-summary")
def get_room_execution_summary(room_id: str, db: Session = Depends(get_db)):
    room = _get_room_or_404(room_id, db)
    return success_response(build_room_execution_summary(room))


@router.get("/{room_id}/material-consumption-summary")
def get_room_material_consumption_summary(room_id: str, db: Session = Depends(get_db)):
    room = _get_room_or_404(room_id, db)
    return success_response(build_room_material_consumption_summary(room))


@router.get("/{room_id}/cost-summary")
def get_room_cost_summary(room_id: str, db: Session = Depends(get_db)):
    room = _get_room_or_404(room_id, db)
    return success_response(
        build_room_cost_summary(room),
        warnings=[build_missing_price_warning()],
    )


@router.get("/{room_id}/procurement-summary")
def get_room_procurement_summary(room_id: str, db: Session = Depends(get_db)):
    room = _get_room_or_404(room_id, db)
    return success_response(build_room_procurement_summary(room))
