class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            left = count = 0
            for right, value in enumerate(nums):
                while value - nums[left] > mid:
                    left += 1
                count += right - left
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low
