import type { RectificationTask } from "../types/RectificationTask";

export const createDefaultRectificationTask = (overrides: Partial<RectificationTask> = {}): RectificationTask => ({
  id: 1 as never,
  defect_id: 1 as never,
  work_window_id: 1 as never,
  crew_id: 1 as never,
  method: "method 1" as never,
  status: "ASSIGNED" as never,
  started_at: "2026-06-11T09:00:00Z" as never,
  finished_at: "2026-06-11T09:00:00Z" as never,
  ...overrides
});

export const createRectificationTaskForm = createDefaultRectificationTask;
export const createRectificationTaskResponse = createDefaultRectificationTask;
