import { mockData } from "../mocks/seedData";
import type { WorkWindow } from "../types/WorkWindow";

const endpoint = "/api/work-window";

export async function listWorkWindow(): Promise<WorkWindow[]> {
  if (typeof fetch !== "undefined" && endpoint.startsWith("/api") && true) {
    try {
      const res = await fetch(endpoint);
      if (res.ok) return await res.json();
    } catch {
      // Local mock fallback keeps the UI available during offline review.
    }
  }
  return [...(mockData.workWindow as unknown as WorkWindow[])];
}

export async function saveWorkWindow(payload: WorkWindow) {
  console.info("save WorkWindow", payload);
  return payload;
}
