from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
from validate import TodoValidate

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all_todos(db: db_dependency):
    return db.query(models.Todos).all()


@app.get("/todo/{id}", status_code=status.HTTP_200_OK)
async def read_by_id(db: db_dependency, id: int = Path(gt=0)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == id).first()
    if todo_model is not None:
        return todo_model
    else:
        raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/add_todo", status_code=status.HTTP_201_CREATED)
async def create_todo(
    db: db_dependency,
    todo_validate: TodoValidate,
):
    todo_model = models.Todos(**todo_validate.model_dump())

    db.add(todo_model)
    db.commit()


@app.put("/update_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(
    db: db_dependency,
    todo_validate: TodoValidate,
    todo_id: int,
):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todos not found")
    else:
        todo_model.title = todo_validate.title
        todo_model.description = todo_validate.description
        todo_model.priority = todo_validate.priority
        todo_model.complete = todo_validate.complete

        db.add(models)
        db.commit()


@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_validate: TodoValidate, id: int):
    todo_model = db.query(models.Todos).filter(models.Todos.id == id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.query(models.Todos).filter(models.Todos.id == id).delete()
    db.commit()
