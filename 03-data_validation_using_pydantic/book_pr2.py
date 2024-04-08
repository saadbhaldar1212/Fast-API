from model.book import Book
from validation.book_validation import BookValidation
from fastapi import FastAPI, Path, Query

# This class defines a BookValidation model with attributes for id, title, description, and rating.

app = FastAPI()

Books = [
    Book(1, "Java", "Java 8", 5, 2023),
    Book(2, "Python", "Python 3.12", 4, 2024),
    Book(3, "C++", "A great book", 3, 2020),
    Book(4, "C#", "Game Development", 2, 2019),
    Book(5, "HTML", "Web Development", 2, 2019),
]


def increment_id(book: Book):
    if len(Books) > 0:
        book.id = Books[-1].id + 1
    else:
        book.id = 1
    return book


@app.get("/")
async def get_all_books():
    """
    This async function returns all books.
    :return: the variable `Books`.
    """
    return Books


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int = Path(gt=0, lt=3)):
    """
    This async function searches for a book in a collection by its ID and returns the book if found.

    :param book_id: The `book_id` parameter in the `get_book_by_id` function is expected to be an
    instance of the `BookValidation` class. This parameter is used to search for a book in the `Books`
    list by comparing the `id` attribute of each book with the provided `book_id
    :type book_id: BookValidation
    :return: The function `find_book_by_id` is returning the book object that matches the provided
    `book_id`.
    """
    for book in Books:
        if book.id == book_id:
            return book


@app.get("/books/")
async def get_book_by_ratings(rating: int = Query(gt=-1)):
    """
    This function retrieves books with a specific rating from a list of books.

    :param rating: The `rating` parameter in the `get_book_by_ratings` function is of type
    `BookValidation`. It is used to filter and retrieve books that match the specified rating. The
    function iterates through a list of books (`Books`) and returns a list of books that have the same
    rating as the
    :type rating: BookValidation
    :return: A list of books that have the specified rating.
    """
    rated_books = []
    for book in Books:
        if book.rating == rating:
            rated_books.append(book)
    return rated_books


@app.get("/books/")
async def get_books_by_published_date(date: int):
    books = []
    for book in Books:
        if book.published_date == date:
            books.append(book)
    return books


# POST - without Data Validation
'''
@app.post("/create_books")
async def create_book(book=Body()):
    """
    The function `create_book` asynchronously appends a book to a list called `Books`.

    :param book: The `create_book` function is an asynchronous function that takes a single parameter
    `book`. The function appends the `book` parameter to a list called `Books`
    """
    Books.append(book)
'''


# POST - with Data Validation
@app.post("/crete_book")
async def create_book(validate: BookValidation):
    """
    This Python async function creates a new book object using a specified validation class and appends
    it to a list of books.

    :param validate: The `validate` parameter in the `create_book` function is an instance of the
    `BookValidation` class. It is used to validate the data before creating a new `Book` object. The
    `model_dump()` method is called on the `validate` object to extract the validated data that will
    """
    book = Book(**validate.model_dump())
    Books.append(book)


@app.post("/crete_book_with_autoincrement_id")
async def create_book_with_autoincrement_id(validate: BookValidation):
    """
    This Python function creates a new book instance with an auto-incremented ID.

    :param validate: The `validate` parameter is an instance of the `BookValidation` class, which is
    used to validate the data for creating a new book entry. It likely contains methods to check if the
    data meets certain criteria or constraints before creating the book object
    :type validate: BookValidation
    """
    book = Book(**validate.model_dump())
    Books.append(increment_id(book))


@app.put("/books/")
async def update_book(book: BookValidation):
    """
    This Python function updates a book in a list of books based on the book's ID.

    :param book: The `update_book` function is an asynchronous function that takes a parameter `book` of
    type `BookValidation`. The function iterates through a list of books (`Books`) and checks if the
    `id` of any book in the list matches the `id` of the `book` parameter
    :type book: BookValidation
    """
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """
    This function deletes a book from a list of books based on the provided book_id.

    :param book_id: The `book_id` parameter in the code snippet represents the unique identifier of the
    book that is being targeted for deletion. This identifier is used to locate the specific book within
    the `Books` list and remove it from the list once found
    :type book_id: int
    """
    for i in range(len(Books)):
        if Books[i].id == book_id:
            Books.pop(i)
            break
