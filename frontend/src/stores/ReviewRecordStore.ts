import { defineStore } from "pinia";
import { listReviewRecord } from "../api/ReviewRecord";
export const useReviewRecordStore = defineStore("reviewRecord", {
  state: () => ({ rows: [] as Awaited<ReturnType<typeof listReviewRecord>>, loading: false }),
  actions: { async load() { this.loading = true; this.rows = await listReviewRecord(); this.loading = false; } }
});
