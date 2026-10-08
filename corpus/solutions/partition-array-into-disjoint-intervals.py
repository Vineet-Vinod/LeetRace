class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        current_max = nums[0]
        boundary = 1
        for index in range(1, len(nums)):
            if nums[index] < left_max:
                boundary = index + 1
                left_max = current_max
            else:
                current_max = max(current_max, nums[index])
        return boundary
