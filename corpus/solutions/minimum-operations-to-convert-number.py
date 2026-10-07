class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([(start, 0)])
        seen = {start}
        while q:
            value, dist = q.popleft()
            for num in nums:
                for nxt in (value + num, value - num, value ^ num):
                    if nxt == goal:
                        return dist + 1
                    if 0 <= nxt <= 1000 and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, dist + 1))
        return -1
