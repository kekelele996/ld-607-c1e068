export interface ReviewRecord {
  id: number;
  task_id: number;
  reviewer_id: number;
  review_result: string;
  measured_value: string;
  review_at: string;
  next_action: string;
}
