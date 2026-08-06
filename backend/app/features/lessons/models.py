from datetime import datetime, timezone
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.extensions.database import db
from app.features.courses import Course

class Lessons(db.Model):
    __tablename__="lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = relationship(foreign_key='courses.id')
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(String(5000), nullable=False)
    video_url: Mapped[str] = mapped_column(String(500), nullable=False)
    lesson_order: Mapped[int] = mapped_column(nullable=False)