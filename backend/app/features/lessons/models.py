import uuid
from datetime import datetime, timezone
from sqlalchemy import String, Integer, ForeignKey, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.courses.models import Course

class Lesson(db.Model):
    __tablename__="lessons"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'), ondelete="CASCADE", nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    video_url: Mapped[str] = mapped_column(String(500), nullable=False)
    lesson_order: Mapped[int] = mapped_column(Integer, nullable=False)

    course: Mapped["Course"] = relationship(
        "CourseModel",
        back_populates="lessons"
    )

    __table_args__ = (
        UniqueConstraint("course_id", "lesson_order", name="uq_course_lesson_order")
    )