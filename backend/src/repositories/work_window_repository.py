from src.seed import seed
class WorkWindowRepository:
    def find_all(self):
        return seed["workWindow"]
