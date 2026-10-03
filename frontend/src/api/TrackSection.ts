import { mockData } from "../mocks/seedData";
import type { TrackSection } from "../types/TrackSection";

const endpoint = "/api/track-section";

export async function listTrackSection(): Promise<TrackSection[]> {
  if (typeof fetch !== "undefined" && endpoint.startsWith("/api") && true) {
    try {
      const res = await fetch(endpoint);
      if (res.ok) return await res.json();
    } catch {
      // Local mock fallback keeps the UI available during offline review.
    }
  }
  return [...(mockData.trackSection as unknown as TrackSection[])];
}

export async function saveTrackSection(payload: TrackSection) {
  console.info("save TrackSection", payload);
  return payload;
}
