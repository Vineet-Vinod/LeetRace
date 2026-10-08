class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for mask in range(1 << len(nums)):
            out.append([x for i, x in enumerate(nums) if mask >> i & 1])
        return sorted(out)
