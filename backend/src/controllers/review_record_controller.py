from src.services.review_record_service import ReviewRecordService
service = ReviewRecordService()
def list_review_record():
    return service.list()
