class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        memo: dict[int, bool] = {}

        def win(mask: int, remaining: int) -> bool:
            if mask in memo:
                return memo[mask]
            for value in range(1, maxChoosableInteger + 1):
                bit = 1 << (value - 1)
                if not mask & bit and (
                    value >= remaining or not win(mask | bit, remaining - value)
                ):
                    memo[mask] = True
                    return True
            memo[mask] = False
            return False

        return win(0, desiredTotal)
