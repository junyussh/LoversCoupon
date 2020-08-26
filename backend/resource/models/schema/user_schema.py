from common.ma import ma
from marshmallow import validate

# {
#     "Id": id,
#     "password": string
#     "Name": string,
#     "Sexual": Int,
#     "Birthday": "1900-01-01",
#     "Phone": 0912345678,
#     "email": "test@example.org"
# }
class UserSchema(ma.Schema):
    id = ma.Int()
    password = ma.Str(required=True)
    name = ma.Str(required=True, allow_none=False, validate=[
                      validate.Length(min=6, max=36)],)
    sex = ma.Int()
    #ISO 8601 standard
    birth = ma.Str()
    phone = ma.Str(required=True)
    email = ma.Email(required=True)
