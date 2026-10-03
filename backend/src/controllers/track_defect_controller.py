from src.services.track_defect_service import TrackDefectService
service = TrackDefectService()
def list_track_defect():
    return service.list()
