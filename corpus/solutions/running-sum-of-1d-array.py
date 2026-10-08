class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for value in nums:
            total += value
            result.append(total)
        return result
