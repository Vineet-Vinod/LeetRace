class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()
        reachable = 0
        added = index = 0
        while reachable < target:
            if index < len(coins) and coins[index] <= reachable + 1:
                reachable += coins[index]
                index += 1
            else:
                reachable += reachable + 1
                added += 1
        return added
