class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        from collections import deque

        digits = sorted({digit1, digit2})
        queue = deque((d, d % k) for d in digits if d != 0)
        visited = {(value, rem) for value, rem in queue}
        while queue:
            value, rem = queue.popleft()
            if value > k and rem == 0:
                return value if value <= 2**31 - 1 else -1
            for digit in digits:
                nxt = value * 10 + digit
                if nxt <= 2**31 - 1 and (nxt, (rem * 10 + digit) % k) not in visited:
                    state = (nxt, (rem * 10 + digit) % k)
                    visited.add(state)
                    queue.append(state)
        return -1
