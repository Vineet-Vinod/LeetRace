from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        boxes = sorted(sorted(box) for box in cuboids)
        dp = []
        for i, box in enumerate(boxes):
            best = 0
            for j in range(i):
                if all(boxes[j][d] <= box[d] for d in range(3)):
                    best = max(best, dp[j])
            dp.append(best + box[2])
        return max(dp)
