class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        output: list[str] = []
        previous = ""
        while len(output) < len(s):
            remaining = len(s) - len(output) - 1
            chosen = None
            for char in sorted(counts):
                if char == previous or counts[char] == 0:
                    continue
                counts[char] -= 1
                feasible = all(
                    count
                    <= (remaining // 2 if letter == char else (remaining + 1) // 2)
                    for letter, count in counts.items()
                )
                if feasible:
                    chosen = char
                    break
                counts[char] += 1
            if chosen is None:
                return ""
            output.append(chosen)
            previous = chosen
        return "".join(output)
