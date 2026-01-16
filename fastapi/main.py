from fastapi import FastAPI
from pymongo import MongoClient
from minio import Minio
import os

print("Starting Cloud Banking API...")

app = FastAPI(title="Cloud Banking API")

# MongoDB (safe default for CI)
mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
mongo_client = MongoClient(mongo_url)
db = mongo_client["bankdb"]

# MinIO (optional – only initialize if configured)
minio_client = None

minio_endpoint = os.getenv("MINIO_ENDPOINT")
minio_access_key = os.getenv("MINIO_ACCESS_KEY")
minio_secret_key = os.getenv("MINIO_SECRET_KEY")

if minio_endpoint and minio_access_key and minio_secret_key:
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )
    print("MinIO client initialized")
else:
    print("MinIO not configured – running without object storage")

@app.get("/")
def root():
    return {"message": "Cloud Banking API is running"}
