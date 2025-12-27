from apps.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each user
    username = Column(String, unique=True, index=True, nullable=False) # Unique username for each user
    email = Column(String, unique=True, index=True, nullable=False) # User's email address
    hashed_password = Column(String, nullable=False) # Store hashed passwords for security
    first_name = Column(String) # Optional first name of the user
    last_name = Column(String) # Optional last name of the user
    role = Column(String, default="user") # e.g., user, admin
    is_active = Column(Boolean, default=True) # Indicates if the user account is active


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each expense
    expense_name = Column(String, nullable=False) # Name or title of the expense
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Foreign key to link to users table
    amount = Column(Integer, nullable=False) # Amount in INR
    category = Column(String) # e.g., food, travel, utilities
    description = Column(String) # Additional details about the expense
    label = Column(String) # e.g., food, travel, utilities
    created_at = Column(DateTime) # Timestamp when the expense was created
    sent_to = Column(String) # e.g., payee or recipient
    received_from = Column(String) # e.g., vendor or payer
    bank_account = Column(String) # bank account associated with the expense
    payment_method = Column(String) # e.g., credit card, cash, bank transfer
    is_recurring = Column(Boolean, default=False) # Indicates if the expense is recurring
    recurrence_interval = Column(String) # e.g., daily, weekly, monthly
    state = Column(String) # e.g., pending, cleared, disputed


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each label
    label_name = Column(String, unique=True, index=True, nullable=False) # Name of the label
    description = Column(String) # Description of the label
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Foreign key to link to users table