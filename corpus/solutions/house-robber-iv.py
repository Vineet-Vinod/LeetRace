class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low, high = min(nums), max(nums)
        while low < high:
            limit = (low + high) // 2
            chosen = 0
            index = 0
            while index < len(nums):
                if nums[index] <= limit:
                    chosen += 1
                    index += 2
                else:
                    index += 1
            if chosen >= k:
                high = limit
            else:
                low = limit + 1
        return low
