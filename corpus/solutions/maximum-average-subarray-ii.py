from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low, high = float(min(nums)), float(max(nums))
        for _ in range(42):
            mid = (low + high) / 2
            prefix = [0.0]
            for x in nums:
                prefix.append(prefix[-1] + x - mid)
            minimum = 0.0
            possible = False
            for i in range(k, len(prefix)):
                minimum = min(minimum, prefix[i - k])
                if prefix[i] - minimum >= 0:
                    possible = True
                    break
            if possible:
                low = mid
            else:
                high = mid
        return low
