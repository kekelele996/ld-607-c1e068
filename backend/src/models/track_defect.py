from pydantic import BaseModel
class TrackDefect(BaseModel):
    id: int | float
    section_id: int | float
    defect_type: str
    km_marker: str
    severity: str
    discovered_at: str
    source: str
    status: str
    photo_url: str
