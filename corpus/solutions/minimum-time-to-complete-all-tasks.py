from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        active = [0] * 2001
        for start, end, duration in sorted(tasks, key=lambda task: task[1]):
            missing = duration - sum(active[start : end + 1])
            for t in range(end, start - 1, -1):
                if missing <= 0:
                    break
                if not active[t]:
                    active[t] = 1
                    missing -= 1
        return sum(active)
