from src.repositories.rectification_task_repository import RectificationTaskRepository
class RectificationTaskService:
    def __init__(self):
        self.repo = RectificationTaskRepository()
    def list(self):
        return self.repo.find_all()
