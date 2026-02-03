from fastapi import FastAPI, HTTPException
import uvicorn,http
from pydantic import BaseModel
from pydantic.v1.fields import is_finalvar_with_default_val

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "psychology of money",
        "author": "jack.j",
    },
    {
        "id": 2,
        "title": "Backend guide",
        "author": "Micheal.M",
    },
]


@app.get(
    "/books",
    tags=["books"],
    summary="get all books"
)
def read_books():
    return books


@app.get("/books/{book_id}",
         tags=["books"],
         summary="get specific book")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


class NewBook(BaseModel):
    title: str
    author: str


@app.post("/books", tags=["books"])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "book added"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



