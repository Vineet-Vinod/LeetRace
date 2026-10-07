class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [[0] * 101]
        for value in nums:
            counts = prefix[-1].copy()
            counts[value] += 1
            prefix.append(counts)
        answers = []
        for left, right in queries:
            previous = -1
            best = float("inf")
            for value in range(1, 101):
                if prefix[right + 1][value] - prefix[left][value]:
                    if previous >= 0:
                        best = min(best, value - previous)
                    previous = value
            answers.append(-1 if best == float("inf") else int(best))
        return answers
