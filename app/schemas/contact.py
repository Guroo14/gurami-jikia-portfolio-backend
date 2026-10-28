from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    message: str = Field(min_length=10, max_length=2000)


class ContactResponse(BaseModel):
    success: bool
    message: str
