from app.extensions.marshmallow import ma
from marshmallow import fields
from app.features.progress.models import Progress
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.features.lessons.schemas import LessonSchema

class ProgressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Progress
        load_instance = True
        include_fk = True

    # Flatten the dynamic response payload to prevent massive object trees over the clients API Gateway
    lesson = fields.Nested(LessonSchema, only=("id", "title", "lesson_order"))

class ProgressToggleSchema(ma.Schema):
    """Validates input payload coming from the client to mark a specific lesson as complete"""
    is_completed = fields.Boolean(required=True)