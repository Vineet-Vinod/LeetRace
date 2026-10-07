class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counts: Dict[int, Dict[int, int]] = {}
        for player, color in pick:
            counts.setdefault(player, {})[color] = (
                counts.setdefault(player, {}).get(color, 0) + 1
            )
        return sum(
            any(count > player for count in counts.get(player, {}).values())
            for player in range(n)
        )
