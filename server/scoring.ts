/**
 * Two thirds of the maximum score reward character efficiency; one third rewards
 * time remaining after locking. An unlocked solve receives no time bonus.
 */
export function roundPoints(
  charCount: number | null,
  finishTime: number | null,
  minSolvedChars: number,
  durationSeconds: number,
): number {
  if (charCount === null || minSolvedChars === Infinity || charCount <= 0 || durationSeconds <= 0) return 0;
  const characterScore = minSolvedChars / charCount;
  const timeScore = finishTime === null ? 0 : Math.max(0, Math.min(1, 1 - finishTime / durationSeconds));
  return 100 * (2 * characterScore + timeScore) / 3;
}
