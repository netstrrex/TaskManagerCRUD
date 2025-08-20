from core.exception import AppException


class TaskNotFoundError(AppException):
    status_code = 404
    message = "Task not found"
