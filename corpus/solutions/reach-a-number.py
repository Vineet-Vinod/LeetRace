class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        moves = 0
        distance = 0
        while distance < target or (distance - target) % 2:
            moves += 1
            distance += moves
        return moves
