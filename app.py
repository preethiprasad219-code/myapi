from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(task: str):
    todos.append(task)
    return {"message": "added", "todos": todos}

@app.delete("/todos")
def delete_todo(task: str):
    todos.remove(task)
    return {"message": "deleted", "todos": todos}