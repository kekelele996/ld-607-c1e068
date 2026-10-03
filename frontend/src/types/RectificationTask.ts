export interface RectificationTask {
  id: number;
  defect_id: number;
  work_window_id: number;
  crew_id: number;
  method: string;
  status: string;
  started_at: string;
  finished_at: string;
}
