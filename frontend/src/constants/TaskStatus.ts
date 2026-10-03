export const TaskStatus = ["WAIT_WINDOW","ASSIGNED","WORKING","REVIEWING","CLOSED","REWORK"] as const;
export type TaskStatus = (typeof TaskStatus)[number];
export const TaskStatusText: Record<TaskStatus, string> = Object.fromEntries(TaskStatus.map((value) => [value, value.replace(/_/g, " ")])) as Record<TaskStatus, string>;
