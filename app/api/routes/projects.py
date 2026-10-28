from fastapi import APIRouter

from app.schemas.project import ProjectResponse
from app.services.project_service import get_projects

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("", response_model=list[ProjectResponse])
def projects() -> list[dict]:
    return get_projects()
