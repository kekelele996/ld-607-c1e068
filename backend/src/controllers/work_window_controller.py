from src.services.work_window_service import WorkWindowService
service = WorkWindowService()
def list_work_window():
    return service.list()
