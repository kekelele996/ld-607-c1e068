from fastapi import APIRouter
from src.controllers.track_section_controller import list_track_section
router = APIRouter(prefix="/api/track-section", tags=["TrackSection"])
router.get("")(list_track_section)
