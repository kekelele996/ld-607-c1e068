from src.repositories.work_window_repository import WorkWindowRepository
class WorkWindowService:
    def __init__(self):
        self.repo = WorkWindowRepository()
    def list(self):
        return self.repo.find_all()
