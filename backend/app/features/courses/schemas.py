from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.courses.models import Course

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        load_instance = True
        include_fk = True

    # Pure string paths completely eliminate circular imports at runtime
    category = fields.Nested("app.features.categories.schemas.CategorySchema", exclude=["courses"])
    instructor = fields.Nested("app.features.auth.schemas.UserSchema")
    
    # Safely lazy-evaluate the Lesson schema sequence
    lessons = fields.List(
        fields.Nested("app.features.lessons.schemas.LessonSchema", exclude=["course_id"])
    )
    
    # Seamlessly incorporate the quiz tracking slice
    quizzes = fields.List(
        fields.Nested("app.features.quiz.schemas.QuizSchema", exclude=["course_id"])
    )

class CourseCreateSchema(ma.Schema):
    """Strictly enforces required fields for adding a new program."""
    title = fields.String(required=True, validate=lambda x: len(x) >= 3)
    description = fields.String(required=True)
    price = fields.Decimal(required=True, places=2)
    duration_mins = fields.Integer(required=True, validate=lambda x: x > 0)
    category_id = fields.UUID(required=True)