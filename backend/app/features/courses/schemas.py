from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.courses.models import Course
from app.features.lessons.schemas import LessonSchema

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        load_instance = True
        include_fk = True

    # Explicitly pull down cleanly serilized nested schemas
    category = fields.Nested("app.features.categories.schemas.CategorySchema", exclude=("courses", ))
    instructor = fields.Nested("app.features.auth.schemas.UserSchema")

    # Leverage the database-level `order_by` sequence configured earlier
    lessons = fields.List(
        fields.Nested(LessonSchema, exclude=("course_id", ))
    )

class CourseCreateSchema(ma.Schema):
    """Strictly enforces required fields for adding a new program"""
    title = fields.String(required=True, validate=lambda x: len(x) >= 3)
    description = fields.String(required=True)
    price = fields.Decimal(required=True, places=2)
    duration_mins = fields.Integer(required=True, validate=lambda x: x > 0)
    category_id = fields.UUID(required=True)