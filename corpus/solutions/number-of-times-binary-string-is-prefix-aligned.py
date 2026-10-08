class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maximum = answer = 0
        for i, value in enumerate(flips, 1):
            maximum = max(maximum, value)
            answer += maximum == i
        return answer
