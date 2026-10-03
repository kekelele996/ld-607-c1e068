from pydantic import BaseModel
class RectificationTask(BaseModel):
    id: int | float
    defect_id: int | float
    work_window_id: int | float
    crew_id: int | float
    method: str
    status: str
    started_at: str
    finished_at: str
