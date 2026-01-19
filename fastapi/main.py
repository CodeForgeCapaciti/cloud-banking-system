from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from minio import Minio
import os

app = FastAPI(title="Cloud Banking API")

# MongoDB connection
mongo_client = MongoClient(os.getenv("MONGO_URL"))
db = mongo_client["bankdb"]

# MinIO connection
minio_client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

# ------------------------
# Pydantic model for JSON body
# ------------------------
class Account(BaseModel):
    name: str
    balance: float

@app.get("/")
def root():
    return {"message": "Cloud Banking API is running"}

@app.post("/accounts")
def create_account(account: Account):
    # Insert JSON data into MongoDB
    db.accounts.insert_one(account.dict())
    return {"status": "Account created", "account": account}
