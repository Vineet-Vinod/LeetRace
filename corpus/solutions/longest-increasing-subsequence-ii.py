from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        size = 1
        while size <= max(nums):
            size *= 2
        tree = [0] * (2 * size)
        for x in nums:
            left, right = max(1, x - k) + size, x + size
            best = 0
            while left < right:
                if left & 1:
                    best = max(best, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    best = max(best, tree[right])
                left //= 2
                right //= 2
            pos = size + x
            tree[pos] = max(tree[pos], best + 1)
            while pos > 1:
                pos //= 2
                tree[pos] = max(tree[pos * 2], tree[pos * 2 + 1])
        return tree[1]
