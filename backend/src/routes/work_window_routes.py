from fastapi import APIRouter
from src.controllers.work_window_controller import list_work_window
router = APIRouter(prefix="/api/work-window", tags=["WorkWindow"])
router.get("")(list_work_window)
