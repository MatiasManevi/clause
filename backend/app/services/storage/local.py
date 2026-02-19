import uuid
import hashlib
from pathlib import Path
from fastapi import UploadFile
from typing import Tuple
from .base import StorageStrategy


class LocalStorageStrategy(StorageStrategy):

    def __init__(self, storage_dir: str = "storage"):
        self.storage_path = Path(storage_dir)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    async def save_file(self, file: UploadFile) -> Tuple[str, str]:
        file_id = uuid.uuid4()
        full_path = self.storage_path / f"{file_id}_{file.filename}"

        content = await file.read()
        checksum = hashlib.sha256(content).hexdigest()

        with full_path.open("wb") as buffer:
            buffer.write(content)

        return str(full_path), checksum
