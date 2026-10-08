from typing import List
from collections import deque


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        n = len(boxes)
        weight = [0] * (n + 1)
        changes = [0] * (n + 1)
        for i, (port, w) in enumerate(boxes, 1):
            weight[i] = weight[i - 1] + w
            changes[i] = changes[i - 1] + int(i > 1 and port != boxes[i - 2][0])
        dp = [0] * (n + 1)
        score = [0] * (n + 1)
        candidates = deque([0])
        for i in range(1, n + 1):
            while (
                i - candidates[0] > maxBoxes
                or weight[i] - weight[candidates[0]] > maxWeight
            ):
                candidates.popleft()
            dp[i] = score[candidates[0]] + changes[i] + 2
            if i < n:
                score[i] = dp[i] - changes[i + 1]
                while candidates and score[candidates[-1]] >= score[i]:
                    candidates.pop()
                candidates.append(i)
        return dp[n]
