from abc import ABC, abstractmethod
from typing import Tuple
from fastapi import UploadFile


class StorageStrategy(ABC):
    @abstractmethod
    async def save_file(self, file: UploadFile) -> Tuple[str, str]:
        """
        Saves the file and returns:
        - storage_url (string)
        - checksum (sha256 string)
        """
        pass
