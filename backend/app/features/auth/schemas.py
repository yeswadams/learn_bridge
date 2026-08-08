from marshmallow import fields
from marshmallow_enum import EnumField
from app.extensions.marshmallow import ma
from app.features.auth.models import User, UserRole

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        include_relationships = False # Keep auth data leans; load relationships on demand
        exclude = ("password_hash",) # Hard guard: Never expose pasword hashes over the wire

    role = EnumField(UserRole, by_value=True)

class UserRegisterSchema(ma.Schema):
    """Explicit validation schema for input client payloads during registration"""
    full_name = fields.String(required=True, validate= lambda x: len(x) >= 2)
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=lambda x: len(x) >= 8)
    age = fields.Integer(required=True, validate=lambda x: x > 0)

