class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        remainder = 0
        result = []
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            result.append(remainder == 0)
        return result
