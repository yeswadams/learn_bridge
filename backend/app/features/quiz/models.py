import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, CheckConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.features.courses.models import Course

class Quiz(db.Model):
    __tablename__ = "quizzes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    course_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("courses.id"), 
        ondelete=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    passing_score: Mapped[int] = mapped_column(
        Integer, 
        nullable=False, 
        default=70
    )

    # Relationships
    course: Mapped["Course"] = relationship(back_populates="quizzes")

    __table_args__ = (
        CheckConstraint(
            "passing_score BETWEEN 0 AND 100", name="check_quiz_passing_score_bounds"
        )
    )

