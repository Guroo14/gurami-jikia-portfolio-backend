from html import escape

import resend
from sqlalchemy.orm import Session

from app.config import get_settings
from app.models.contact import ContactMessage
from app.schemas.contact import ContactCreate


def send_contact_email(payload: ContactCreate) -> None:
    settings = get_settings()
    if not settings.resend_api_key or not settings.contact_to_email:
        raise RuntimeError("Email settings are missing. Configure RESEND_API_KEY and CONTACT_TO_EMAIL.")

    resend.api_key = settings.resend_api_key
    safe_name = escape(payload.name)
    safe_email = escape(str(payload.email))
    safe_message = escape(payload.message).replace("\n", "<br>")

    resend.Emails.send({
        "from": settings.resend_from_email,
        "to": [settings.contact_to_email],
        "reply_to": str(payload.email),
        "subject": f"New portfolio message from {payload.name}",
        "html": (
            f"<h2>New portfolio contact message</h2>"
            f"<p><strong>Name:</strong> {safe_name}</p>"
            f"<p><strong>Email:</strong> {safe_email}</p>"
            f"<p><strong>Message:</strong><br>{safe_message}</p>"
        ),
        "text": f"Name: {payload.name}\nEmail: {payload.email}\n\n{payload.message}",
    })


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
