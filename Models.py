from pydantic import BaseModel, Field, field_validator,HttpUrl,ValidationError
from typing import Optional
from faker import Faker
from datetime import datetime

fake = Faker()

class Model(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl

class SupportModel(BaseModel):
    url: HttpUrl
    text: str

class ResponseModel(BaseModel):
    support: SupportModel
    data: Model

#####

class UserRequest(BaseModel):
    name: str
    job: str


class UserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime = Field(default_factory=datetime.now)

    @classmethod
    @field_validator('name', 'job', 'id', 'createdAt')
    def validate_fields(cls, value, field):
        if not value:
            raise ValidationError(f'Invalid value for {field.name}: must not be empty')
        return value

####
class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None

    @classmethod
    @field_validator('name', 'job')
    def validate_fields(cls, value, field):
        if value is not None and not isinstance(value, str):
            raise ValidationError(f'Invalid type for {field.name}: must be a string')
        if value == "":
            raise ValidationError(f'Invalid value for {field.name}: must not be empty')
        return value

class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: datetime = Field(default_factory=datetime.now)

####
