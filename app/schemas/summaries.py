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


class MaterialConsumptionItem(BaseModel):
    item_id: str
    room_id: str
    source_operation_id: str
    rule_id: str
    material_id: str
    material_name: str
    formula_type: str
    base_quantity: float
    calculated_quantity: float
    unit: str
    loss_factor: float
    layer_count: int | None = None
    thickness_mm: float | None = None
    package_id: str
    package_size: float
    package_count: int
    warnings: list[str] = []


class MaterialConsumptionSummary(BaseModel):
    room_id: str
    items: list[MaterialConsumptionItem]
    calculated_at: str
    artifact_version: str
