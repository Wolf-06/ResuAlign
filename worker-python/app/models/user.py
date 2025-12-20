from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator
from typing import Optional, Dict, Any
from uuid import UUID

class UserBase(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v
    

class ProfileBase(BaseModel):
    contact_email: Optional[EmailStr]=None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    linkedin_url :Optional[str]= None
    github_url :Optional[str]= None
    contact_phoneNo: Optional[int]=None

    # the JSONB field to store the additional profile data
    custom_fields: Dict[str, Any]= Field(default_factory=dict)

class ProfileCreate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    user_id: UUID

    model_config = ConfigDict(from_attributes=True)

class UserResponse(UserBase):
    id: UUID
    email: EmailStr
    profile : Optional[ProfileResponse] = None

    model_config = ConfigDict(from_attributes=True)

