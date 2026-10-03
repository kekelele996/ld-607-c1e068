from pydantic import BaseModel
class ReviewRecord(BaseModel):
    id: int | float
    task_id: int | float
    reviewer_id: int | float
    review_result: str
    measured_value: str
    review_at: str
    next_action: str
