class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        unavailable = set(banned)
        total = count = 0
        for value in range(1, n + 1):
            if value not in unavailable and total + value <= maxSum:
                total += value
                count += 1
        return count
