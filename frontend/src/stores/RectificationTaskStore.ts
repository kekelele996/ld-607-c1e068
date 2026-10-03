import { defineStore } from "pinia";
import { listRectificationTask } from "../api/RectificationTask";
export const useRectificationTaskStore = defineStore("rectificationTask", {
  state: () => ({ rows: [] as Awaited<ReturnType<typeof listRectificationTask>>, loading: false }),
  actions: { async load() { this.loading = true; this.rows = await listRectificationTask(); this.loading = false; } }
});
