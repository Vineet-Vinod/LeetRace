class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        bad_edges = sum(colors[i] == colors[(i + 1) % n] for i in range(k - 1))
        result = 0
        for start in range(n):
            if bad_edges == 0:
                result += 1
            if start + 1 < n:
                bad_edges -= colors[start] == colors[(start + 1) % n]
                bad_edges += colors[(start + k - 1) % n] == colors[(start + k) % n]
        return result
