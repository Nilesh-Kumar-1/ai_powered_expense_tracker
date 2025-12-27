from fastapi import FastAPI
from apps import models
from apps.routers.users import users
from apps.routers.auth import auth
from apps.routers.expenses import expenses
from apps.core.database import engine


app = FastAPI(
    title="AI Powered Expense Tracker",
    description="A AI powered expense tracker application to help users manage and track their expenses efficiently.",
    version="1.0.0",
)

models.Base.metadata.create_all(bind=engine) # Create the database tables if they don't exist mentioned in models.py using the engine from database.py

app.include_router(users.router) # Include the auth router from models.py for authentication endpoints
app.include_router(auth.router) # Include the auth router from models.py for authentication endpoints
app.include_router(expenses.router) # Include the auth router from models.py for authentication endpoints
# app.include_router(todos.router) # Include the auth router from models.py for authentication endpoints
# app.include_router(admin.router) # Include the admin router from models.py for admin-specific endpoints
# app.include_router(users.router) # Include the admin router from models.py for admin-specific endpoints