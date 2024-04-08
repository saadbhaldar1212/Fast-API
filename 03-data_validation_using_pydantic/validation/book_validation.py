from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


# This class defines a BookValidation model with attributes for id, title, description, and rating.
class BookValidation(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    description: str = Field(min_length=1, max_length=20)
    rating: int = Field(gt=-1, lt=6)
    published_date: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Title from json_schema_extra",
                "description": "Description from json_schema_extra",
                "rating": 4,
                "published_date": 2024,
            }
        }
