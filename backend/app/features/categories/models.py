from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.extensions.database import db
from sqlalchemy import String
from app.features.courses import Course


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    courses: Mapped[list["Course"]] = relationship(
        back_populates="category"
    )