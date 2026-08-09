from marshmallow import fields
from app.extensions.marshmallow import ma
from app.features.enrollments.models import Enrollment, ProgressStatus

class EnrollmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Enrollment
        load_instance = True
        include_fk = True

    status = fields.Enum(ProgressStatus, by_value=True)
    
    course = ma.Nested(
        "app.features.courses.schemas.CourseSchema", 
        only=("id", "title", "duration_mins")
    )
    user = ma.Nested(
        "app.features.auth.schemas.UserSchema",  # Fixed typo here
        only=("id", "full_name", "email")
    )
