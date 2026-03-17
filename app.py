from http.client import HTTPException

from fastapi  import FastAPI
from schemas import TaskSchema, TaskSchemaDB, ListTasksSchema, Message
from http import HTTPStatus

app = FastAPI()

tarefas = []

def buscar_tarefa_por_id(id: int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
        
    return None

@app.get("/tarefas/", response_model=ListTasksSchema)
def get_tarefas():
    return {"tarefas": tarefas}

@app.post("/tarefas/", response_model=TaskSchemaDB, status_code=HTTPStatus.CREATED)
def post_tarefas(tarefa : TaskSchema):
    tarefa_com_id = TaskSchemaDB(**tarefa.model_dump(), id=len(tarefas) + 1)
    tarefas.append(tarefa_com_id)

    return tarefa_com_id

@app.put("/tarefas/{id}", response_model=TaskSchemaDB)
def put_tarefas(id: int, tarefa: TaskSchema):
    tarefa_db = buscar_tarefa_por_id(id)
    if not tarefa_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail="Tarefa não encontrada")

    tarefa_com_id = TaskSchemaDB(**tarefa.model_dump(), id=id)
    tarefas[tarefas.index(tarefa_db)] = tarefa_com_id

    return tarefa_com_id

@app.delete("/tarefas/{id}", response_model=Message)
def delete_tarefas(id: int):
    tarefa_db = buscar_tarefa_por_id(id)

    if  not tarefa_db:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Tarefa não encontrada")
    
    tarefas.remove(tarefa_db)

    return {"mensagem": "Tarefa apagada"}
