class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        blocked = set(forbidden)
        if x == 0:
            return 0
        limit = max(max(forbidden, default=0), x) + a + b
        queue = deque([(0, False, 0)])
        seen = {(0, False)}
        while queue:
            position, moved_back, jumps = queue.popleft()
            forward = position + a
            if (
                forward <= limit
                and forward not in blocked
                and (forward, False) not in seen
            ):
                if forward == x:
                    return jumps + 1
                seen.add((forward, False))
                queue.append((forward, False, jumps + 1))
            backward = position - b
            if (
                not moved_back
                and backward >= 0
                and backward not in blocked
                and (backward, True) not in seen
            ):
                if backward == x:
                    return jumps + 1
                seen.add((backward, True))
                queue.append((backward, True, jumps + 1))
        return -1
