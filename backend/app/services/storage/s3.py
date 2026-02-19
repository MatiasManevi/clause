import uuid
import hashlib
import boto3
from fastapi import UploadFile
from typing import Tuple
from .base import StorageStrategy


class S3StorageStrategy(StorageStrategy):

    def __init__(self, bucket_name: str, region: str = "us-east-1"):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client("s3", region_name=region)

    async def save_file(self, file: UploadFile) -> Tuple[str, str]:
        file_id = uuid.uuid4()
        key = f"{file_id}_{file.filename}"

        content = await file.read()
        checksum = hashlib.sha256(content).hexdigest()

        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=content,
            ContentType=file.content_type
        )

        storage_url = f"s3://{self.bucket_name}/{key}"

        return storage_url, checksum
