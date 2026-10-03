export const DefectType = ["RAIL_WEAR","BALLAST_LOSS","SUBGRADE_SETTLEMENT","FASTENER_LOOSE","DRAINAGE_BLOCK"] as const;
export type DefectType = (typeof DefectType)[number];
export const DefectTypeText: Record<DefectType, string> = Object.fromEntries(DefectType.map((value) => [value, value.replace(/_/g, " ")])) as Record<DefectType, string>;
