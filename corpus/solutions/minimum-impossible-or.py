class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        values = set(nums)
        answer = 1
        while answer in values:
            answer <<= 1
        return answer
