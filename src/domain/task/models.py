from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class TaskStatus(str, Enum):
    created = "created"
    in_progress = "in_progress"
    done = "done"


class TaskModel(BaseModel):
    id: UUID
    title: str
    description: str
    status: TaskStatus
