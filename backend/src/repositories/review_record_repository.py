from src.seed import seed
class ReviewRecordRepository:
    def find_all(self):
        return seed["reviewRecord"]
