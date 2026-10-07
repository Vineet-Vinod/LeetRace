from heapq import heapify, heappop, heappush


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph = {c: set() for w in words for c in w}
        indegree = dict.fromkeys(graph, 0)
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in graph[x]:
                        graph[x].add(y)
                        indegree[y] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""
        ready = [c for c in graph if indegree[c] == 0]
        heapify(ready)
        answer = []
        while ready:
            c = heappop(ready)
            answer.append(c)
            for d in graph[c]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    heappush(ready, d)
        return "".join(answer) if len(answer) == len(graph) else ""
