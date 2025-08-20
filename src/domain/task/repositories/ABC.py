from abc import ABC, abstractmethod
from uuid import UUID

from core.database import AbstractDatabase
from domain.task.models import TaskModel


class AbstractTaskRepository(ABC):
    def __init__(self, database: AbstractDatabase) -> None:
        self._database = database

    @abstractmethod
    async def create_task(self, title: str, description: str) -> UUID:
        """
        Create task record asynchronously.

        Args:
            title (str): Task title.
            description (str): Task description.

        Returns:
            UUID: id of task record.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_task(self, uuid: UUID) -> TaskModel:
        """
        Get task record asynchronously by id.

        Args:
            uuid (UUID): id of task.

        Returns:
            TaskModel: pydantic dataclass.

        Raises:
            TaskNotFoundError: If task with this uuid does not exist.
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_tasks(self) -> tuple[TaskModel, ...]:
        """
        Get all tasks records asynchronously.

        Returns:
            tuple[TaskModel]: tuple of pydantic dataclasses.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError

    @abstractmethod
    async def update_task(self, task: TaskModel) -> None:
        """
        Update task record asynchronously.

        Args:
            task (TaskModel): TaskModel pydantic dataclass.

        Raises:
            TaskNotFoundError: If task with this uuid does not exist.
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete_task(self, uuid: UUID) -> None:
        """
        Delete task record asynchronously by id.

        Args:
            uuid (UUID): TaskModel pydantic dataclass.

        Raises:
            TaskNotFoundError: If task with this uuid does not exist.
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError
