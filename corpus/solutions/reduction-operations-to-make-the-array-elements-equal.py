class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        distinct = sorted(set(nums))
        ranks = {value: index for index, value in enumerate(distinct)}
        return sum(ranks[value] for value in nums)
