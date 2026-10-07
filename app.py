from fastapi import FastAPI
from database import SessionLocal, Todo

app = FastAPI()


@app.get("/todos")
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()

    return todos


@app.post("/todos")
def add_todo(task: str):
    db = SessionLocal()

    new_todo = Todo(task=task)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    db.close()

    return {"message": "added", "todo": new_todo}


@app.delete("/todos")
def delete_todo(task: str):
    db = SessionLocal()

    todo = db.query(Todo).filter(Todo.task == task).first()

    if todo:
        db.delete(todo)
        db.commit()
        db.close()
        return {"message": "deleted"}

    db.close()
    return {"message": "Todo not found"}