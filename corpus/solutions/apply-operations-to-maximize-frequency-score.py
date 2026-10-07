from typing import List


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        pref = [0]
        for v in nums:
            pref.append(pref[-1] + v)
        left = 0
        best = 0
        for right in range(len(nums)):
            while True:
                mid = (left + right) // 2
                cost = (
                    nums[mid] * (mid - left)
                    - (pref[mid] - pref[left])
                    + pref[right + 1]
                    - pref[mid + 1]
                    - nums[mid] * (right - mid)
                )
                if cost <= k:
                    break
                left += 1
            best = max(best, right - left + 1)
        return best
