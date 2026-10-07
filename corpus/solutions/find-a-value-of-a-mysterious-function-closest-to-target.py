from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        previous = set()
        answer = 10**8
        for x in arr:
            previous = {x} | {x & v for v in previous}
            answer = min(answer, min(abs(v - target) for v in previous))
        return answer
