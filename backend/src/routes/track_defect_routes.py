from fastapi import APIRouter
from src.controllers.track_defect_controller import list_track_defect
router = APIRouter(prefix="/api/track-defect", tags=["TrackDefect"])
router.get("")(list_track_defect)
