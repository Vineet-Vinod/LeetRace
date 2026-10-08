class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([(x, 0)])
        seen = {x}
        upper = max(x, y) + 11
        while queue:
            value, steps = queue.popleft()
            if value == y:
                return steps
            neighbors = [value - 1, value + 1]
            if value % 5 == 0:
                neighbors.append(value // 5)
            if value % 11 == 0:
                neighbors.append(value // 11)
            for nxt in neighbors:
                if 0 <= nxt <= upper and nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1
