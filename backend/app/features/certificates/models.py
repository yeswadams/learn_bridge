import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, UUID, ForeignKey, UniqueConstraint
from typing import Optional, TYPE_CHECKING
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.auth.models import User
    from app.features.courses.models import Course

class Certificate(db.Model):
    __tablename__ = "certificates"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        dafault=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # We reference the targeted PK cleanly without needing a back-populating the course ref in Course
    course_id: Mapped[uuid.UUID] = mapped_column(
        distinct_target_key="Course.id"
    )

    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="unique_user_course_certificate")
    )
