class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: list[tuple[int, ...]] = [()]
        for value in nums:
            result += [subset + (value,) for subset in result]
        return [list(subset) for subset in sorted(set(result))]
