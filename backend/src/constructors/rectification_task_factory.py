def create_rectification_task_dto(**overrides):
    row = {"id":1,"defect_id":1,"work_window_id":1,"crew_id":1,"method":"method 1","status":"ASSIGNED","started_at":"2026-06-11T09:00:00Z","finished_at":"2026-06-11T09:00:00Z"}
    row.update(overrides)
    return row
