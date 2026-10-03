from src.repositories.review_record_repository import ReviewRecordRepository
class ReviewRecordService:
    def __init__(self):
        self.repo = ReviewRecordRepository()
    def list(self):
        return self.repo.find_all()
