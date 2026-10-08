from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        extra = x - y
        low, high = 0, (max(nums) + y - 1) // y
        while low < high:
            middle = (low + high) // 2
            needed = sum(
                max(0, (value - middle * y + extra - 1) // extra) for value in nums
            )
            if needed <= middle:
                high = middle
            else:
                low = middle + 1
        return low
