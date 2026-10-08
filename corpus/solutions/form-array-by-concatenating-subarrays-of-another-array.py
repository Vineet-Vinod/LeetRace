class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        position = 0
        for group in groups:
            while (
                position + len(group) <= len(nums)
                and nums[position : position + len(group)] != group
            ):
                position += 1
            if position + len(group) > len(nums):
                return False
            position += len(group)
        return True
