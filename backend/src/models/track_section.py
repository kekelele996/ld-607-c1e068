from pydantic import BaseModel
class TrackSection(BaseModel):
    id: int | float
    line_name: str
    start_km: str
    end_km: str
    direction: str
    speed_limit: str
    responsible_team_id: int | float
    risk_level: str
