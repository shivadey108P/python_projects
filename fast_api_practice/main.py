from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {"todo_id": 1, "todo_name": "Sports", "todo_description": "Go to the gym"},
    {
        "todo_id": 2,
        "todo_name": "Read",
        "todo_description": "Read 10 pages of value added books",
    },
    {"todo_id": 3, "todo_name": "Shop", "todo_description": "Go shopping"},
    {"todo_id": 4, "todo_name": "Study", "todo_description": "Study daily for 2 hrs"},
    {"todo_id": 5, "todo_name": "Meditate", "todo_description": "Meditate for 20 mins"},
]


@api.get("/doc")
def index():
    return {"name": "Shiva Dey"}


@api.get("/todo/{todo_id:int}")
def get_todo(todo_id):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return {"results": todo}


@api.get("/todos")
def get_all_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
