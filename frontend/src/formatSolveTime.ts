export function formatSolveTime(seconds: number) {
  const tenths = Math.round(seconds * 10);
  if (tenths < 600) return `${(tenths / 10).toFixed(1)} sec`;

  const second = `${String(Math.floor(tenths / 10) % 60).padStart(2, "0")}.${tenths % 10}`;
  const minute = String(Math.floor(tenths / 600) % 60).padStart(2, "0");
  if (tenths < 36_000) return `${minute}:${second}`;

  const hour = String(Math.floor(tenths / 36_000)).padStart(2, "0");
  return `${hour}:${minute}:${second}`;
}
