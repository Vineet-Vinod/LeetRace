class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(values) for values in itertools.permutations(sorted(nums))]
