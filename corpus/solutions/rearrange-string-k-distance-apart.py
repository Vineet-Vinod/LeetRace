from collections import Counter, deque
from heapq import heapify, heappop, heappush


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(heap)
        waiting = deque()
        answer = []
        for i in range(len(s)):
            while waiting and waiting[0][0] <= i:
                _, count, char = waiting.popleft()
                heappush(heap, (count, char))
            if not heap:
                return ""
            count, char = heappop(heap)
            answer.append(char)
            if count + 1 < 0:
                waiting.append((i + k, count + 1, char))
        return "".join(answer)
