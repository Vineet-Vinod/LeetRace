class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = sum(
            max(0, end - start - 2) for start, end in self._runs(colors, "A")
        )
        bob_moves = sum(
            max(0, end - start - 2) for start, end in self._runs(colors, "B")
        )
        return alice_moves > bob_moves

    def _runs(self, colors: str, color: str) -> list[tuple[int, int]]:
        runs = []
        start = 0
        while start < len(colors):
            if colors[start] != color:
                start += 1
                continue
            end = start + 1
            while end < len(colors) and colors[end] == color:
                end += 1
            runs.append((start, end))
            start = end
        return runs
