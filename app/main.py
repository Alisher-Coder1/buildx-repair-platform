from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.routes import health, projects, rooms, summaries
from app.core.config import API_PREFIX, API_TITLE, API_VERSION
from app.core.errors import ErrorCode
from app.core.responses import error_item, error_response
from app.db.base import init_db

app = FastAPI(title=API_TITLE, version=API_VERSION)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for err in exc.errors():
        loc = err.get("loc", [])
        field = str(loc[-1]) if loc else None
        message = err.get("msg", "Validation error.")

        error_code = ErrorCode.ERR_REQUIRED_FIELD_MISSING.value
        if "extra" in err.get("type", ""):
            error_code = ErrorCode.ERR_EXTRA_FIELD_FORBIDDEN.value
        elif "greater_than_equal" in err.get("type", "") or "less_than_equal" in err.get("type", ""):
            error_code = ErrorCode.ERR_OUT_OF_RANGE.value
        elif "enum" in err.get("type", ""):
            error_code = ErrorCode.ERR_INVALID_ENUM_VALUE.value
        elif "ERR_UNSUPPORTED_COVERING" in message:
            error_code = ErrorCode.ERR_UNSUPPORTED_COVERING.value

        errors.append(
            error_item(
                error_code=error_code,
                message=message,
                field=field,
                entity="Request",
                details={"raw": str(err)},
            )
        )

    return JSONResponse(status_code=422, content=error_response(errors))


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=error_response([
            error_item(
                ErrorCode.ERR_INTERNAL_CALCULATION_ERROR.value,
                "Internal server error.",
                entity="Application",
                details={"error": str(exc)},
            )
        ]),
    )


app.include_router(health.router, prefix=API_PREFIX)
app.include_router(projects.router, prefix=API_PREFIX)
app.include_router(rooms.router, prefix=API_PREFIX)
app.include_router(summaries.router, prefix=API_PREFIX)
