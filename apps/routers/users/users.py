from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from apps.dependency.dependency import db_dependency
from apps.routers.users.user_schema import UserCreateRequest
from apps.models import User, Expense, Label
from apps.routers.auth.auth import user_dependency
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["users"])
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.get("/retrieve/{username}/", response_model=dict)
async def get_user(username: str, db: db_dependency):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role,
        "is_active": user.is_active,
    }

@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency, user_request: UserCreateRequest):
    existing_user = db.query(User).filter(User.username == user_request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    else:
        create_user = User(
            username=user_request.username,
            email=user_request.email,
            first_name=user_request.first_name,
            last_name=user_request.last_name,
            hashed_password=bcrypt_context.hash(user_request.password),
            role=user_request.role,
            is_active=True
        )
        db.add(create_user)
        db.commit()
        return {"message": f"{create_user.username} created successfully"}

@router.delete("/delete/{username}/", status_code=status.HTTP_200_OK)
async def delete_user(username: str, db: db_dependency, user: user_dependency):
    user = db.query(User).filter(User.username == username, User.id == user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    expenses = db.query(Expense).filter(Expense.user_id == user.id).all()
    labels = db.query(Label).filter(Label.user_id == user.id).all()
    db.delete(user)
    for expense in expenses:
        db.delete(expense)
    for label in labels:
        db.delete(label)
    db.commit()
    return {"message": f"User {username} deleted successfully"}

@router.put("/update/{username}/", status_code=status.HTTP_200_OK)
async def update_user(username: str, user_request: UserCreateRequest, db: db_dependency, user: user_dependency):
    user = db.query(User).filter(User.username == username, User.id == user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.email = user_request.email # type: ignore
    user.first_name = user_request.first_name # type: ignore
    user.last_name = user_request.last_name # type: ignore
    user.is_active = user_request.is_active# type: ignore
    user.hashed_password = user_request.password # type: ignore
    user.is_active = user_request.is_active # type: ignore

    db.commit()
    return {"message": f"User {username} updated successfully"}