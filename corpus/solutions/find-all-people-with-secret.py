from collections import defaultdict
from itertools import groupby


class Solution:
    def findAllPeople(
        self, n: int, meetings: list[list[int]], firstPerson: int
    ) -> list[int]:
        known = {0, firstPerson}
        for _, events in groupby(
            sorted(meetings, key=lambda m: m[2]), key=lambda m: m[2]
        ):
            graph = defaultdict(list)
            for a, b, _ in events:
                graph[a].append(b)
                graph[b].append(a)
            stack = [u for u in graph if u in known]
            reached = set(stack)
            while stack:
                for v in graph[stack.pop()]:
                    if v not in reached:
                        reached.add(v)
                        stack.append(v)
            known.update(reached)
        return sorted(known)
