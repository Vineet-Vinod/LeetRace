class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)
        return (
            index
            if all(value == largest or largest >= 2 * value for value in nums)
            else -1
        )
