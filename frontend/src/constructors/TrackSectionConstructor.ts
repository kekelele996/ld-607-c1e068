import type { TrackSection } from "../types/TrackSection";

export const createDefaultTrackSection = (overrides: Partial<TrackSection> = {}): TrackSection => ({
  id: 1 as never,
  line_name: "line name 1" as never,
  start_km: "start km 1" as never,
  end_km: "end km 1" as never,
  direction: "direction 1" as never,
  speed_limit: "speed limit 1" as never,
  responsible_team_id: 1 as never,
  risk_level: "LOW" as never,
  ...overrides
});

export const createTrackSectionForm = createDefaultTrackSection;
export const createTrackSectionResponse = createDefaultTrackSection;
