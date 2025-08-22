from fastapi import FastAPI
from app.api import routes_auth, routes_user
from app.routers import transactions,budgets

app = FastAPI(title="Finance App")

# Routers
app.include_router(routes_auth.router, prefix="/auth", tags=["Auth"])
app.include_router(routes_user.router, prefix="/user", tags=["User"])

@app.get("/health")
def health():
    return {"status": "ok"}
@app.post("/verify-token")
async def verify_token(token: str):
    # TODO: validate the Firebase token here
    # For now, just return dummy response
    return {"message": "Token received", "token": token}
app.include_router(transactions.router)
app.include_router(budgets.router)
