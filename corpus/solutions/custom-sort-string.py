class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        result = []
        for char in order:
            result.append(char * counts.pop(char, 0))
        result.extend(char * counts[char] for char in sorted(counts))
        return "".join(result)
