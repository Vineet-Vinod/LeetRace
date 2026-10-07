class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        suffixes = list(range(n))
        rank = [ord(char) for char in s]
        step = 1
        while step < n:
            suffixes.sort(
                key=lambda i: (rank[i], rank[i + step] if i + step < n else -1)
            )
            next_rank = [0] * n
            for position in range(1, n):
                prior, current = suffixes[position - 1], suffixes[position]
                prior_key = (
                    rank[prior],
                    rank[prior + step] if prior + step < n else -1,
                )
                current_key = (
                    rank[current],
                    rank[current + step] if current + step < n else -1,
                )
                next_rank[current] = next_rank[prior] + (prior_key != current_key)
            rank = next_rank
            if rank[suffixes[-1]] == n - 1:
                break
            step *= 2
        inverse = [0] * n
        for position, suffix in enumerate(suffixes):
            inverse[suffix] = position
        common = 0
        best = 0
        for start in range(n):
            position = inverse[start]
            if position == n - 1:
                common = 0
                continue
            other = suffixes[position + 1]
            while (
                start + common < n
                and other + common < n
                and s[start + common] == s[other + common]
            ):
                common += 1
            best = max(best, common)
            if common:
                common -= 1
        return best
