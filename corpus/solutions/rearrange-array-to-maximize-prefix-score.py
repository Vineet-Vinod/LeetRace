class Solution:
    def maxScore(self, nums: List[int]) -> int:
        total = 0
        answer = 0
        for value in sorted(nums, reverse=True):
            total += value
            if total <= 0:
                break
            answer += 1
        return answer
