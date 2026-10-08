from typing import List
from functools import cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(left: int, right: int, extra: int) -> int:
            if left > right:
                return 0
            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                extra += 1
            best = dp(left, right - 1, 0) + (extra + 1) ** 2
            for mid in range(left, right):
                if boxes[mid] == boxes[right]:
                    best = max(
                        best, dp(left, mid, extra + 1) + dp(mid + 1, right - 1, 0)
                    )
            return best

        return dp(0, len(boxes) - 1, 0)
