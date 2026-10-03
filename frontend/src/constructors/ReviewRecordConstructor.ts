import type { ReviewRecord } from "../types/ReviewRecord";

export const createDefaultReviewRecord = (overrides: Partial<ReviewRecord> = {}): ReviewRecord => ({
  id: 1 as never,
  task_id: 1 as never,
  reviewer_id: 1 as never,
  review_result: "review result 1" as never,
  measured_value: "measured value 1" as never,
  review_at: "2026-06-11T09:00:00Z" as never,
  next_action: "next action 1" as never,
  ...overrides
});

export const createReviewRecordForm = createDefaultReviewRecord;
export const createReviewRecordResponse = createDefaultReviewRecord;
