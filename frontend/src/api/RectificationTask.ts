import { mockData } from "../mocks/seedData";
import type { RectificationTask } from "../types/RectificationTask";

const endpoint = "/api/rectification-task";

export async function listRectificationTask(): Promise<RectificationTask[]> {
  if (typeof fetch !== "undefined" && endpoint.startsWith("/api") && true) {
    try {
      const res = await fetch(endpoint);
      if (res.ok) return await res.json();
    } catch {
      // Local mock fallback keeps the UI available during offline review.
    }
  }
  return [...(mockData.rectificationTask as unknown as RectificationTask[])];
}

export async function saveRectificationTask(payload: RectificationTask) {
  console.info("save RectificationTask", payload);
  return payload;
}
