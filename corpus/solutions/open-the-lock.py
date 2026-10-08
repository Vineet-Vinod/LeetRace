class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocked = set(deadends)
        if "0000" in blocked:
            return -1
        queue = deque([("0000", 0)])
        seen = {"0000"}
        while queue:
            state, distance = queue.popleft()
            if state == target:
                return distance
            for index in range(4):
                digit = int(state[index])
                for next_digit in ((digit + 1) % 10, (digit - 1) % 10):
                    neighbor = state[:index] + str(next_digit) + state[index + 1 :]
                    if neighbor not in blocked and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, distance + 1))
        return -1
