from pydantic import BaseModel

from app.domain.geometry import RoomGeometry


class CoreSummary(BaseModel):
    room_id: str
    room_name: str
    zone: str
    geometry: RoomGeometry
    coverings: dict[str, str]
