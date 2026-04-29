from typing import Any

from app.core.errors import ErrorSeverity


def success_response(data: Any, warnings: list | None = None, meta: dict | None = None) -> dict:
    return {
        "success": True,
        "data": data,
        "warnings": warnings or [],
        "meta": meta or {},
    }


def error_item(
    error_code: str,
    message: str,
    field: str | None = None,
    entity: str | None = None,
    severity: ErrorSeverity = ErrorSeverity.BLOCKING,
    details: dict | None = None,
) -> dict:
    return {
        "error_code": error_code,
        "message": message,
        "field": field,
        "entity": entity,
        "severity": severity.value if hasattr(severity, "value") else severity,
        "details": details or {},
    }


def error_response(errors: list[dict], warnings: list | None = None, meta: dict | None = None) -> dict:
    return {
        "success": False,
        "errors": errors,
        "warnings": warnings or [],
        "meta": meta or {},
    }
