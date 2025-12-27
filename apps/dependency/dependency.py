from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from apps.core.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]  # Dependency injection to get a database session using Depends