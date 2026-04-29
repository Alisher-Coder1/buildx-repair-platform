from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.errors import ErrorCode
from app.core.responses import error_item, error_response, success_response
from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectRead
from app.services.project_service import create_project, get_project

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("")
def create_project_endpoint(payload: ProjectCreate, db: Session = Depends(get_db)):
    project = create_project(db, payload)
    return success_response(ProjectRead.model_validate(project).model_dump(mode="json"))


@router.get("/{project_id}")
def get_project_endpoint(project_id: str, db: Session = Depends(get_db)):
    project = get_project(db, project_id)
    if project is None:
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

    data = ProjectRead.model_validate(project).model_dump(mode="json")
    data["rooms"] = []
    return success_response(data)
