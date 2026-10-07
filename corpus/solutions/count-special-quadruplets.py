class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    for d in range(c + 1, len(nums)):
                        result += nums[a] + nums[b] + nums[c] == nums[d]
        return result
