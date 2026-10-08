class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = [i for i, char in enumerate(s) if char == c]
        return [min(abs(i - position) for position in positions) for i in range(len(s))]
