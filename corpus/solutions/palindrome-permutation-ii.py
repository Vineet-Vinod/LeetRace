class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counts = Counter(s)
        odd = [char for char, count in counts.items() if count % 2]
        if len(odd) > 1:
            return []
        half_counts = {char: count // 2 for char, count in counts.items()}
        half_length = len(s) // 2
        result = []

        def build(prefix: List[str]) -> None:
            if len(prefix) == half_length:
                first = "".join(prefix)
                result.append(first + (odd[0] if odd else "") + first[::-1])
                return
            for char in sorted(half_counts):
                if half_counts[char] == 0:
                    continue
                half_counts[char] -= 1
                prefix.append(char)
                build(prefix)
                prefix.pop()
                half_counts[char] += 1

        build([])
        return result
