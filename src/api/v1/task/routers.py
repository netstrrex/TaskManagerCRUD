from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Depends

from api.v1.schemas import OkResponse
from api.v1.task.dependencies import get_task_service
from domain.task.models import TaskModel
from domain.task.service import TaskService

router = APIRouter(prefix="/task", tags=["Task Management"])


@router.post("/")
async def new_task(
    title: str,
    description: str,
    task_service: TaskService = Depends(get_task_service),
) -> UUID:
    new_task_uuid = await task_service.create_task(title, description)
    return new_task_uuid


@router.get(
    "/",
    response_model=TaskModel,
    responses={404: {"description": "Task not found"}},
)
async def get_task(
    uuid: UUID, task_service: TaskService = Depends(get_task_service)
) -> TaskModel:
    task = await task_service.get_task(uuid)
    return task


@router.get("/all", response_model=tuple[TaskModel, ...])
async def get_tasks(
    task_service: TaskService = Depends(get_task_service),
) -> tuple[TaskModel, ...]:
    tasks = await task_service.get_tasks()
    return tasks


@router.put(
    "/",
    response_model=OkResponse,
    responses={404: {"description": "Task not found"}},
)
async def update_task(
    task: TaskModel, task_service: TaskService = Depends(get_task_service)
) -> OkResponse:
    await task_service.update_task(task)
    return OkResponse(ok=True)


@router.delete(
    "/",
    response_model=OkResponse,
    responses={404: {"description": "Task not found"}},
)
async def delete_task(
    uuid: UUID, task_service: TaskService = Depends(get_task_service)
) -> OkResponse:
    await task_service.delete_task(uuid)
    return OkResponse(ok=True)
