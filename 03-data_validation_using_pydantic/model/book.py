from typing import Optional

"""
This Python class represents a Book object with attributes such as id, title, description, and rating.
"""


class Book:
    id: int
    title: str
    description: str
    rating: int
    published_date: Optional[int] = None

    def __init__(self, id, title, description, rating, published_date):
        self.id = id
        self.title = title
        self.description = description
        self.rating = rating
        self.published_date = published_date
