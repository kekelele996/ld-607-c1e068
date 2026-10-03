def create_track_defect_dto(**overrides):
    row = {"id":1,"section_id":1,"defect_type":"BALLAST_LOSS","km_marker":"km marker 1","severity":"severity 1","discovered_at":"2026-06-11T09:00:00Z","source":"source 1","status":"ASSIGNED","photo_url":"/mock/photo_url-1.png"}
    row.update(overrides)
    return row
