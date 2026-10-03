from src.seed import seed
class RectificationTaskRepository:
    def find_all(self):
        return seed["rectificationTask"]
