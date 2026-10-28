from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.contact import ContactCreate, ContactResponse
from app.services.contact_service import create_contact_message, send_contact_email

router = APIRouter(prefix="/api/contact", tags=["contact"])


@router.post(
    "",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
)
def submit_contact(
    payload: ContactCreate,
    db: Session = Depends(get_db),
) -> ContactResponse:
    try:
        send_contact_email(payload)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The message could not be emailed. Please try again later.",
        )

    try:
        create_contact_message(db, payload)
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Your email was sent, but the message could not be saved.",
        )

    return ContactResponse(
        success=True,
        message="Thanks — your message has been received.",
    )
