class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        displacement = moves.count("R") - moves.count("L")
        return abs(displacement) + moves.count("_")
