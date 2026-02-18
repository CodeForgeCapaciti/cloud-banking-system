# main.py
from dotenv import load_dotenv
load_dotenv()

import logging
from pythonjsonlogger import jsonlogger
import os
import time
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from pymongo import MongoClient
from minio import Minio
from prometheus_client import Counter, Histogram, generate_latest


# Instrument the app to expose metrics
Instrumentator().instrument(app).expose(app)
# ========================
# JSON Logging Setup
# ========================
logger = logging.getLogger("cloud_banking_api")
logger.setLevel(logging.INFO)

log_handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s'
)
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# ========================
# FastAPI App
# ========================
app = FastAPI(title="Cloud Banking API")

# ========================
# MongoDB Connection
# ========================
mongo_client = MongoClient(os.getenv("MONGO_URL"))
db = mongo_client["bankdb"]

# ========================
# MinIO Connection
# ========================
minio_client = Minio(
    os.getenv("MINIO_ENDPOINT"),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

# ========================
# Prometheus Metrics
# ========================
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"]
)

# ========================
# Middleware for metrics and logging
# ========================
@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    # Update Prometheus metrics
    REQUEST_COUNT.labels(
        request.method, request.url.path, str(response.status_code)
    ).inc()
    REQUEST_LATENCY.labels(request.method, request.url.path).observe(duration)

    # Log request info
    logger.info(
        "request",
        extra={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_sec": duration
        }
    )

    return response

# ========================
# Metrics Endpoint
# ========================
@app.get("/metrics")
def metrics():
    """Expose Prometheus metrics"""
    return Response(generate_latest(), media_type="text/plain")

# ========================
# Application Routes
# ========================
class Account(BaseModel):
    name: str
    balance: float

@app.get("/")
def root():
    return {"message": "Cloud Banking API is running"}

@app.post("/accounts")
def create_account(account: Account):
    db.accounts.insert_one(account.dict())
    return {"status": "Account created", "account": account}

@app.get("/")
def read_root():
    return {"message": "Hello World"}