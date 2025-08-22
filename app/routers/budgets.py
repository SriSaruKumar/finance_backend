from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.api.deps import get_current_user
from app.services.firestore_service import add_budget, get_budgets
from pydantic import BaseModel


router = APIRouter(prefix="/budgets", tags=["Budgets"])

# Fetch all budgets
@router.get("/", response_model=List[dict])
def list_budgets(user: dict = Depends(get_current_user)):
    return get_budgets(user_id=user["uid"])

# Create or update a budget
class BudgetCreate(BaseModel):
    category: str
    limit: float

@router.post("/", response_model=dict)
def create_budget(budget: BudgetCreate, user: dict = Depends(get_current_user)):
    return add_budget(user_id=user["uid"], category=budget.category, limit=budget.limit)
