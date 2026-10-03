import { defineStore } from "pinia";
import { listTrackSection } from "../api/TrackSection";
export const useTrackSectionStore = defineStore("trackSection", {
  state: () => ({ rows: [] as Awaited<ReturnType<typeof listTrackSection>>, loading: false }),
  actions: { async load() { this.loading = true; this.rows = await listTrackSection(); this.loading = false; } }
});
