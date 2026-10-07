class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = [0]
        for value in sorted(nums):
            prefix.append(prefix[-1] + value)
        return [bisect_right(prefix, query) - 1 for query in queries]
