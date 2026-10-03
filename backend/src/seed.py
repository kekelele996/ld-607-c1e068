seed = {
  "trackSection": [
    {
      "id": 1,
      "line_name": "line name 1",
      "start_km": "start km 1",
      "end_km": "end km 1",
      "direction": "direction 1",
      "speed_limit": "speed limit 1",
      "responsible_team_id": 1,
      "risk_level": "LOW"
    },
    {
      "id": 2,
      "line_name": "line name 2",
      "start_km": "start km 2",
      "end_km": "end km 2",
      "direction": "direction 2",
      "speed_limit": "speed limit 2",
      "responsible_team_id": 2,
      "risk_level": "MEDIUM"
    },
    {
      "id": 3,
      "line_name": "line name 3",
      "start_km": "start km 3",
      "end_km": "end km 3",
      "direction": "direction 3",
      "speed_limit": "speed limit 3",
      "responsible_team_id": 3,
      "risk_level": "HIGH"
    }
  ],
  "trackDefect": [
    {
      "id": 1,
      "section_id": 1,
      "defect_type": "BALLAST_LOSS",
      "km_marker": "km marker 1",
      "severity": "severity 1",
      "discovered_at": "2026-06-11T09:00:00Z",
      "source": "source 1",
      "status": "ASSIGNED",
      "photo_url": "/mock/photo_url-1.png"
    },
    {
      "id": 2,
      "section_id": 2,
      "defect_type": "SUBGRADE_SETTLEMENT",
      "km_marker": "km marker 2",
      "severity": "severity 2",
      "discovered_at": "2026-06-12T09:00:00Z",
      "source": "source 2",
      "status": "WORKING",
      "photo_url": "/mock/photo_url-2.png"
    },
    {
      "id": 3,
      "section_id": 3,
      "defect_type": "FASTENER_LOOSE",
      "km_marker": "km marker 3",
      "severity": "severity 3",
      "discovered_at": "2026-06-13T09:00:00Z",
      "source": "source 3",
      "status": "WAIT_WINDOW",
      "photo_url": "/mock/photo_url-3.png"
    }
  ],
  "workWindow": [
    {
      "id": 1,
      "section_id": 1,
      "window_date": "2026-06-11T09:00:00Z",
      "start_time": "2026-06-11T09:00:00Z",
      "end_time": "2026-06-11T09:00:00Z",
      "window_type": "BALLAST_LOSS",
      "approval_status": "ASSIGNED",
      "dispatcher_note": "dispatcher note 1"
    },
    {
      "id": 2,
      "section_id": 2,
      "window_date": "2026-06-12T09:00:00Z",
      "start_time": "2026-06-12T09:00:00Z",
      "end_time": "2026-06-12T09:00:00Z",
      "window_type": "SUBGRADE_SETTLEMENT",
      "approval_status": "WORKING",
      "dispatcher_note": "dispatcher note 2"
    },
    {
      "id": 3,
      "section_id": 3,
      "window_date": "2026-06-13T09:00:00Z",
      "start_time": "2026-06-13T09:00:00Z",
      "end_time": "2026-06-13T09:00:00Z",
      "window_type": "FASTENER_LOOSE",
      "approval_status": "WAIT_WINDOW",
      "dispatcher_note": "dispatcher note 3"
    }
  ],
  "rectificationTask": [
    {
      "id": 1,
      "defect_id": 1,
      "work_window_id": 1,
      "crew_id": 1,
      "method": "method 1",
      "status": "ASSIGNED",
      "started_at": "2026-06-11T09:00:00Z",
      "finished_at": "2026-06-11T09:00:00Z"
    },
    {
      "id": 2,
      "defect_id": 2,
      "work_window_id": 2,
      "crew_id": 2,
      "method": "method 2",
      "status": "WORKING",
      "started_at": "2026-06-12T09:00:00Z",
      "finished_at": "2026-06-12T09:00:00Z"
    },
    {
      "id": 3,
      "defect_id": 3,
      "work_window_id": 3,
      "crew_id": 3,
      "method": "method 3",
      "status": "WAIT_WINDOW",
      "started_at": "2026-06-13T09:00:00Z",
      "finished_at": "2026-06-13T09:00:00Z"
    }
  ],
  "reviewRecord": [
    {
      "id": 1,
      "task_id": 1,
      "reviewer_id": 1,
      "review_result": "review result 1",
      "measured_value": "measured value 1",
      "review_at": "2026-06-11T09:00:00Z",
      "next_action": "next action 1"
    },
    {
      "id": 2,
      "task_id": 2,
      "reviewer_id": 2,
      "review_result": "review result 2",
      "measured_value": "measured value 2",
      "review_at": "2026-06-12T09:00:00Z",
      "next_action": "next action 2"
    },
    {
      "id": 3,
      "task_id": 3,
      "reviewer_id": 3,
      "review_result": "review result 3",
      "measured_value": "measured value 3",
      "review_at": "2026-06-13T09:00:00Z",
      "next_action": "next action 3"
    }
  ]
}
