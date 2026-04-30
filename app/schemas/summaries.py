from pydantic import BaseModel

from app.domain.geometry import RoomGeometry


class CoreSummary(BaseModel):
    room_id: str
    room_name: str
    zone: str
    geometry: RoomGeometry
    coverings: dict[str, str]


class ExecutionOperation(BaseModel):
    operation_id: str
    operation_name: str
    stage: str
    surface_type: str
    quantity: float
    unit: str
    source_rule_id: str
    sort_order: int
    is_required: bool
    warnings: list[str] = []


class ExecutionSummary(BaseModel):
    room_id: str
    operations: list[ExecutionOperation]
    generated_at: str
    artifact_version: str
