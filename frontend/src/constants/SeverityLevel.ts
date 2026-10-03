export const SeverityLevel = ["A","B","C","D"] as const;
export type SeverityLevel = (typeof SeverityLevel)[number];
export const SeverityLevelText: Record<SeverityLevel, string> = Object.fromEntries(SeverityLevel.map((value) => [value, value.replace(/_/g, " ")])) as Record<SeverityLevel, string>;
