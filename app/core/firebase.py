import firebase_admin
from firebase_admin import credentials
from app.core.config import settings

# Prevent reinitialization if already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)
