class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        minimum: Dict[int, int] = {}
        answer = None
        for value in nums:
            for start in (value - k, value + k):
                if start in minimum:
                    candidate = prefix + value - minimum[start]
                    answer = candidate if answer is None else max(answer, candidate)
            minimum[value] = min(minimum.get(value, prefix), prefix)
            prefix += value
        return 0 if answer is None else answer
