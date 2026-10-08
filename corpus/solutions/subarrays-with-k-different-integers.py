from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit: int) -> int:
            count = defaultdict(int)
            left = total = 0
            for right, value in enumerate(nums):
                count[value] += 1
                while len(count) > limit:
                    old = nums[left]
                    count[old] -= 1
                    if count[old] == 0:
                        del count[old]
                    left += 1
                total += right - left + 1
            return total

        return at_most(k) - at_most(k - 1)
