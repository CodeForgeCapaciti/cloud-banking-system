from fastapi import FastAPI
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

@app.get("/")
def root():
    return {"message": "Cloud Banking API is running"}

@app.post("/accounts")
def create_account(name: str, balance: float):
    account = {"name": name, "balance": balance}
    db.accounts.insert_one(account)
    return {"status": "Account created", "account": account}
