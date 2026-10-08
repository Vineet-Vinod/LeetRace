class Solution:
    def maximumLength(self, s: str) -> int:
        runs: dict[str, list[int]] = defaultdict(list)
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            runs[s[i]].append(j - i)
            i = j
        answer = 0
        for lengths in runs.values():
            for length in range(1, max(lengths) + 1):
                count = sum(max(0, run - length + 1) for run in lengths)
                if count >= 3:
                    answer = max(answer, length)
        return answer if answer else -1
