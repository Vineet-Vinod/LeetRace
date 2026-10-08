class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        answer = -1
        for middle in range(n):
            left = max(
                (profits[i] for i in range(middle) if prices[i] < prices[middle]),
                default=None,
            )
            right = max(
                (
                    profits[i]
                    for i in range(middle + 1, n)
                    if prices[i] > prices[middle]
                ),
                default=None,
            )
            if left is not None and right is not None:
                answer = max(answer, left + profits[middle] + right)
        return answer
