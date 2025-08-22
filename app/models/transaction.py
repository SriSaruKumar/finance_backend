from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base model with shared fields
class TransactionBase(BaseModel):
    amount: float
    category: str
    type: str  # spend/income
    note: Optional[str] = None
    date: datetime

# Model for creating a transaction
class TransactionCreate(TransactionBase):
    pass  # inherits everything from TransactionBase

# Model for reading a transaction
class Transaction(TransactionBase):
    id: str
    user_id: str
