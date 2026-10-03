from src.services.track_section_service import TrackSectionService
service = TrackSectionService()
def list_track_section():
    return service.list()
