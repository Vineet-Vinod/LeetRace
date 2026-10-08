class Solution:
    def maximumLength(self, s: str) -> int:
        runs = {}
        start = 0
        while start < len(s):
            end = start
            while end < len(s) and s[end] == s[start]:
                end += 1
            length = end - start
            for size in range(1, length + 1):
                runs.setdefault(s[start], {})[size] = (
                    runs.setdefault(s[start], {}).get(size, 0) + length - size + 1
                )
            start = end
        answer = 0
        for counts in runs.values():
            for length, occurrences in counts.items():
                if occurrences >= 3:
                    answer = max(answer, length)
        return answer if answer else -1
