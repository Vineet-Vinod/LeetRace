class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts = sorted(events)
        best = 0
        ans = 0
        ends = []
        for s, e, v in starts:
            while ends and ends[0][0] < s:
                end, val = heappop(ends)
                best = max(best, val)
            ans = max(ans, best + v, v)
            heappush(ends, (e, v))
        return ans
