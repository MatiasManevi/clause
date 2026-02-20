from fastapi import APIRouter, UploadFile, File, Depends, status
# from sqlalchemy.orm import Session
# from app.db.session import get_db
from app.schemas.document import DocumentResponse
from app.services.storage.factory import get_storage_service
from app.services.storage.service import StorageService
from app.services.document import DocumentService
from app.core.auth import get_current_user

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post(
    "/upload",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
async def upload_document(
    file: UploadFile = File(...),
    # db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    storage_service: StorageService = Depends(get_storage_service),
):
    service = DocumentService(storage_service)
    return await service.upload_document(file, current_user.id)
