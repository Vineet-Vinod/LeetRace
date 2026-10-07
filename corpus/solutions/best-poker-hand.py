class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        counts = Counter(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        if max(counts.values()) >= 3:
            return "Three of a Kind"
        if max(counts.values()) == 2:
            return "Pair"
        return "High Card"
