from fastapi  import FastAPI
from schemas import *
from http import HTTPStatus

app = FastAPI()

tarefas = []

@app.get("/tarefas")
def get_tarefas(response_model=ListTasksSchema, status_code=HTTPStatus.OK):
    return tarefas

@app.post("/tarefas", response_model=TaskSchema, status_code=HTTPStatus.CREATED)
def post_tarefas(tarefa : TaskSchema):
    tarefas.append(tarefa)

    return tarefa

@app.put("/tarefas")
def put_tarefas(tarefa: TaskSchema):
    tarefas[tarefa]
