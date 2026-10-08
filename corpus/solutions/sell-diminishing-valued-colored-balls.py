class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 10**9 + 7
        levels = sorted(inventory, reverse=True) + [0]
        colors = 0
        profit = 0
        for i in range(len(inventory)):
            colors += 1
            high, low = levels[i], levels[i + 1]
            available = (high - low) * colors
            sold = min(orders, available)
            full, remainder = divmod(sold, colors)
            profit += colors * (high + high - full + 1) * full // 2
            profit += remainder * (high - full)
            orders -= sold
            if orders == 0:
                break
        return profit % mod
