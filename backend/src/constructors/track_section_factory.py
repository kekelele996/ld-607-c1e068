def create_track_section_dto(**overrides):
    row = {"id":1,"line_name":"line name 1","start_km":"start km 1","end_km":"end km 1","direction":"direction 1","speed_limit":"speed limit 1","responsible_team_id":1,"risk_level":"LOW"}
    row.update(overrides)
    return row
