import uuid
from typing import Optional, TYPE_CHECKING, List
from sqlalchemy import (
    String, 
    Integer, 
    ForeignKey, 
    Text, 
    UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.courses.models import Course
    from app.features.progress.models import Progress
    

class Lesson(db.Model):
    __tablename__="lessons"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    course_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('courses.id', ondelete="CASCADE"), 
        nullable=False
    )
    title: Mapped[str] = mapped_column(
        String(200), 
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        Text, 
        nullable=False
    )
    video_url: Mapped[Optional[str]] = mapped_column(
        String(500), 
        nullable=True
    )
    lesson_order: Mapped[int] = mapped_column(
        Integer, 
        nullable=False
    )

    # Relationships
    course: Mapped["Course"] = relationship(
        back_populates="lessons"
    )
    progress_records: Mapped[List["Progress"]] = relationship(
        back_populates="lesson", 
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint(
            "course_id", 
            "lesson_order", 
            name="uq_course_lesson_order"
        ),
    )