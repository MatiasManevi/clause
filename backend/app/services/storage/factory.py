from app.core.config import STORAGE_PROVIDER, S3_BUCKET, S3_REGION
from .local import LocalStorageStrategy
from .s3 import S3StorageStrategy
from .service import StorageService


def get_storage_service() -> StorageService:

    if STORAGE_PROVIDER == "s3":
        strategy = S3StorageStrategy(
            bucket_name=S3_BUCKET,
            region=S3_REGION
        )
    else:
        strategy = LocalStorageStrategy()

    return StorageService(strategy)
