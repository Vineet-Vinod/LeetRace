class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        latest = {}
        best = len(cards) + 1
        for index, card in enumerate(cards):
            if card in latest:
                best = min(best, index - latest[card] + 1)
            latest[card] = index
        return best if best <= len(cards) else -1
