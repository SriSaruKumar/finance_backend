from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.api.deps import get_current_user
from app.models.transaction import TransactionCreate, Transaction
from app.services.firestore_service import (
    create_transaction,
    get_transactions,
    update_transaction,
    delete_transaction,
)

router = APIRouter(prefix="/transactions", tags=["Transactions"])

# Create transaction
@router.post("", response_model=Transaction)
def create_tx(transaction: TransactionCreate, user: dict = Depends(get_current_user)):
    return create_transaction(user_id=user["uid"], transaction=transaction)

# Get all transactions
@router.get("", response_model=List[Transaction])
def list_tx(user: dict = Depends(get_current_user)):
    return get_transactions(user_id=user["uid"])

# Update transaction
@router.put("/{transaction_id}")
def update_tx(transaction_id: str, update_data: dict, user: dict = Depends(get_current_user)):
    success = update_transaction(user_id=user["uid"], transaction_id=transaction_id, update_data=update_data)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found or unauthorized")
    return {"message": "Transaction updated"}

# Delete transaction
@router.delete("/{transaction_id}")
def delete_tx(transaction_id: str, user: dict = Depends(get_current_user)):
    success = delete_transaction(user_id=user["uid"], transaction_id=transaction_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found or unauthorized")
    return {"message": "Transaction deleted"}
