from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        positions = []
        run = 0
        longest = 0
        for i, v in enumerate(nums):
            if v:
                positions.append(i)
                run += 1
                longest = max(longest, run)
            else:
                run = 0
        c = min(k, 3, longest)
        if maxChanges >= k - c:
            return max(0, c - 1) + 2 * (k - c)
        take = k - maxChanges
        prefix = [0]
        for p in positions:
            prefix.append(prefix[-1] + p)
        best = 10**30
        for left in range(len(positions) - take + 1):
            right = left + take
            mid = (left + right) // 2
            p = positions[mid]
            value = (
                p * (mid - left)
                - (prefix[mid] - prefix[left])
                + prefix[right]
                - prefix[mid]
                - p * (right - mid)
            )
            best = min(best, value)
        return best + 2 * maxChanges
