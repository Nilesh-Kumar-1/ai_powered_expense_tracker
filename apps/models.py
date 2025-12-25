from apps.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String, default="user")
    is_active = Column(Boolean, default=True)


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    expense_name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    category = Column(String)
    description = Column(String)
    label = Column(String)
    transaction_id = Column(String, unique=True, index=True)
    created_at = Column(DateTime)
    sent_to = Column(String)
    received_from = Column(String)
    bank_account = Column(String)
    payment_method = Column(String)
    is_recurring = Column(Boolean, default=False)
    recurrence_interval = Column(String)
    state = Column(String)


class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True)
    label_name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)