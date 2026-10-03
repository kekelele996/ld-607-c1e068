import type { WorkWindow } from "../types/WorkWindow";

export const createDefaultWorkWindow = (overrides: Partial<WorkWindow> = {}): WorkWindow => ({
  id: 1 as never,
  section_id: 1 as never,
  window_date: "2026-06-11T09:00:00Z" as never,
  start_time: "2026-06-11T09:00:00Z" as never,
  end_time: "2026-06-11T09:00:00Z" as never,
  window_type: "BALLAST_LOSS" as never,
  approval_status: "ASSIGNED" as never,
  dispatcher_note: "dispatcher note 1" as never,
  ...overrides
});

export const createWorkWindowForm = createDefaultWorkWindow;
export const createWorkWindowResponse = createDefaultWorkWindow;
