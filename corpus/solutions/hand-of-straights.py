class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        counts = Counter(hand)
        for start in sorted(counts):
            amount = counts[start]
            if amount:
                for value in range(start, start + groupSize):
                    if counts[value] < amount:
                        return False
                    counts[value] -= amount
        return True
