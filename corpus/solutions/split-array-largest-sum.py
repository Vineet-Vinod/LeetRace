class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            parts, total = 1, 0
            for x in nums:
                if total + x > mid:
                    parts += 1
                    total = 0
                total += x
            if parts <= k:
                high = mid
            else:
                low = mid + 1
        return low
