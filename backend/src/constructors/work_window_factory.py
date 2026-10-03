def create_work_window_dto(**overrides):
    row = {"id":1,"section_id":1,"window_date":"2026-06-11T09:00:00Z","start_time":"2026-06-11T09:00:00Z","end_time":"2026-06-11T09:00:00Z","window_type":"BALLAST_LOSS","approval_status":"ASSIGNED","dispatcher_note":"dispatcher note 1"}
    row.update(overrides)
    return row
