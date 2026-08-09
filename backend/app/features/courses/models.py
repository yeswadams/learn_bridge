import uuid
from decimal import Decimal 
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Numeric, Text, Text, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.extensions.database import db

if TYPE_CHECKING:
    from app.features.auth.models import User
    from app.features.categories.models import Category
    from app.features.lessons.models import Lesson
    from app.features.enrollments.models import Enrollment
    from app.features.quiz.models import Quiz

class Course(db.Model):
    __tablename__ = "course"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(
        String(255), 
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        Text, 
        nullable=False
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), 
        nullable=False, 
        default=0.00
    )
    duration_mins: Mapped[int] = mapped_column(
        nullable=False
    )
    category_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("category.id", ondelete="SET NULL")
    )
    instructor_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )

    # Relationship
    category: Mapped[Optional["Category"]] = relationship(back_populates="courses")
    instructor: Mapped["User"] = relationship(back_populates="courses_created")
    lessons: Mapped[List["Lesson"]] = relationship(
        back_populates="course", 
        order_by="Lesson.lesson_order", 
        cascade="all, delete-orphan"
    )
    enrollments: Mapped[List["Enrollment"]] = relationship(
        back_populates="course", 
        cascade="all, delete-orphan"
    )
    quizzes: Mapped[List["Quiz"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )

    __table_args__ = (
        CheckConstraint("duration_mins >= 0", name="check_course_duration_postive"),
        CheckConstraint("price >= 0", name="check_course_price_non_negative"),
    )

    def __repr__(self):
        return f"<Course name: {self.title} by {self.instructor}>"
