class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        result = [0] if low == 0 else []
        queue = deque(range(1, 10))
        while queue:
            value = queue.popleft()
            if low <= value <= high:
                result.append(value)
            if value > high // 10:
                continue
            last = value % 10
            if last > 0:
                queue.append(value * 10 + last - 1)
            if last < 9:
                queue.append(value * 10 + last + 1)
        return sorted(result)
