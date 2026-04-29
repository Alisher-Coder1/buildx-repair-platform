from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProjectCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    project_name: str = Field(..., min_length=1)


class ProjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    project_id: str
    project_name: str
    status: str
    created_at: datetime
    updated_at: datetime


class ProjectDetail(ProjectRead):
    rooms: list = []
