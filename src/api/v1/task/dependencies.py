from typing import cast

from fastapi.params import Depends

from api.v1.dependencies import get_database
from domain.task.repositories.repository import TaskRepository
from domain.task.service import TaskService
from infrastructure.database.postgres import PostgresDatabase

task_service: TaskService | None = None


def get_task_service(
    database: PostgresDatabase = Depends(get_database),
) -> TaskService:
    global task_service
    if task_service is None:
        task_repository = TaskRepository(database)
        task_service = TaskService(task_repository)
    return cast(TaskService, task_service)
