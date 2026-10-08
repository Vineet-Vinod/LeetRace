class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = sorted((x, y))
        diff = [0] * (n + 2)

        def add(a: int, b: int) -> None:
            if a > b:
                return
            diff[a] += 2
            diff[b + 1] -= 2

        for i in range(1, n):
            a = abs(i - x) + 1
            end = y
            split = min(end, (a + y + i) // 2)
            lo = i + 1
            if lo <= split:
                add(lo - i, split - i)
            lo = max(lo, split + 1)
            if lo <= end:
                add(a + y - end, a + y - lo)
            lo = max(i + 1, y + 1)
            if lo <= n:
                offset = min(-i, a - y)
                add(lo + offset, n + offset)
        answer = []
        running = 0
        for distance in range(1, n + 1):
            running += diff[distance]
            answer.append(running)
        return answer
