from sqlalchemy.orm import Session

from app.models.contact import ContactMessage
from app.schemas.contact import ContactCreate


def create_contact_message(db: Session, payload: ContactCreate) -> ContactMessage:
    record = ContactMessage(
        name=payload.name,
        email=str(payload.email),
        message=payload.message,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
