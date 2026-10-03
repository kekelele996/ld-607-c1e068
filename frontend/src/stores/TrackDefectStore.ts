import { defineStore } from "pinia";
import { listTrackDefect } from "../api/TrackDefect";
export const useTrackDefectStore = defineStore("trackDefect", {
  state: () => ({ rows: [] as Awaited<ReturnType<typeof listTrackDefect>>, loading: false }),
  actions: { async load() { this.loading = true; this.rows = await listTrackDefect(); this.loading = false; } }
});
