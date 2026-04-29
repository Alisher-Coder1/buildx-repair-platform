from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class RoomZone(str, Enum):
    DRY = "DRY"
    WET = "WET"
    KITCHEN = "KITCHEN"


FLOOR_COVERINGS = {
    "COATING_FLOOR_LAMINATE",
    "COATING_FLOOR_PORCELAIN_TILE",
    "COATING_FLOOR_LINOLEUM",
    "COATING_FLOOR_SELF_LEVELING",
}

WALL_COVERINGS = {
    "COATING_WALL_VINYL_WALLPAPER",
    "COATING_WALL_NON_WOVEN_WALLPAPER",
    "COATING_WALL_WATER_BASED_PAINT",
    "COATING_WALL_CERAMIC_TILE",
    "COATING_WALL_DECORATIVE_PLASTER",
}

CEILING_COVERINGS = {
    "COATING_CEILING_WHITEWASH",
    "COATING_CEILING_WATER_BASED_PAINT",
    "COATING_CEILING_STRETCH",
}


class RoomCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    room_name: str = Field(..., min_length=1)
    length_m: float = Field(..., ge=0.5, le=100.0)
    width_m: float = Field(..., ge=0.5, le=100.0)
    height_m: float = Field(..., ge=0.5, le=10.0)
    zone: RoomZone
    floor_covering: str
    wall_covering: str
    ceiling_covering: str

    @model_validator(mode="after")
    def validate_coverings(self):
        if self.floor_covering not in FLOOR_COVERINGS:
            raise ValueError("ERR_UNSUPPORTED_COVERING: invalid floor_covering")
        if self.wall_covering not in WALL_COVERINGS:
            raise ValueError("ERR_UNSUPPORTED_COVERING: invalid wall_covering")
        if self.ceiling_covering not in CEILING_COVERINGS:
            raise ValueError("ERR_UNSUPPORTED_COVERING: invalid ceiling_covering")
        return self


class RoomRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    room_id: str
    project_id: str
    room_name: str
    length_m: float
    width_m: float
    height_m: float
    zone: str
    floor_covering: str
    wall_covering: str
    ceiling_covering: str
    status: str
    created_at: datetime
    updated_at: datetime
