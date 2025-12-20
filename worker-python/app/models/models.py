import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class User(Base):
    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    encrypted_api_key=Column(String, nullable=True)

    is_active=Column(Boolean, default=True)
    created_at= Column(DateTime(timezone=True), server_default=func.now())

    #Relationships
    profile = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete-orphan")


class Profile(Base):

    id=Column(Integer, primary_key=True, index=True)
    user_id= Column(UUID(as_uuid=True), ForeignKey("user.id"), unique=True, nullable=False)

    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)
    contact_email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    linkedin_url = Column(String, nullable=True)
    
    address = Column(JSONB, default=dict)
    custom_fields= Column(JSONB, default=dict)

    user = relationship("User", back_populates="Profile")