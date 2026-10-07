class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return "".join(
            char * count
            for char, count in sorted(
                counts.items(), key=lambda item: (-item[1], item[0])
            )
        )
