class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        answer = []
        maximum = 0
        score = 0
        for value in nums:
            maximum = max(maximum, value)
            score += value + maximum
            answer.append(score)
        return answer
