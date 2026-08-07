import uuid
import enum
from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey, Enum, DateTime, UniqueConstraint, CheckConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.auth.models import User
    from app.features.courses.models import Course

class ProgressStatus(enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Enrollment(db.Model):
    __tablename__="enrollments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[ProgressStatus] = mapped_column(
        Enum(ProgressStatus, native_enum=True, name="progress_status"), 
        default=ProgressStatus.NOT_STARTED,
        nullable=False
    )

    progress_percentage: Mapped[int] = mapped_column(
        Integer, 
        default=0, 
        nullable=False
    )
    enrolled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    ) 

    # Relationships
    user: Mapped["User"] = relationship(back_populates="enrollments")
    course: Mapped["Course"] = relationship(back_populates="enrollments")

    __table_args__ = (
        UniqueConstraint(
            "user_id", "program_id", 
            name="unique_user_course_enrollment"
        ),
        CheckConstraint(
            "progress_percentage BETWEEN 0 AND 100", name="check_progress_percentage_bounds"
        ),
        Index("idx_enrollments_lookup", "user_id", "status")
    )

