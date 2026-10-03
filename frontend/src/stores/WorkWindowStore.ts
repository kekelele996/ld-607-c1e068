import { defineStore } from "pinia";
import { listWorkWindow } from "../api/WorkWindow";
export const useWorkWindowStore = defineStore("workWindow", {
  state: () => ({ rows: [] as Awaited<ReturnType<typeof listWorkWindow>>, loading: false }),
  actions: { async load() { this.loading = true; this.rows = await listWorkWindow(); this.loading = false; } }
});
