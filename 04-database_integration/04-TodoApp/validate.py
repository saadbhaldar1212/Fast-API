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
