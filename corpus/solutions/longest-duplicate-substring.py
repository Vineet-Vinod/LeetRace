class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        suffixes = list(range(n))
        ranks = [ord(c) for c in s]
        step = 1
        while step < n:
            suffixes.sort(
                key=lambda i: (ranks[i], ranks[i + step] if i + step < n else -1)
            )
            new = [0] * n
            for j in range(1, n):
                a, b = suffixes[j - 1], suffixes[j]
                new[b] = new[a] + (
                    (ranks[a], ranks[a + step] if a + step < n else -1)
                    != (ranks[b], ranks[b + step] if b + step < n else -1)
                )
            ranks = new
            if ranks[suffixes[-1]] == n - 1:
                break
            step *= 2
        position = [0] * n
        for j, i in enumerate(suffixes):
            position[i] = j
        longest, best, length = 0, n, 0
        for i in range(n):
            rank = position[i]
            if rank == 0:
                length = 0
                continue
            j = suffixes[rank - 1]
            while i + length < n and j + length < n and s[i + length] == s[j + length]:
                length += 1
            if length > longest or (length == longest and rank < best):
                longest, best = length, rank
            length = max(0, length - 1)
        return s[suffixes[best] : suffixes[best] + longest] if longest else ""
