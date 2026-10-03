import { mockData } from "../mocks/seedData";
import type { ReviewRecord } from "../types/ReviewRecord";

const endpoint = "/api/review-record";

export async function listReviewRecord(): Promise<ReviewRecord[]> {
  if (typeof fetch !== "undefined" && endpoint.startsWith("/api") && true) {
    try {
      const res = await fetch(endpoint);
      if (res.ok) return await res.json();
    } catch {
      // Local mock fallback keeps the UI available during offline review.
    }
  }
  return [...(mockData.reviewRecord as unknown as ReviewRecord[])];
}

export async function saveReviewRecord(payload: ReviewRecord) {
  console.info("save ReviewRecord", payload);
  return payload;
}
