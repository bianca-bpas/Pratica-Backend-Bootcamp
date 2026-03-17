from typing import List
from pydantic import BaseModel

class TaskSchema(BaseModel):
    nome: str
    concluido: bool

class TaskSchemaDB(TaskSchema):
    id: int

class ListTasksSchema(BaseModel):
    tarefas: List[TaskSchemaDB]
