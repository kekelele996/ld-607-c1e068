import type { TrackDefect } from "../types/TrackDefect";

export const createDefaultTrackDefect = (overrides: Partial<TrackDefect> = {}): TrackDefect => ({
  id: 1 as never,
  section_id: 1 as never,
  defect_type: "BALLAST_LOSS" as never,
  km_marker: "km marker 1" as never,
  severity: "severity 1" as never,
  discovered_at: "2026-06-11T09:00:00Z" as never,
  source: "source 1" as never,
  status: "ASSIGNED" as never,
  photo_url: "/mock/photo_url-1.png" as never,
  ...overrides
});

export const createTrackDefectForm = createDefaultTrackDefect;
export const createTrackDefectResponse = createDefaultTrackDefect;
