import os
import json
import base64
import firebase_admin
from firebase_admin import credentials

# Decode the environment variable
decoded_json = base64.b64decode(os.environ["FIREBASE_SERVICE_ACCOUNT"]).decode("utf-8")
service_account_info = json.loads(decoded_json)

cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)
