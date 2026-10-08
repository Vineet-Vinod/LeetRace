class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses: dict[int, int] = {}
        for winner, loser in matches:
            losses.setdefault(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1
        unbeaten = sorted(player for player, count in losses.items() if count == 0)
        one_loss = sorted(player for player, count in losses.items() if count == 1)
        return [unbeaten, one_loss]
