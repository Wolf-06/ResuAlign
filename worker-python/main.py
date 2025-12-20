from fastapi import FastAPI
from app.api.v1.endpoints import auth
from app.db.base import Base
from app.db.session import engine