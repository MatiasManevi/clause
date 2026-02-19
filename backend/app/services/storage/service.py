from fastapi import UploadFile
from typing import Tuple
from .base import StorageStrategy


class StorageService:

    def __init__(self, strategy: StorageStrategy):
        self._strategy = strategy

    async def save_file(self, file: UploadFile) -> Tuple[str, str]:
        return await self._strategy.save_file(file)
