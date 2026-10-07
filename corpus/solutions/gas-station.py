class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        size = len(gas)
        changes = [gas[index] - cost[index] for index in range(size)]
        if sum(changes) < 0:
            return -1
        prefix = [0]
        for change in changes * 2:
            prefix.append(prefix[-1] + change)

        minima: deque[int] = deque()
        for position in range(1, size + 1):
            while minima and prefix[minima[-1]] >= prefix[position]:
                minima.pop()
            minima.append(position)

        for start in range(size):
            while minima and minima[0] <= start:
                minima.popleft()
            if prefix[minima[0]] >= prefix[start]:
                return start
            next_position = start + size + 1
            while minima and prefix[minima[-1]] >= prefix[next_position]:
                minima.pop()
            minima.append(next_position)
        return -1
