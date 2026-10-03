from fastapi import APIRouter
from src.controllers.review_record_controller import list_review_record
router = APIRouter(prefix="/api/review-record", tags=["ReviewRecord"])
router.get("")(list_review_record)
