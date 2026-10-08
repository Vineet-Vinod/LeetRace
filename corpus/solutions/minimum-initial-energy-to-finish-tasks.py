from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        spent = 0
        initial = 0
        for actual, minimum in sorted(
            tasks, key=lambda task: task[1] - task[0], reverse=True
        ):
            initial = max(initial, spent + minimum)
            spent += actual
        return initial
