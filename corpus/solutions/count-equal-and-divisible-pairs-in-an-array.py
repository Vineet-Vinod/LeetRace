class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        for i, value in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if value == nums[j] and (i * j) % k == 0:
                    count += 1
        return count
