from src.services.rectification_task_service import RectificationTaskService
service = RectificationTaskService()
def list_rectification_task():
    return service.list()
