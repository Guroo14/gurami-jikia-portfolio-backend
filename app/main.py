from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import contact, health, projects
from app.config import get_settings
from app.database import Base, engine
from app.models.contact import ContactMessage  # noqa: F401

settings = get_settings()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="REST API for Gurami Jikia's personal portfolio.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(health.router)
app.include_router(projects.router)
app.include_router(contact.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Gurami Jikia Portfolio API"}
