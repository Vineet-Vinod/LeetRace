class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = answer = 0
        for i, value in enumerate(nums, 1):
            prefix += value
            answer = max(answer, (prefix + i - 1) // i)
        return answer
