from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/")
async def first_api():
    """
    The function `first_api` is an asynchronous Python function that returns a dictionary with a message
    "Hello Eric".
    :return: {"message": "Hello Saad"}
    """
    return {"message": "Hello Saad"}


@app.get("/books")
async def get_all_books():
    """
    This async function `get_books` is expected to return a variable `books`.
    :return: The function `get_books()` is returning the variable `books`.
    """
    return books


# Path Parameter
@app.get("/books/{title}")
async def get_books_by_title(title: str):
    """
    The function `get_books_by_title` searches for a book by its title in a case-insensitive manner.

    :param title: The function `get_books_by_title` is an asynchronous function that takes a `title`
    parameter as input. The function iterates over a collection of books and checks if the title of each
    book matches the input `title` parameter (case-insensitive comparison). If a match is found, the
    function
    :type title: str
    :return: the book with a title that matches the input title (case-insensitive comparison).
    """
    for book in books:
        if book.get("title").casefold() == title.casefold():
            return book


# Query Parameter
@app.get("/books/")
async def get_books_by_category(category: str):
    """
    The function `get_books_by_category` filters a list of books by a specified category and returns the
    filtered list.

    :param category: The function `get_books_by_category` is an asynchronous function that takes a
    category as input and returns a list of books that belong to that category. The function iterates
    through a list of books and checks if the category of each book matches the input category
    (case-insensitive comparison). If a match
    :type category: str
    :return: A list of books that belong to the specified category is being returned.
    """
    books_to_return = []
    for book in books:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Path and Query Parameter together
@app.get("/books/{author}/")
async def get_books_by_author_and_category(author: str, category: str):
    books_to_return = []
    for book in books:
        if (
            book.get("author").casefold() == author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)
    return books_to_return


# -----------------POST--------------------------#
@app.post("/books/create_book")
async def create_book(book=Body()):
    """
    The function `create_book` asynchronously appends a book object to a list of books.

    :param book: The `create_book` function is an asynchronous function that takes a single parameter
    `book`. The function appends the `book` parameter to a list named `books`
    """
    books.append(book)


# -----------------PUT---------------------------#
@app.put("/books/update_book")
async def update_book(book=Body()):
    """
    The function `update_book` updates a book in a list of books based on the title provided.

    :param book: The `update_book` function is an asynchronous function that takes a `book` object as a
    parameter. The function iterates through a list of books and checks if the title of any book in the
    list matches the title of the `book` parameter (case-insensitive comparison). If a match is
    """
    for i in range(len(books)):
        if books[i].get("title").casefold() == book.get("title").casefold():
            books[i] = book


# -----------------DELETE---------------------------#
@app.delete("/books/delete_books/{book}")
async def delete_books(book: str):
    """
    The function `delete_books` deletes a book from a list of books based on its title.
    
    :param book: The `delete_books` function is an asynchronous function that takes a book title as a
    parameter. It iterates through a list of books and deletes the book with a matching title
    (case-insensitive comparison). If a book with the specified title is found, it is removed from the
    `books` list
    :type book: str
    """
    for i in range(len(books)):
        if books[i].get("title").casefold() == book.casefold():
            books.pop(book)
            break
