# from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException, status
from datetime import datetime
# from app.models.document import Document
from app.models.document import DocumentResponse
from app.services.storage.service import StorageService

ALLOWED_TYPES = {
    "application/pdf",
    "text/plain",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB


class DocumentService:

    def __init__(self, storage_service: StorageService):
        # self.db = db
        self.storage_service = storage_service

    async def upload_document(self, file: UploadFile, user_id):
        # Validate content type
        if file.content_type not in ALLOWED_TYPES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported file type"
            )

        # Read once to validate size
        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File too large"
            )

        # Reset pointer
        file.file.seek(0)

        try:
            storage_path, checksum = await self.storage_service.save_file(file)

            # document = Document(
            #     user_id=user_id,
            #     filename=file.filename,
            #     content_type=file.content_type,
            #     file_size=len(content),
            #     storage_url=storage_path,
            #     checksum=checksum,
            #     processing_status="pending",
            #     upload_date=datetime.utcnow(),
            # )

            # self.db.add(document)
            # self.db.commit()
            # self.db.refresh(document)


            return DocumentResponse(
                id="123e4567-e89b-12d3-a456-426614174000",
                filename=file.filename,
                content_type=file.content_type,
                file_size=len(content),
                processing_status="pending",
                upload_date=datetime.utcnow()
            )

        except Exception:
            # self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to upload document"
            )
