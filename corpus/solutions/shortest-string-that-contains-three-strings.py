class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        import itertools

        def merge(first: str, second: str) -> str:
            if second in first:
                return first
            if first in second:
                return second
            overlap = min(len(first), len(second))
            while overlap and first[-overlap:] != second[:overlap]:
                overlap -= 1
            return first + second[overlap:]

        candidates = []
        for order in itertools.permutations((a, b, c)):
            combined = merge(merge(order[0], order[1]), order[2])
            candidates.append(combined)
        return min(candidates, key=lambda value: (len(value), value))
