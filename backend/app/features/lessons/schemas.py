from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.lessons.models import Lesson

class LessonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lesson
        load_instance = True
        include_fk = True

class LessonCreateSchema(ma.Schema):
    """Validate data coming from admin client when appending lessons."""
    title = fields.String(required=True, validate=lambda x: 0 < len(x) <= 200)
    content = fields.String(required=True)
    video_url = fields.URL(allow_none=True)
    lesson_order = fields.Integer(required=True, validate=lambda x: x>= 1)