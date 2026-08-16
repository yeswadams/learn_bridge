import enum
import uuid
from datetime import datetime, timezone
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, Integer, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.enrollments.models import Enrollment
    from app.features.certificates.models import Certificate
    from app.features.courses.models import Course

class UserRole(enum.Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"
    ADMINISTRATOR = "administrator"

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, native_enum=True, name="User_role"),
        default=UserRole.STUDENT,
        nullable=False
    )
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    profile_img: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships - Used String references to avoid runtime circular import
    enrollments: Mapped[List["Enrollment"]] = relationship(
        back_populates='user', 
        cascade='all, delete-orphan'
    )
    certificates: Mapped[List["Certificate"]] = relationship(
        back_populates='user', 
        cascade="all, delete-orphan"
    )
    courses_created: Mapped[List["Course"]] = relationship(
        back_populates="instructor"
    )