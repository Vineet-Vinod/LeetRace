class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        frequency = Counter({0: 1})
        prefix = answer = 0
        for value in nums:
            prefix += value
            answer += frequency[prefix - goal]
            frequency[prefix] += 1
        return answer
