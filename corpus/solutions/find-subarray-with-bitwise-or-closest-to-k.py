from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        prev = set()
        ans = 10**30
        for v in nums:
            prev = {v} | {x | v for x in prev}
            ans = min(ans, min(abs(x - k) for x in prev))
            if ans == 0:
                return 0
        return ans
