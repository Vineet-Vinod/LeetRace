class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        positions = deque(range(len(deck)))
        result = [0] * len(deck)
        for card in sorted(deck):
            result[positions.popleft()] = card
            if positions:
                positions.append(positions.popleft())
        return result
