import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, Boolean,  UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.features.auth.models import User
    from app.features.lessons.models import Lesson

class Progress(db.Model):
    """Tracks atomic completion status of individual lesson per student"""
    __tablename__ = "progress"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False
    )
    lesson_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("lessons.id", ondelete="CASCADE"), 
        nullable=False
    )
    is_completed: Mapped[bool] = mapped_column(
        Boolean, 
        default=False, 
        nullable=False
    )
    completed_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="progress_records")
    lesson: Mapped["Lesson"] = relationship(back_populates="progress_records")

    __table_args__ = (
        UniqueConstraint(
            "user_id", 
            "lesson_id", 
            name="unique_user_lesson_progress"
        )
    )

