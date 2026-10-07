class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        richer_than = [[] for _ in range(n)]
        indegree = [0] * n
        for rich, poor in richer:
            richer_than[rich].append(poor)
            indegree[poor] += 1
        answer = list(range(n))
        queue = deque(i for i in range(n) if indegree[i] == 0)
        while queue:
            person = queue.popleft()
            for poorer in richer_than[person]:
                if quiet[answer[person]] < quiet[answer[poorer]]:
                    answer[poorer] = answer[person]
                indegree[poorer] -= 1
                if indegree[poorer] == 0:
                    queue.append(poorer)
        return answer
