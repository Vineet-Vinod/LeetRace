class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        before = sum(value < target for value in nums)
        return list(range(before, before + nums.count(target)))
