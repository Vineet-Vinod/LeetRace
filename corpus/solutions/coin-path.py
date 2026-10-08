from typing import List


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        costs = [float("inf")] * n
        following = [-1] * n
        if coins[-1] != -1:
            costs[-1] = coins[-1]
        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue
            for j in range(i + 1, min(n, i + maxJump + 1)):
                value = coins[i] + costs[j]
                if value < costs[i]:
                    costs[i], following[i] = value, j
        if costs[0] == float("inf"):
            return []
        path = []
        i = 0
        while i != -1:
            path.append(i + 1)
            i = following[i]
        return path
