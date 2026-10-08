class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counts = Counter(nums)
        answer = 0
        for first in set(nums):
            if not target.startswith(first):
                continue
            second = target[len(first) :]
            if second not in counts:
                continue
            answer += counts[first] * counts[second]
            if first == second:
                answer -= counts[first]
        return answer
