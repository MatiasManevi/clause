from app.core.config import config
from .local import LocalStorageStrategy
from .s3 import S3StorageStrategy
from .service import StorageService


def get_storage_service() -> StorageService:

    if config.storage_provider == "s3":
        strategy = S3StorageStrategy(
            bucket_name=config.s3_bucket,
            region=config.s3_region
        )
    else:
        strategy = LocalStorageStrategy()

    return StorageService(strategy)
