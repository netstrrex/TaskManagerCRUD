from fastapi import APIRouter

from api.v1.task.routers import router as task_router

router = APIRouter(prefix="/v1")
router.include_router(task_router)

__all__ = ["router"]
