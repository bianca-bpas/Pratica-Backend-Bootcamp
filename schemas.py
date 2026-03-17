from pydantic import BaseModel

class TaskSchema(BaseModel):
    nome: str
    concluido: bool

class TaskSchemaDB(TaskSchema):
    id: int

class ListTasksSchema(BaseModel):
    tarefas: list[TaskSchemaDB]

class Message(BaseModel):
    mensagem: str