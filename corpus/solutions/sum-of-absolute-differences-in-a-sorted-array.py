class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        prefix = 0
        answer: list[int] = []
        for i, value in enumerate(nums):
            left = value * i - prefix
            right = total - prefix - value - value * (n - i - 1)
            answer.append(left + right)
            prefix += value
        return answer
