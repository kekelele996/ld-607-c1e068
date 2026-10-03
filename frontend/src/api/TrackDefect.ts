import { mockData } from "../mocks/seedData";
import type { TrackDefect } from "../types/TrackDefect";

const endpoint = "/api/track-defect";

export async function listTrackDefect(): Promise<TrackDefect[]> {
  if (typeof fetch !== "undefined" && endpoint.startsWith("/api") && true) {
    try {
      const res = await fetch(endpoint);
      if (res.ok) return await res.json();
    } catch {
      // Local mock fallback keeps the UI available during offline review.
    }
  }
  return [...(mockData.trackDefect as unknown as TrackDefect[])];
}

export async function saveTrackDefect(payload: TrackDefect) {
  console.info("save TrackDefect", payload);
  return payload;
}
