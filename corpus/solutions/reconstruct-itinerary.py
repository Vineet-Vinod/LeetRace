from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)
        stack = ["JFK"]
        route = []
        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                route.append(stack.pop())
        return route[::-1]
