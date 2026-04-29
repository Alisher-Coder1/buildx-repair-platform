from typing import Any

from pydantic import BaseModel


class ValidationErrorItem(BaseModel):
    error_code: str
    message: str
    field: str | None = None
    entity: str | None = None
    severity: str = "BLOCKING"
    details: dict[str, Any] = {}


class ErrorEnvelope(BaseModel):
    success: bool = False
    errors: list[ValidationErrorItem]
    warnings: list[ValidationErrorItem] = []
    meta: dict[str, Any] = {}
