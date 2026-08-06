from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.extensions.database import db

class Course(db.Model):
    __tablename__ = 'courses'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="course")
    price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    duration_mins: Mapped[int] = mapped_column(nullable=False)

    # Relationship
    courses = 
