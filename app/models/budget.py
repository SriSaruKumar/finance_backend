from pydantic import BaseModel
from typing import Optional

class BudgetBase(BaseModel):
    category: Optional[str] = "Monthly"
    limit: float

class BudgetCreate(BudgetBase):
    pass

class Budget(BudgetBase):
    id: str
    user_id: str
