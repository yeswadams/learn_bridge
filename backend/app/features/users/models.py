from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions.database import db
from sqlalchemy import String, Integer, DateTime
from typing import Optional


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) 
    full_name: Mapped[str] = mapped_column(
        String(120), 
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(255), 
        unique=True, 
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    role: Mapped[str] = mapped_column(
        String(50), 
        default="student", 
        nullable=False
    )
    age: Mapped[int] = mapped_column(
        Integer, 
        nullable=False
    )
    profile_img: Mapped[Optional[str]] = mapped_column(
        String(500), 
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )

    #Relationships:
    enrollements: Mapped[list["Enrollment"]] = relationship(back_populates='')
    certificates: Mapped[list["Certificate"]] = relationship(back_populates='')
    courses: Mapped[list["Course"]] = relationship(back_populates='')