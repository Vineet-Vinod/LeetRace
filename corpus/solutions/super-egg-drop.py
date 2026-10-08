class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1:
            return n
        floors = [0] * (k + 1)
        moves = 0
        while floors[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                floors[eggs] += floors[eggs - 1] + 1
        return moves
