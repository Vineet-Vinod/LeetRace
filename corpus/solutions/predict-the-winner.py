class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        difference = nums[:]
        for length in range(2, len(nums) + 1):
            for left in range(len(nums) - length + 1):
                right = left + length - 1
                difference[left] = max(
                    nums[left] - difference[left + 1], nums[right] - difference[left]
                )
        return difference[0] >= 0
