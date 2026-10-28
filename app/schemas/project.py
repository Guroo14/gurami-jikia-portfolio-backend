from pydantic import BaseModel


class ProjectResponse(BaseModel):
    id: str
    title: str
    description: str
    category: str
    technologies: list[str]
    github_url: str | None = None
    live_demo_url: str | None = None
    image: str
    featured: bool
    status: str | None = None
