class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1
        for coin in coins:
            for total in range(coin, amount + 1):
                ways[total] += ways[total - coin]
        return ways[amount]
