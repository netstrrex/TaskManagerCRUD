from uuid import UUID

from core.database import AbstractDatabase
from domain.task.exceptions import TaskNotFoundError
from domain.task.models import TaskModel
from domain.task.repositories.ABC import AbstractTaskRepository


class TaskRepository(AbstractTaskRepository):
    def __init__(self, database: AbstractDatabase):
        super().__init__(database)

    async def create_task(self, title: str, description: str) -> UUID:
        res = await self._database.fetch(
            """INSERT INTO tasks(title, description) VALUES ($1, $2) RETURNING id""",
            title,
            description,
        )
        return res[0]["id"]

    async def get_task(self, uuid: UUID) -> TaskModel:
        res = await self._database.fetch("""SELECT * FROM tasks WHERE id = $1""", uuid)
        if not res:
            raise TaskNotFoundError
        return TaskModel(
            id=res[0]["id"],
            title=res[0]["title"],
            description=res[0]["description"],
            status=res[0]["status"],
        )

    async def get_tasks(self) -> tuple[TaskModel, ...]:
        res = await self._database.fetch("""SELECT * FROM tasks""")
        return tuple(
            TaskModel(
                id=i["id"],
                title=i["title"],
                description=i["description"],
                status=i["status"],
            )
            for i in res
        )

    async def update_task(self, task: TaskModel) -> None:
        res = await self._database.fetch(
            """UPDATE tasks SET title = $1, description = $2,
             status = $3 WHERE id = $4 RETURNING id""",
            task.title,
            task.description,
            task.status,
            task.id,
        )
        if not res:
            raise TaskNotFoundError

    async def delete_task(self, uuid: UUID) -> None:
        res = await self._database.fetch(
            """DELETE FROM tasks WHERE id = $1 RETURNING id""", uuid
        )
        if not res:
            raise TaskNotFoundError
