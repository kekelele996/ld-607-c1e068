CREATE TABLE IF NOT EXISTS track_section (
  id INTEGER PRIMARY KEY,
  line_name TEXT,
  start_km TEXT,
  end_km TEXT,
  direction TEXT,
  speed_limit TEXT,
  responsible_team_id TEXT,
  risk_level TEXT
);

CREATE TABLE IF NOT EXISTS track_defect (
  id INTEGER PRIMARY KEY,
  section_id TEXT,
  defect_type TEXT,
  km_marker TEXT,
  severity TEXT,
  discovered_at TEXT,
  source TEXT,
  status TEXT,
  photo_url TEXT
);

CREATE TABLE IF NOT EXISTS work_window (
  id INTEGER PRIMARY KEY,
  section_id TEXT,
  window_date TEXT,
  start_time TEXT,
  end_time TEXT,
  window_type TEXT,
  approval_status TEXT,
  dispatcher_note TEXT
);

CREATE TABLE IF NOT EXISTS rectification_task (
  id INTEGER PRIMARY KEY,
  defect_id TEXT,
  work_window_id TEXT,
  crew_id TEXT,
  method TEXT,
  status TEXT,
  started_at TEXT,
  finished_at TEXT
);

CREATE TABLE IF NOT EXISTS review_record (
  id INTEGER PRIMARY KEY,
  task_id TEXT,
  reviewer_id TEXT,
  review_result TEXT,
  measured_value TEXT,
  review_at TEXT,
  next_action TEXT
);

CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY,
  actor TEXT,
  action TEXT,
  target_type TEXT,
  target_id TEXT,
  created_at TEXT
);
