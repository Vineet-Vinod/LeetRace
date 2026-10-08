class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        positions = {word: i for i, word in enumerate(list1)}
        common = [
            (i + j, word)
            for j, word in enumerate(list2)
            if (i := positions.get(word)) is not None
        ]
        if not common:
            return []
        best = min(total for total, _ in common)
        return sorted(word for total, word in common if total == best)
