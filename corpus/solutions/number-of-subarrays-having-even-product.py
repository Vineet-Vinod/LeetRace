class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        odd_run = 0
        odd_only = 0
        for value in nums:
            if value % 2:
                odd_run += 1
            else:
                odd_only += odd_run * (odd_run + 1) // 2
                odd_run = 0
        odd_only += odd_run * (odd_run + 1) // 2
        total = len(nums) * (len(nums) + 1) // 2
        return total - odd_only
