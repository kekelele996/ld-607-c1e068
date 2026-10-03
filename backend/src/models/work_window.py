from pydantic import BaseModel
class WorkWindow(BaseModel):
    id: int | float
    section_id: int | float
    window_date: str
    start_time: str
    end_time: str
    window_type: str
    approval_status: str
    dispatcher_note: str
