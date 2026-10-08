class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        largest = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= largest:
                largest += nums[i]
            else:
                largest = nums[i]
        return largest
