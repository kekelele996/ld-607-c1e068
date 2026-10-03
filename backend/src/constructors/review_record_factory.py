def create_review_record_dto(**overrides):
    row = {"id":1,"task_id":1,"reviewer_id":1,"review_result":"review result 1","measured_value":"measured value 1","review_at":"2026-06-11T09:00:00Z","next_action":"next action 1"}
    row.update(overrides)
    return row
