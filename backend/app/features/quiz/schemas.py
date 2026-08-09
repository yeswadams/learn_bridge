from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.quiz.models import Quiz

class QuizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quiz
        load_instance = True
        include_fk = True

class QuizCreateSchema(ma.Schema):
    """Validates incoming client requests bodies when the admin creates a quiz to a course"""
    title = fields.String(required=True, validate=lambda x: 0 < len(x) <= 255)
    passing_score = fields.Integer(required=True, validate=lambda x: 0 <= x <= 100)