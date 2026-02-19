import os

STORAGE_PROVIDER = os.getenv("STORAGE_PROVIDER", "local")
S3_BUCKET = os.getenv("S3_BUCKET", "")
S3_REGION = os.getenv("S3_REGION", "us-east-1")
DATABASE_URL = os.getenv("DATABASE_URL")
