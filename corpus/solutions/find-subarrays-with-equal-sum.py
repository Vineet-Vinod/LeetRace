class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            total = nums[i] + nums[i + 1]
            if total in seen:
                return True
            seen.add(total)
        return False
