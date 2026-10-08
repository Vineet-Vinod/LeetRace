class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for prerequisite, course in relations:
            prerequisite -= 1
            course -= 1
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(index for index, degree in enumerate(indegree) if degree == 0)
        semesters = completed = 0
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                completed += 1
                for following in graph[course]:
                    indegree[following] -= 1
                    if indegree[following] == 0:
                        queue.append(following)
        return semesters if completed == n else -1
