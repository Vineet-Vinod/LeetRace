class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = {s}
        pending = deque([s])
        best = s
        while pending:
            current = pending.popleft()
            if current < best:
                best = current
            chars = list(current)
            for index in range(1, len(chars), 2):
                chars[index] = str((int(chars[index]) + a) % 10)
            added = "".join(chars)
            rotated = current[-b:] + current[:-b]
            for candidate in (added, rotated):
                if candidate not in seen:
                    seen.add(candidate)
                    pending.append(candidate)
        return best
