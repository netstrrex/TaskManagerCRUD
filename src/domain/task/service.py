from logging import getLogger
from uuid import UUID

from domain.task.exceptions import TaskNotFoundError
from domain.task.models import TaskModel
from domain.task.repositories.ABC import AbstractTaskRepository

logger = getLogger(__name__)


class TaskService:
    def __init__(self, repo: AbstractTaskRepository) -> None:
        self._repo = repo

    async def create_task(self, title: str, description: str) -> UUID:
        new_task_id = await self._repo.create_task(title, description)
        logger.info("Task with id - %s was created", str(new_task_id))
        return new_task_id

    async def get_task(self, uuid: UUID) -> TaskModel:
        try:
            task = await self._repo.get_task(uuid)
        except TaskNotFoundError as e:
            logger.info("Task with id - %s not found", str(uuid))
            raise e
        logger.info("Get task with id - %s", str(uuid))
        return task

    async def get_tasks(self) -> tuple[TaskModel, ...]:
        tasks = await self._repo.get_tasks()
        logger.info("Get all tasks")
        return tasks

    async def update_task(self, task: TaskModel) -> None:
        try:
            await self._repo.update_task(task)
        except TaskNotFoundError as e:
            logger.info("Task with id - %s not found", str(task.id))
            raise e
        logger.info("Task with id - %s was updated", str(task.id))

    async def delete_task(self, uuid: UUID) -> None:
        try:
            await self._repo.delete_task(uuid)
        except TaskNotFoundError as e:
            logger.info("Task with id - %s not found", str(uuid))
            raise e
        logger.info("Task with id - %s was deleted", str(uuid))
