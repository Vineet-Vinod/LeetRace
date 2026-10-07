class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def can_skip(index):
            return (
                all(nums[i] < nums[i + 1] for i in range(index - 1))
                and (
                    index == 0
                    or index == len(nums) - 1
                    or nums[index - 1] < nums[index + 1]
                )
                and all(nums[i] < nums[i + 1] for i in range(index + 1, len(nums) - 1))
            )

        for index in range(len(nums) - 1):
            if nums[index] >= nums[index + 1]:
                return can_skip(index) or can_skip(index + 1)
        return True
