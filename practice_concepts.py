# from marshmallow import Schema, fields

# class UserSchema(Schema):
#     name = fields.String(required=True)
#     email = fields.Email(required=True)
    
# data = {
#     "name": "Shiva",
#     "email": "shiva@example.com"
# }

# result = UserSchema().load(data)

# print(result)

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    
data_kwargs = {
    'name': "Shiva",
    'email':"shiva@example.com"
}
user = User(**data_kwargs)
print(user)
print(user.model_dump())
