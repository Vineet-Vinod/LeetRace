class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)
        answer = []
        for kind, day, daily_cap in queries:
            earliest = day + 1
            latest = (day + 1) * daily_cap
            answer.append(earliest <= prefix[kind + 1] and latest > prefix[kind])
        return answer
