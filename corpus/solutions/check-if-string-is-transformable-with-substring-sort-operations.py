from collections import deque


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        positions = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            positions[int(ch)].append(i)
        for ch in t:
            digit = int(ch)
            if not positions[digit]:
                return False
            i = positions[digit][0]
            if any(positions[d] and positions[d][0] < i for d in range(digit)):
                return False
            positions[digit].popleft()
        return True
