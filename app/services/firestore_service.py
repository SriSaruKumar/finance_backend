from firebase_admin import firestore
from app.models.transaction import TransactionCreate, Transaction
import uuid

db = firestore.client()

# -------------------------------
# TRANSACTIONS
# -------------------------------

def create_transaction(user_id: str, transaction: TransactionCreate) -> Transaction:
    doc_id = str(uuid.uuid4())
    data = transaction.dict()
    data.update({"user_id": user_id})
    print(f"🔹 Creating transaction for user_id={user_id} with data={data}")
    db.collection("transactions").document(doc_id).set(data)
    print(f"✅ Transaction created with doc_id={doc_id}")
    return Transaction(id=doc_id, user_id=user_id, **transaction.dict())

def get_transactions(user_id: str):
    print(f"🔹 Fetching transactions for user_id={user_id}")
    docs = db.collection("transactions").where("user_id", "==", user_id).stream()
    transactions = []
    for doc in docs:
        tx_data = doc.to_dict()
        print(f"  🔸 Found transaction doc_id={doc.id} data={tx_data}")
        transactions.append(Transaction(id=doc.id, **tx_data))
    print(f"✅ Total transactions fetched: {len(transactions)}")
    return transactions

def update_transaction(user_id: str, transaction_id: str, update_data: dict):
    print(f"🔹 Updating transaction_id={transaction_id} for user_id={user_id} with update_data={update_data}")
    doc_ref = db.collection("transactions").document(transaction_id)
    doc = doc_ref.get()
    if doc.exists and doc.to_dict().get("user_id") == user_id:
        doc_ref.update(update_data)
        print("✅ Transaction updated successfully")
        return True
    print("❌ Transaction update failed: not found or user mismatch")
    return False

def delete_transaction(user_id: str, transaction_id: str):
    print(f"🔹 Deleting transaction_id={transaction_id} for user_id={user_id}")
    doc_ref = db.collection("transactions").document(transaction_id)
    doc = doc_ref.get()
    if doc.exists and doc.to_dict().get("user_id") == user_id:
        doc_ref.delete()
        print("✅ Transaction deleted successfully")
        return True
    print("❌ Transaction delete failed: not found or user mismatch")
    return False

# -------------------------------
# BUDGETS
# -------------------------------

def add_budget(user_id: str, category: str, limit: float):
    """Create or overwrite a budget category for a user"""
    print(f"🔹 Adding/updating budget for user_id={user_id}, category={category}, limit={limit}")
    doc_ref = db.collection("users").document(user_id).collection("budgets").document(category)
    doc_ref.set({"limit": limit})
    print("✅ Budget added/updated successfully")
    return {"category": category, "limit": limit}

def get_budgets(user_id: str):
    print(f"🔹 Fetching budgets for user_id={user_id}")
    docs = db.collection("users").document(user_id).collection("budgets").stream()
    budgets = [{"id": doc.id, **doc.to_dict()} for doc in docs]
    for b in budgets:
        print(f"  🔸 Budget: {b}")
    print(f"✅ Total budgets fetched: {len(budgets)}")
    return budgets
