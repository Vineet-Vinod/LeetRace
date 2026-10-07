from collections import deque


class Solution:
    def timeTaken(self, arrival: list[int], state: list[int]) -> list[int]:
        n = len(arrival)
        queue = [deque(), deque()]
        answer = [0] * n
        i = 0
        time = 0
        previous = 1
        while i < n or queue[0] or queue[1]:
            if not queue[0] and not queue[1] and i < n and time < arrival[i]:
                time = arrival[i]
                previous = 1
            while i < n and arrival[i] <= time:
                queue[state[i]].append(i)
                i += 1
            direction = previous if queue[previous] else 1 - previous
            person = queue[direction].popleft()
            answer[person] = time
            time += 1
            previous = direction
        return answer
