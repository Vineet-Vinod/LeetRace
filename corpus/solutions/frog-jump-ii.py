class Solution:
    def maxJump(self, stones: List[int]) -> int:
        answer = stones[1] - stones[0]
        for i in range(2, len(stones)):
            answer = max(answer, stones[i] - stones[i - 2])
        return answer
