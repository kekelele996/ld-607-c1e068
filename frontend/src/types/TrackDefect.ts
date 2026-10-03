export interface TrackDefect {
  id: number;
  section_id: number;
  defect_type: string;
  km_marker: string;
  severity: string;
  discovered_at: string;
  source: string;
  status: string;
  photo_url: string;
}
