class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) % 2 else "Bob"
