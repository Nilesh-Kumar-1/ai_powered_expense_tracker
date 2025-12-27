from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import date
class ExpenseCreateRequest(BaseModel):

    expense_name : str # Name or title of the expense
    amount : float # Amount in INR
    category : str # e.g., food, travel, utilities
    description : str # Additional details about the expense
    label : str # e.g., food, travel, utilities
    created_at : date # Timestamp when the expense was created
    sent_to : str # e.g., payee or recipient
    received_from : str # e.g., vendor or payer
    bank_account : str # bank account associated with the expense
    payment_method : str # e.g., credit card, cash, bank transfer
    is_recurring : bool # Indicates if the expense is recurring
    recurrence_interval : str # e.g., daily, weekly, monthly
    state : str # e.g., pending, cleared, disputed