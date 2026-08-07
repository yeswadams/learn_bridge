import uuid
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.extensions.database import db
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from typing import  TYPE_CHECKING

if TYPE_CHECKING:
    from app.features.courses.models import Course


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    slug: Mapped[str] = mapped_column(
        String(100), 
        unique=True,
        nullable=False
    )

    # Relationship
    courses: Mapped[list["Course"]] = relationship(
        back_populates="category"
    )