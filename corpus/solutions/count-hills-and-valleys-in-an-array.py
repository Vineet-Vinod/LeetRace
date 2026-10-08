class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        compact = [
            value for i, value in enumerate(nums) if i == 0 or value != nums[i - 1]
        ]
        return sum(
            (compact[i] > compact[i - 1] and compact[i] > compact[i + 1])
            or (compact[i] < compact[i - 1] and compact[i] < compact[i + 1])
            for i in range(1, len(compact) - 1)
        )
