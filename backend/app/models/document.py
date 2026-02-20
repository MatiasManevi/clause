from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    content_type: str
    file_size: int
    processing_status: str
    upload_date: datetime

    class Config:
        from_attributes = True
