class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10**9 + 7
        seen: Dict[int, int] = defaultdict(int)
        answer = 0
        for value in deliciousness:
            for power in (1 << bit for bit in range(22)):
                answer += seen[power - value]
            seen[value] += 1
        return answer % mod
