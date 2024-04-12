from pydantic import BaseModel, Field
from typing import Optional


class TodoValidate(BaseModel):
    id: Optional[int] = None, Field(gt=0)
    title: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=30)
    priority: int = Field(min_length=1, gt=-1, lt=6)
    complete: bool

    class Config:
        json_schema_extra = {
            "example": {
                "id": 4,
                "title": "Example title",
                "description": "Example Description",
                "priority": 5,
                "complete": False,
            }
        }


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    role: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "username": "Example Username",
                "first_name": "Example First Name",
                "last_name": "Example Last Name",
                "hashed_password": "Example Password",
                "role": "Example Role",
            }
        }

class Token(BaseModel):
    access_token: str
    token_type: str
