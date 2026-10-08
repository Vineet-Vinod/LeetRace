class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1
        for previous, current in zip(nums, nums[1:]):
            if current > previous:
                up = down + 1
            elif current < previous:
                down = up + 1
        return up if up > down else down
