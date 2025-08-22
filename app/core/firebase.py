import os
import json
import base64
import firebase_admin
from firebase_admin import credentials

# Decode the environment variable
service_account_info = json.loads(base64.b64decode(os.environ["FIREBASE_SERVICE_ACCOUNT"]))

cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)
