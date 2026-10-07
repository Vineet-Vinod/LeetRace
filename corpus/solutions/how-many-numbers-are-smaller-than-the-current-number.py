class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        first_index = {}
        for i, value in enumerate(ordered):
            if value not in first_index:
                first_index[value] = i
        return [first_index[value] for value in nums]
