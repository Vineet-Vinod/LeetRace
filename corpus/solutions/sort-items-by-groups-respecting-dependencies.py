from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:
        groups = group[:]
        for i in range(n):
            if groups[i] == -1:
                groups[i] = m
                m += 1
        members = [[] for _ in range(m)]
        item_edges = [set() for _ in range(n)]
        item_degree = [0] * n
        group_edges = [set() for _ in range(m)]
        group_degree = [0] * m
        for i in range(n):
            members[groups[i]].append(i)
            for j in beforeItems[i]:
                if groups[i] == groups[j]:
                    item_edges[j].add(i)
                    item_degree[i] += 1
                elif groups[i] not in group_edges[groups[j]]:
                    group_edges[groups[j]].add(groups[i])
                    group_degree[groups[i]] += 1
        orders = [[] for _ in range(m)]
        for g, items in enumerate(members):
            queue = [i for i in items if item_degree[i] == 0]
            heapify(queue)
            while queue:
                u = heappop(queue)
                orders[g].append(u)
                for v in item_edges[u]:
                    item_degree[v] -= 1
                    if item_degree[v] == 0:
                        heappush(queue, v)
            if len(orders[g]) != len(items):
                return []
        queue = [
            (orders[g][0], g) for g in range(m) if orders[g] and group_degree[g] == 0
        ]
        heapify(queue)
        answer = []
        while queue:
            _, g = heappop(queue)
            answer.extend(orders[g])
            for h in group_edges[g]:
                group_degree[h] -= 1
                if group_degree[h] == 0:
                    heappush(queue, (orders[h][0], h))
        return answer if len(answer) == n else []
