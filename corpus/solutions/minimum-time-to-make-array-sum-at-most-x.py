from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        dp = [0] * (n + 1)
        for seen, (rate, initial) in enumerate(sorted(zip(nums2, nums1)), 1):
            for count in range(seen, 0, -1):
                dp[count] = max(dp[count], dp[count - 1] + initial + rate * count)
        initial, rate = sum(nums1), sum(nums2)
        for time, reduction in enumerate(dp):
            if initial + rate * time - reduction <= x:
                return time
        return -1
