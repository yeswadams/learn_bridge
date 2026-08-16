import uuid
from typing import TYPE_CHECKING
from datetime import datetime, timezone
from sqlalchemy import (
    DateTime,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.auth.models import User
    from app.features.courses.models import Course

class Certificate(db.Model):
    __tablename__ = "certificates"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # We reference the targeted PK cleanly without needing a back-populating the course ref in Course
    course_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("courses.id", ondelete="CASCADE"),
        nullable=False
    )

    issued_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # Relationships
    user: Mapped["User"] = relationship(
        back_populates="certificates"
    )

    course: Mapped["Course"] = relationship(
        back_populates="certificates"
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "course_id",
            name="unique_user_course_certificate"
        ),
    )
