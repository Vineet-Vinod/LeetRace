class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = Counter()
        answer = 0
        for value in nums:
            answer += counts[value - k] + counts[value + k]
            counts[value] += 1
        return answer
