from fastapi import APIRouter
from src.controllers.rectification_task_controller import list_rectification_task
router = APIRouter(prefix="/api/rectification-task", tags=["RectificationTask"])
router.get("")(list_rectification_task)
