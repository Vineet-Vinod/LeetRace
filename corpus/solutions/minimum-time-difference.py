class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(value[:2]) * 60 + int(value[3:]) for value in timePoints)
        differences = [minutes[i] - minutes[i - 1] for i in range(1, len(minutes))]
        differences.append(minutes[0] + 1440 - minutes[-1])
        return min(differences)
