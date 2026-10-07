class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, answer = [], []
        consecutive = 0
        for value in nums:
            if value == -1:
                consecutive += 1
                answer.append(seen[-consecutive] if consecutive <= len(seen) else -1)
            else:
                seen.append(value)
                consecutive = 0
        return answer
