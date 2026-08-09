from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.categories.models import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        
    # Pluggable deep nesting without manual imports using absolute path strings
    courses = fields.List(
        fields.Nested("app.features.courses.schemas.CourseSchema", exclude=("category"))
    )