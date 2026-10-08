class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        candidates: list[int] = []
        for i, value in enumerate(nums):
            if not candidates or value < nums[candidates[-1]]:
                candidates.append(i)
        answer = 0
        for j in range(len(nums) - 1, -1, -1):
            while candidates and nums[candidates[-1]] <= nums[j]:
                answer = max(answer, j - candidates.pop())
        return answer
