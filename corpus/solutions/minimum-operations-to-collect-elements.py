class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        found: set[int] = set()
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] <= k:
                found.add(nums[index])
            if len(found) == k:
                return len(nums) - index
        return len(nums)
