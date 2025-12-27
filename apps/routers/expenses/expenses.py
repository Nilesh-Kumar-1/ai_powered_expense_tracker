from fastapi import APIRouter, Depends, HTTPException, status
from apps.dependency.dependency import db_dependency
from apps.models import Expense
from apps.routers.expenses.expenses_schema import ExpenseCreateRequest
from apps.routers.auth.auth import user_dependency

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_expense(db: db_dependency, expense_request: ExpenseCreateRequest, user: user_dependency):
    expense = Expense(**expense_request.model_dump(), user_id=user.id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return {"message": "Expense created successfully"}

@router.get("/list/")
async def list_expenses(db: db_dependency, user: user_dependency):
    expenses = db.query(Expense).filter(Expense.user_id == user.id).all()
    return expenses

@router.delete("/delete/{expense_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_expense(expense_id: int, db: db_dependency, user: user_dependency):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted successfully"}

@router.put("/update/{expense_id}/")
async def update_expense(expense_id: int, expense_request: ExpenseCreateRequest, db: db_dependency, user: user_dependency):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    for key, value in expense_request.model_dump().items():
        setattr(expense, key, value)
    db.commit()
    db.refresh(expense)
    return {"message": "Expense updated successfully"}

@router.get("/detail/{expense_id}/")
async def get_expense_detail(expense_id: int, db: db_dependency, user: user_dependency):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.user_id == user.id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found")
    return expense