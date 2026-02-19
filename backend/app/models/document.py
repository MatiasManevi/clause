# import uuid
# from datetime import datetime
# from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
# from app.db.base import Base


# class Document(Base):
#     __tablename__ = "documents"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

#     filename = Column(String, nullable=False)
#     content_type = Column(String, nullable=False)
#     file_size = Column(Integer, nullable=False)
#     storage_url = Column(String, nullable=False)

#     checksum = Column(String, nullable=False)

#     processing_status = Column(
#         String,
#         nullable=False,
#         default="pending"
#     )

#     text_extracted = Column(Text, nullable=True)

#     upload_date = Column(DateTime, default=datetime.utcnow, nullable=False)

#     user = relationship("User", back_populates="documents")
