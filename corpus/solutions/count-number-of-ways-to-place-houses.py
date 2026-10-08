class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10**9 + 7
        empty, occupied = 1, 0
        for _ in range(n):
            empty, occupied = (empty + occupied) % mod, empty
        return (empty + occupied) ** 2 % mod
