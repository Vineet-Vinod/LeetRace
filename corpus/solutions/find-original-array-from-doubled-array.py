class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        counts = Counter(changed)
        original = []
        for value in sorted(counts):
            if value == 0:
                pairs = counts[value] // 2
                if counts[value] % 2:
                    return []
                original.extend([0] * pairs)
                continue
            if counts[value] > counts[2 * value]:
                return []
            original.extend([value] * counts[value])
            counts[2 * value] -= counts[value]
        return original
