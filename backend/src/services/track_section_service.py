from src.repositories.track_section_repository import TrackSectionRepository
class TrackSectionService:
    def __init__(self):
        self.repo = TrackSectionRepository()
    def list(self):
        return self.repo.find_all()
