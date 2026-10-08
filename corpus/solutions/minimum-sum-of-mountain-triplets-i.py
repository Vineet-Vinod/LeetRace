class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        best = inf
        for middle in range(1, len(nums) - 1):
            left = min(nums[:middle])
            right = min(nums[middle + 1 :])
            if left < nums[middle] and right < nums[middle]:
                best = min(best, left + nums[middle] + right)
        return -1 if best == inf else int(best)
