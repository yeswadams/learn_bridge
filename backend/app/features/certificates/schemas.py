from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.certificates.models import Certificate

class CertificateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Certificate
        load_instance = True
        include_fk = True

    course = fields.Nested(
        "app.features.courses.schemas.CourseSchema",
        only=("id", "title")
    )
    user = fields.Nested(
        "app.features.auth.schemas.UserSchema",
        only=("id", "full_name")
    )
