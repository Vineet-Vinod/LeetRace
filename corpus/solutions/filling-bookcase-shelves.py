class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [10**9] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            width = height = 0
            for start in range(end - 1, -1, -1):
                width += books[start][0]
                if width > shelfWidth:
                    break
                height = max(height, books[start][1])
                dp[end] = min(dp[end], dp[start] + height)
        return dp[n]
