from fastapi import Body, FastAPI

app = FastAPI()


class Books:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Books(
        1,
        "Computer Science with Gen AI like Pro",
        "Shiva Dey",
        "This book will guide you to excel in career with implementation of GenAI in various sectors of Computer Science and IT fields",
        4,
    ),
    Books(
        2,
        "Be Fast with FastAPI",
        "Shiva Dey",
        "Usage to latest tech with fastAPI to excel your bank-end services",
        3,
    ),
    Books(3, "Master endpoints", "Roby Guy", "Get the most out of endpoints", 3),
    Books(
        4,
        "Maths with Python numpy",
        "Carry Sutar",
        "Usage of equations and making time complexity to 1",
        4,
    ),
    Books(
        5,
        "A record of mortals journey to Immortality",
        "Wang Yu",
        "It's a frictional fantasy ",
        5,
    ),
    Books(
        6,
        "Library of heaven's path",
        "Heng Sao Tian Ya",
        "This a fantasy comedy and cultivation type novel",
        5,
    ),
]


@app.get("/books")
async def return_all_books():
    return BOOKS

@app.post('/create-book')
async def create_book(book_request = Body()):
    Books.append(book_request)