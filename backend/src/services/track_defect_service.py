from src.repositories.track_defect_repository import TrackDefectRepository
class TrackDefectService:
    def __init__(self):
        self.repo = TrackDefectRepository()
    def list(self):
        return self.repo.find_all()
